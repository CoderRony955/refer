from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.markdown import Markdown
from colors import TEXT_COLORS
from commands import AllCommands
from causal_keywords import Keywords
import random
import asyncio
import maskpass
import yaml
import os

console = Console()


class OnStartup:
    async def check_config_file(self):
        """check referconfig.yaml file if not found then create new one
        """
        with console.status(status=f"[green]{random.choice(Keywords.start_keywords)}[/green]...", spinner="star"):
            await asyncio.sleep(4)

        # if config file does not exist
        console.print(
            "\nEnter required credentials to make your referral & management easy with refer:\n\n")

        # ask user to enter their required credentials
        # password
        while True:
            password = maskpass.askpass(
                prompt="1. Set new password for refer: ", mask="*")

            if not password:
                print("Please set a new password first!\n")
                continue
            break

        # Ask user for if user want's to use refer local or not
        while True:
            referdb = Prompt.ask(
                "2. If you want's to use [bold]refer local db[/bold], then type [Yes] otherwise [No]: ")

            if not referdb:
                console.print(
                    "[yellow]please select from [Yes]/[No][/yellow]\n")
                continue

            options = ["Yes", "yes", "No", "no"]
            if referdb not in options:
                console.print(
                    "[yellow]Wrong option! Please select from [Yes]/[No][/yellow]\n")
                continue
            break

        print()  # for one line spacing

        # user type 'Yes' then ask user for any secret specific location to create local db
        location = ""

        if referdb == "Yes" or referdb == "yes":
            while True:
                location = Prompt.ask(
                    "Enter the any secret specific path here where [bold]refer local db[/bold] has been created: ")

                if not location:
                    continue

                if not os.path.exists(location):
                    console.print("[yellow]location not found![/yellow]\n")
                    continue

                if os.path.exists(f"{location}\\referdb"):
                    console.print(
                        f"{location}\\referdb [yellow][!] referdb folder already exist!\n")
                    break

                # create db folder
                os.mkdir(f"{location}\\referdb")
                break

        elif referdb == "No" or referdb == "no":
            console.print(
                "Alright! It seems like you don't want to use refer local db. 😃")

            # create config file to store all credentials
        credentials = {
            "password": password,
            "referdb_location": location or None
        }
        with open('referconfig.yaml', 'w') as file:
            yaml.safe_dump(credentials, file, sort_keys=False)

        console.print(
            f"[bold green]{random.choice(Keywords.confirmation_keywords)}[/bold green]\n")

    def ask_for_pass(self):
        """ask for password to login into refer 
        """
        try:
            with open("./referconfig.yaml", "r") as file:
                config = yaml.safe_load(file.read())

            times = 0
            while times < 5:
                ask = maskpass.askpass(
                    prompt="Enter the passsword to login: ", mask="*")

                if ask == config['password']:
                    return True

                console.print(f"[red]Oops! Wrong password[/red]\nTry again!\n")
                times += 1

            return False
        except Exception as e:
            print(e)

    def description_display(self):
        """Display ASCII Refer text with about their description
        """
        with open("./ascii.txt", 'r') as file:
            ascii_text = file.read()
        with open("./about.md", "r") as mdfile:
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

        for command, forr in AllCommands.BASIC_COMMANDS.items():
            basic_commands.add_row(f"[bold cyan]{command}[/bold cyan]", forr)

        console.print(basic_commands)

        # management commands
        management_commands = Table(
            title="MANAGEMENT COMMANDS", show_lines=True)
        management_commands.add_column("command", width=80)
        management_commands.add_column("for", width=80)
        management_commands.add_column("example", width=90)

        for command, detail in AllCommands.MANAGEMENT_COMMANDS.items():
            management_commands.add_row(f"[bold cyan]{command}[/bold cyan]", detail.get(
                'for'), detail.get('example'))

        console.print(management_commands)

        # ----------------------------------------------------
        #                 Referral commands
        # ----------------------------------------------------
        # commands for referral from refer's local db
        referral_from_db_commands = Table(
            title="COMMANDS FOR REFERRAL THROUGH DB", show_lines=True, border_style="blue")
        referral_from_db_commands.add_column("command")
        referral_from_db_commands.add_column("for")
        referral_from_db_commands.add_column("example")

        for command, detail in AllCommands.REFERRAL_FROM_DB.items():
            referral_from_db_commands.add_row(f"[bold cyan]{command}[/bold cyan]", detail.get(
                'for'), detail.get('example'))

        console.print(referral_from_db_commands)

        # commands for referral directly through path
        referral_from_local_commands = Table(
            title="COMMANDS FOR REFERRAL THROUGH LOCALLY", show_lines=True, border_style="yellow")
        referral_from_local_commands.add_column("command")
        referral_from_local_commands.add_column("for")
        referral_from_local_commands.add_column("example")

        for command, detail in AllCommands.REFERRAL_FROM_LOCAL.items():
            referral_from_local_commands.add_row(f"[bold cyan]{command}[/bold cyan]", detail.get(
                'for'), detail.get('example'))

        console.print(referral_from_local_commands)
