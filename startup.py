from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from colors import TEXT_COLORS
from commands import Commands
from dotenv import load_dotenv

load_dotenv(dotenv_path="./env")

console = Console()


class OnStartup:
    def description_display(self):
        """Display ASCII Refer text with about their description
        """
        with open("./ascii.txt", 'r') as file:
            ascii_text = file.read()
        with open("./introduction.md", "r", encoding="utf-8") as mdfile:
            about = Markdown(mdfile.read())

        print(f"{TEXT_COLORS.YELLOW}{ascii_text}{TEXT_COLORS.RESET}\n")
        console.print(about)
        print("\n")

    def commands_display(self):
        """Display all commands in category wise tables
        """
        # basic commands
        basic_commands = Table(title="BASIC COMMANDS", show_lines=True)
        basic_commands.add_column("command")
        basic_commands.add_column("for")

        for command, forr in Commands.BASIC_COMMANDS.items():
            basic_commands.add_row(f"[bold cyan]{command}[/bold cyan]", forr)

        console.print(basic_commands)

        # ----------------------------------------------------
        #                 Referral commands
        # ----------------------------------------------------
        referral_from_local_commands = Table(
            title="COMMANDS FOR REFERRAL THROUGH LOCAL PATHS", show_lines=True, border_style="yellow")
        referral_from_local_commands.add_column("command")
        referral_from_local_commands.add_column("for")
        referral_from_local_commands.add_column("example")

        for command, detail in Commands.REFERRAL_FROM_LOCAL.items():
            referral_from_local_commands.add_row(f"[bold cyan]{command}[/bold cyan]", detail.get(
                'for'), detail.get('example'))

        console.print(referral_from_local_commands)
