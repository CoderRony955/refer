from flask import Flask, render_template, send_from_directory, request
from urllib.request import urlopen
from validator import Validate
from rich.console import Console
from rich.prompt import Prompt
from pathlib import Path
from pyngrok import ngrok
import subprocess
import logging
import shutil
import sys
import re
import multiprocessing


console = Console()


def _flask_process_entry(shareable_folder: str, message: str, template: str, host: str, port: int):
    """Top-level function to run Flask in a separate process (picklable on Windows)."""
    templates_dir = str(Path(__file__).parent / 'templates')
    app = Flask(__name__, template_folder=templates_dir)

    @app.route('/')
    def template_route():
        return render_template(template, shareable_folder="/download", message=message)

    @app.route('/download')
    def download_route():
        try:
            p = Path(shareable_folder).resolve()
            if not p.exists() or not p.is_file():
                return ("Not found", 404)
            return send_from_directory(str(p.parent), p.name, as_attachment=True)
        except Exception:
            return ("Error serving file", 500)

    # simple shutdown endpoint for in-process use (not used by parent process termination)
    @app.route('/_shutdown', methods=['POST', 'GET'])
    def _shutdown_proc():
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            return ("Not running with the Werkzeug Server", 500)
        func()
        return ("Shutting down", 200)

    app.run(host=host, port=port, use_reloader=False)


class Create_Tunnel_For_Flask_Server:
    def __init__(self, port: str):
        self.port = port

    def _shutdown_flask(self):
        try:
            # request the Flask shutdown endpoint
            urlopen(f"http://127.0.0.1:{self.port}/_shutdown", timeout=2)
        except Exception:
            pass

    def cloudflared(self):
        """Start tunnel using cloudflared service 
        """
        try:
            # start tunneling service
            process = subprocess.Popen(
                ['cloudflared', 'tunnel', '--url',
                 f'http://localhost:{self.port}'],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )

            url_pattern = re.compile(r"https://[^\s]+trycloudflare\.com")
            tunnel_url = None

            for line in process.stdout:
                # print logs live
                sys.stdout.write(line)

                # try to capture the tunnel url
                if tunnel_url is None:
                    m = url_pattern.search(line)
                    if m:
                        tunnel_url = m.group(0)
                        console.print(
                            f"\n[bold][Webpage URL][/bold] [green]{tunnel_url}[/green]\n")

            # after closing tunnel connection delete that temp zip folder that is created for only specific point of time
            temphold = Path("././temphold")
            for item in temphold.iterdir():
                if item.is_dir():
                    shutil.rmtree(item)
                else:
                    item.unlink()
            console.print("[yellow]Connection closed![/yellow]")
            # try to shutdown flask server running in background
            try:
                self._shutdown_flask()
            except Exception:
                pass
            return

        except KeyboardInterrupt:
            try:
                self._shutdown_flask()
            except Exception:
                pass
            return

    def ngrok(self):
        """Start tunnel using ngrok service 
        """
        tunnel_url = ngrok.connect(self.port)
        console.print(
            f"\n[bold][Webpage URL][/bold] [green]{tunnel_url.public_url}[/green]\n")

        try:
            input("Press ENTER to close connection...\n")

            # after closing tunnel connection delete that temp zip folder that is created for only specific point of time
            temphold = Path("././temphold")
            for item in temphold.iterdir():
                if item.is_dir():
                    shutil.rmtree(item)
                else:
                    item.unlink()
            console.print("[yellow]Connection closed![/yellow]")
            try:
                self._shutdown_flask()
            except Exception:
                pass
            return
        except Exception:
            pass


