from rich.console import Console
from startup import OnStartup
from command_handler import Handler
import os

console = Console()
commands_handler = Handler()
startup = OnStartup()


def main():
    # on startup display app welcome screen and commands
    startup.description_display()
    startup.commands_display()

    # call main command handler
    commands_handler.main_handler()

if __name__ == "__main__":
    try:
        os.makedirs("./temphold", exist_ok=True)
        main()
    except KeyboardInterrupt:
        console.print("[bold]Exit![/bold]")
