from http.server import HTTPServer, SimpleHTTPRequestHandler
from functools import partial
from validator import Validate
from rich.console import Console
from rich.prompt import Prompt
from pathlib import Path
from pyngrok import ngrok
import subprocess
import shutil
import sys
import re


console = Console()


class Create_Tunnel_For_Non_Flask_Server:
    def __init__(self, port: str, path: str):
        self.port = port
        self.path = path

    def cloudflared(self, pkg_name: str):
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
                            f"\n[bold][Download URL][/bold] [green]{tunnel_url}/{pkg_name}.zip[/green]\n")

            # after closing tunnel connection delete that temp zip folder that is created for only specific point of time
            temphold = Path("././temphold")
            for item in temphold.iterdir():
                if item.is_dir():
                    shutil.rmtree(item)
                else:
                    item.unlink()
            console.print("[yellow]Connection closed![/yellow]")
            return

        except KeyboardInterrupt:
            pass

    def ngrok(self, pkg_name: str):
        """Start tunnel using ngrok service 
        """
        tunnel_url = ngrok.connect(self.port)
        console.print(
            f"\n[bold][Download URL][/bold] [green]{tunnel_url.public_url}/{pkg_name}.zip[/green]\n")

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
            return
        except Exception:
            pass


class Start_server:
    """Start local server and then start tunneling service as per user choice
    """
    @staticmethod
    def non_flask(pkg_path: str):
        """Start non flask server
        """
        try:
            # ask to enter port number
            port = ""
            while True:
                port = input("Enter the port number: ")
                if not port.isdigit():
                    console.print(
                        "[yellow] [!] Please write in digits! e.g. 3000[/yellow]")
                    continue
                break

            host = "0.0.0.0"
            port = int(port)

            folder_to_serve = r".\temphold"

            handler = partial(SimpleHTTPRequestHandler,
                              directory=folder_to_serve)

            server = HTTPServer((host, port), handler)

            # ask to choose one service to expose local server to public
            service = ""
            while True:
                service = Prompt.ask(
                    "Please select one service to start server:\n1. [bold]Cloudflared[/bold] type [1]\n2. [bold]Ngrok[/bold] type [2]\n")
                if service not in ["1", "2"]:
                    console.print(
                        "[yellow] [!] Please select from [1] for cloudflared\n[2] for ngrok[/yellow]")
                    continue

                Tunnel = Create_Tunnel_For_Non_Flask_Server(
                    port=port, path=pkg_path)
                package_name = Path(pkg_path).name

                # create temp zip folder of target package in ./temphold dir
                console.print(
                    f"[cyan]Creating copy of temp[/cyan] [bold]{package_name}.zip[/bold] [cyan]just wait for couple of seconds![/cyan]")
                shutil.make_archive(
                    f"./temphold/{package_name}", "zip", pkg_path)

                # if user select cloudflared
                if service == "1":
                    console.print(
                        f"Serving localhost on at port: [bold]{port}[/bold]")

                    # run local server on another seperate thread to prevent from blocking
                    import threading
                    threading.Thread(
                        target=server.serve_forever,
                        daemon=True
                    ).start()

                    Validate.tunneling_services(option="1")
                    return Tunnel.cloudflared(pkg_name=package_name)

                # if user select ngrok
                elif service == "2":
                    console.print(
                        f"Serving localhost on at port: [bold]{port}[/bold]")

                    # run local server on another seperate thread to prevent from blocking
                    import threading
                    threading.Thread(
                        target=server.serve_forever,
                        daemon=True
                    ).start()

                    Validate.tunneling_services(option="2")
                    return Tunnel.ngrok(pkg_name=package_name)
        except Exception as e:
            console.print(e)
