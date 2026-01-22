from rich.console import Console
from rich.prompt import Prompt
from startup import OnStartup
import asyncio

console = Console()


class Handler:
    async def main_handler(self):
        while True:
            try:
                user = Prompt.ask("\n[bold]>_[/bold] ")
                if user == "ok":
                    pass
                    # after successful log in display all commands
                elif user == "":
                    pass

                elif user == "help" or user == "h":
                    commands = OnStartup()
                    commands.commands_display()
                else:
                    console.print(f"[red]Wrong command![/red]")
            except EOFError:
                console.print(
                    "[bold]use ctrl + c / cmd + c again to exit[/bold]")
