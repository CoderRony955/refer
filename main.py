from rich.console import Console
from startup import OnStartup
from causal_keywords import Keywords
from command_handler import Handler
import asyncio
import random
import os

console = Console()


async def main():
    # on startup display app description
    startup = OnStartup()
    startup.description_display()

    # config file already exist than directly ask for password if password match in five times try then move on forward otherwise exit from app
    if os.path.exists("./referconfig.yaml"):
        if not startup.ask_for_pass():
            console.print(
                "[bold red]After trying some times your password doesn't match![/bold red]")
            return
        else:
            console.print(
                f"[bold green]{random.choice(Keywords.success_keywords)}[/bold green]\n")
    else:
        try:
            await startup.check_config_file()

            # after config file checking or creating new one display all available commands
            console.print("[bold]Here is the all available options![/bold]\n")
            startup.commands_display()
            commands_handler = Handler()
            await commands_handler.main_handler()
        except Exception:
            pass


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        console.print("[bold]Exit![/bold]")
