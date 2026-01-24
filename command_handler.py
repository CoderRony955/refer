from rich.console import Console
from rich.prompt import Prompt
from startup import OnStartup
from basic import (
    about,
    usage,
    redirect,
    wheredb,
    changedb
)
console = Console()


class Handler:
    async def main_handler(self):
        while True:
            try:
                user = Prompt.ask("\n[bold]>_[/bold] ")

                # if user enter without typing anything then ignore
                if not user:
                    pass

                # display about refer in proper markdown format
                elif user.lower() == "about":
                    about.show_about()

                # display usage documentation
                elif user.lower() == "usage":
                    usage.show_usage()
                    usage.show_command_quick_reference()

                # redirect to official github repository
                elif user.lower() == "contribute":
                    redirect.to_official_repository()

                # display refer db folder location
                elif user.lower() == "wheredb":
                    wheredb.display_referdb_location()

                # to change or shift referdb location
                elif user.lower().split()[0] == "changedb":
                    if len(user.lower().split()) != 2:
                        console.print(
                            "[red]Wrong use of[/red] changedb [red]command![/red]\n[bold]Use like this:[/bold] changedb C:\\Users\\Your-Name\\OneDrive\\SecretFolder\n")
                        continue

                    changedb.change_refer_db(user.lower().split()[1])

                # display all available options
                elif user == "help" or user == "h":
                    commands = OnStartup()
                    commands.commands_display()
                else:
                    console.print(f"[red]Wrong command![/red]")
            except EOFError:
                console.print(
                    "[bold]use ctrl + c / cmd + c again to exit[/bold]")