class Start_server:
    """Start Flask local server and then start tunneling service as per user choice
    """

    def __init__(self, shareable_folder: str, message: str = "Hey! Here is my projects.", template: str = "skeleton.html"):
        self.app = Flask(__name__)
        self.shareable_folder = shareable_folder
        self.message = message
        self.template = template

    def run_flask_with_start_message(self, app, host: str, port: int, debug=False):
        """Start flask server and while serving localhost flask server display messages
        """
        werkzeug_logger = logging.getLogger("werkzeug")
        original_level = werkzeug_logger.level

        # Hide logs while starting
        werkzeug_logger.setLevel(logging.ERROR)

        @self.app.before_request
        def _on_ready():
            werkzeug_logger.setLevel(original_level)

        console.print(
            "⏳ [bold cyan]Server is starting, please wait...[/bold cyan]")

        app.run(host=host, port=port, use_reloader=False, debug=debug)

    def start(self, host: str, port: int):
        """Start flask local server on given specific port
        """
        @self.app.route('/')
        def template():
            # render page with download link routed to /download
            return render_template(self.template, shareable_folder="/download", message=self.message)

        @self.app.route('/_shutdown', methods=['POST', 'GET'])
        def _shutdown():
            func = request.environ.get('werkzeug.server.shutdown')
            if func is None:
                return ("Not running with the Werkzeug Server", 500)
            func()
            return ("Shutting down", 200)

        @self.app.route('/download')
        def download():
            # serve the shareable file (zip) from its directory
            try:
                p = Path(self.shareable_folder)
                # resolve relative paths like ".\\temphold\\shareable_packages.zip"
                p = p.resolve()
                if not p.exists() or not p.is_file():
                    return ("Not found", 404)

                return send_from_directory(str(p.parent), p.name, as_attachment=True)
            except Exception as e:
                console.print(e)
                return ("Error serving file", 500)
        self.run_flask_with_start_message(self.app, host, port)

    def run(self):
        """Start flask server
        """
        try:
            # ask to enter port number
            port = ""
            while True:
                port = input("Enter the port number: ")
                if not port.isdigit():
                    console.print(
                        "[yellow][!] Please write in digits! e.g. 3000[/yellow]\n")
                    continue
                break

            host = "0.0.0.0"
            port = int(port)

            console.print(
                "[bold green]Flask server is starting, please be paitent and wait for couple of seconds...[bold green]\n")

            # run flask in a separate process so we can terminate it reliably
            proc = multiprocessing.Process(target=_flask_process_entry, args=(
                self.shareable_folder, self.message, self.template, host, port))
            proc.daemon = True
            proc.start()
            self.flask_process = proc
            console.print(
                f"[cyan]Starting Flask local server at port:[/cyan] {port}")

            from . import timer
            timer.timer(10)
            print()  # for spacing

            console.print(
                f"[bold green]Flask server is running at port:[bold green] {port}\n")

            # ask to choose one service to expose local server to public
            service = ""
            while True:
                service = Prompt.ask(
                    "Please select one service to start server:\n1. [bold]Cloudflared[/bold] type [1]\n2. [bold]Ngrok[/bold] type [2]\n")
                if service not in ["1", "2"]:
                    console.print(
                        "[yellow][!] Please select from [1] for cloudflared\n[2] for ngrok[/yellow]\n")
                    continue

                # tunneling service
                Tunnel = Create_Tunnel_For_Flask_Server(port=str(port))

                # if user select cloudflared
                if service == "1":
                    Validate.tunneling_services(option="1")
                    # block here while tunnel is open; when it returns, terminate flask process and exit
                    try:
                        Tunnel.cloudflared()
                    finally:
                        try:
                            if hasattr(self, 'flask_process') and self.flask_process.is_alive():
                                self.flask_process.terminate()
                                self.flask_process.join(timeout=2)
                        except Exception:
                            pass
                        console.print("[green]Exiting...[/green]")
                        sys.exit(0)

                # if user select ngrok
                elif service == "2":
                    if Validate.tunneling_services(option="2"):
                        try:
                            Tunnel.ngrok()
                        finally:
                            try:
                                if hasattr(self, 'flask_process') and self.flask_process.is_alive():
                                    self.flask_process.terminate()
                                    self.flask_process.join(timeout=2)
                            except Exception:
                                pass
                            console.print("[green]Exiting...[/green]")
                            sys.exit(0)
                    return
        except Exception as e:
            console.print(e)
