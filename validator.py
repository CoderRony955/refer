from rich.console import Console
import platform
import subprocess
import os

from service_install_commands import (
    WIN_CLOUDFLARED_INSTALL,
    WIN_NGROK_INSTALL,

    LINUX_CLOUDFLARED_INSTALL,
    LINUX_NGROK_INSTALL,

    MACOS_CLOUDFLARED_INSTALL,
    MACOS_NGROK_INSTALL
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
                check = subprocess.run(
                    ["ngrok", "--version"], shell=True, capture_output=True)

                # if ngrok not found in machine
                if check.stderr:
                    # for windows
                    if platform.system() == "Windows":
                        console.print(
                            "[yellow]ngrok is not found in your machine! Try to install automatically.[/yellow]")

                        # install via winget
                        os.system(WIN_NGROK_INSTALL)
                        console.print(
                            "[green]ngrok installed![/green] [cyan]Now exit from refer and add your ngrok auth token using command[/cyan] [bold]ngrok config add-authtoken <your-auth-token>[/bold] [cyan]then restart refer in order to use same command.[/cyan]")
                        return

                    # for linux
                    elif platform.system() == "Linux":
                        console.print(
                            "[yellow]ngrok is not found in your machine! Try to install automatically.[/yellow]")

                        # install via curl & apt
                        os.system(LINUX_NGROK_INSTALL)
                        console.print(
                            "[green]ngrok installed![/green] [cyan]Now exit from refer and add your ngrok auth token using command[/cyan] [bold]ngrok config add-authtoken <your-auth-token>[/bold] [cyan]then restart refer in order to use same command.[/cyan]")
                        return

                    # for macos
                    elif platform.system() == "Darwin":
                        console.print(
                            "[yellow]ngrok is not found in your machine! Try to install automatically.[/yellow]")

                        # install via brew
                        os.system(MACOS_NGROK_INSTALL)
                        console.print(
                            "[green]ngrok installed![/green] [cyan]Now exit from refer and add your ngrok auth token using command[/cyan] [bold]ngrok config add-authtoken <your-auth-token>[/bold] [cyan]then restart refer in order to use same command.[/cyan]")
                        return

                    else:
                        console.print("[!] Unkown OS[/yellow]")
                        return
                else:
                    # if ngrok is already installed in machine
                    console.print(
                        f"[green]{subprocess.run(["ngrok", "--version"], capture_output=True, shell=True).stdout}[/green]")
                    return
        except Exception as e:
            return e
