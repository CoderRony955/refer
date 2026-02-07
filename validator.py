from rich.console import Console
from rich.prompt import Prompt
import platform
import subprocess
import os

from service_install_commands import (
    WIN_CLOUDFLARED_INSTALL,
    LINUX_CLOUDFLARED_INSTALL,
    MACOS_CLOUDFLARED_INSTALL,
)

console = Console()


class Validate:
    @staticmethod
    def path(path: str):
        """Validate given path 
        """
        try:
            target_path = ""
            if path.startswith("\'"):
                target_path = path.replace("\'", "")

            elif path.startswith("\"", ""):
                target_path = path.replace("\"", "")

            if not os.path.exists(path=target_path):
                return False
            return True
        except Exception as e:
            return e

    @staticmethod
    def packages(pkgs: list[str]):
        """Validate packages paths and then further take action upon it

        Args:
            pkgs (list[str]): packages names or paths
        """
        try:
            for pkg in pkgs:
                if not os.path.exists(pkg):
                    return False
            return True
        except Exception as e:
            return e

    @staticmethod
    def tunneling_services(option: str):
        """Validate tunneling service in user's system, if not found then install it
        """
        try:
            if option == "1":
                check = subprocess.run(
                    ["cloudflared", "--version"], shell=True, capture_output=True)

                # if cloudflared not found in machine
                if check.stderr:
                    # for windows
                    if platform.system() == "Windows":
                        console.print(
                            "[yellow]cloudflared is not found in your machine! Try to install automatically.[/yellow]")

                        # install via winget
                        os.system(WIN_CLOUDFLARED_INSTALL)
                        console.print(
                            "[green]cloudflared installed![/green] [cyan]Now restart refer.[/cyan]")
                        return

                    # for linux
                    elif platform.system() == "Linux":
                        console.print(
                            "[yellow]cloudflared is not found in your machine! Try to install automatically.[/yellow]")

                        # install via wget
                        os.system(LINUX_CLOUDFLARED_INSTALL)
                        console.print(
                            "[green]cloudflared installed![/green] [cyan]Now restart refer.[/cyan]")
                        return

                    # for macos
                    elif platform.system() == "Darwin":
                        console.print(
                            "[yellow]cloudflared is not found in your machine! Try to install automatically.[/yellow]")

                        # install via brew
                        os.system(MACOS_CLOUDFLARED_INSTALL)
                        console.print(
                            "[green]cloudflared installed![/green] [cyan]Now restart refer.[/cyan]")
                        return

                    else:
                        console.print("[!] Unkown OS[/yellow]")
                        return
                else:
                    # if cloudlflared is already installed in machine
                    console.print(
                        f"[green]{subprocess.run(["cloudflared", "--version"], capture_output=True, shell=True).stdout}[/green]")
                    return

            elif option == "2":
                # first of all check if ngrok auth token is null in config then ask user to enter it
                import yaml

                # read config file
                with open("./referconfig.yaml", "r") as file:
                    config = yaml.safe_load(file.read())

                ngrok_auth = config["ngrok_auth"]

                # if auth token is null
                if not ngrok_auth:
                    while True:
                        auth = Prompt.ask(
                            "\n[bold]Get your ngrok auth token from:[/bold] [cyan]https://dashboard.ngrok.com/[/cyan] \nEnter your ngrok auth token: ")
                        print()

                        if auth.lower() == "quit":
                            return False

                        if not auth:
                            console.print(
                                "[yellow][!] please enter your ngrok auth token to continue or type 'quit' to exit from operation[/yellow]")
                            continue

                        # write auth token to config file
                        config["ngrok_auth"] = auth
                        with open("./referconfig.yaml", "w") as f:
                            yaml.safe_dump(config, f, sort_keys=False)
                        return True

                # if auth token is already stored in config file
                return True
        except Exception as e:
            return e
