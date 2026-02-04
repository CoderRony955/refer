from rich.console import Console
from rich.prompt import Prompt
from startup import OnStartup
from basic import (
    about,
    usage,
    redirect,
    wheredb,
    changedb,
)
from management import (
    addpkg,
    updatepkg,
    listpkgs,
    delpkg,
    renamepkg,
    listpkg
)
console = Console()


class Handler:
    def changedb_command(self, command: str):
        """Handle changedb command
        """
        if len(command.lower().split()) != 2:
            console.print(
                "[red]Wrong use of[/red] changedb [red]command![/red]\n[bold]Use like this:[/bold] changedb C:\\Users\\Your-Name\\OneDrive\\SecretFolder\n")
            return False

        changedb.change_refer_db(command.lower().split()[1])

    def addpkg_command(self, command: str):
        """Handle addpkg command
        """
        readable = fr"{command.lower()}"
        command = readable.split()
        if len(command) != 5:
            console.print(
                "[red]Wrong use of[/red] addpkg [red]command![/red]\n[bold]Use like this:[/bold] addpkg addpkg -name \'clitool\' -path \'C:\\Users\\<name>\\Myprojects\\tool\'\n")
            return False

        addpkg.addpkg(name=command[2], path=command[4])

    def updatepkg_command(self, command: str):
        """Handle updatepkg command
        """
        readable = fr"{command.lower()}"
        command = readable.split()
        if len(command) != 5:
            console.print(
                "[red]Wrong use of[/red] updatepkg [red]command![/red]\n[bold]Use like this:[/bold] updatepkg -name \'clitool\' -path \'C:\\Users\\<name>\\Myprojects\\tool\'\n")
            return False

        updatepkg.updatepkg(name=command[2], path=command[4])

    def delpkg_command(self, command: str):
        """Handle delpkg command
        """
        readable = fr"{command.lower()}"
        command = readable.split()
        if len(command) != 3:
            console.print(
                "[red]Wrong use of[/red] delpkg [red]command![/red]\n[bold]Use like this:[/bold] delpkg -name \'clitool\'\n")
            return False

        delpkg.delpkg(name=command[2])

    def renamepkg_command(self, command: str):
        """Handle renamepkg command
        """
        readable = fr"{command.lower()}"
        command = readable.split()
        if len(command) != 5:
            console.print(
                "[red]Wrong use of[/red] renamepkg [red]command![/red]\n[bold]Use like this:[/bold] renamepkg -from \'clitool\' -to \'myclitool\'\n")
            return False

        renamepkg.renamepkg(
            old_name=command[2], new_name=command[4])

    def listpkg_command(self, command: str):
        """Handle listpkg command
        """
        readable = fr"{command.lower()}"
        command = readable.split()
        if len(command) != 3:
            console.print(
                "[red]Wrong use of[/red] listpkg [red]command![/red]\n[bold]Use like this:[/bold] listpkg -name \'clitool\'\n")
            return False

        listpkg.listpkg(
            name=command[2])

    def refer_with_db_command(self, command: str):
        """Handle refer through db command
        """
        print(command.split())
        user_command = command.lower().split()
        if len(user_command) != 3:
            console.print(
                "[red]Wrong use of[/red] refer [red]command![/red]\n[bold]Use like this:[/bold] refer -pkg \'clitool\'\n")
            return False

        exact_command = ["refer", "-pkg"]

        for parameter in range(2):
            if user_command[parameter] not in exact_command:
                console.print(
                    "[red]Wrong use of[/red] refer [red]command![/red]\n[bold]Use like this:[/bold] refer -pkg \'clitool\'\n")
                return False
        

    async def main_handler(self):
        """Main handler
        """
        while True:
            try:
                user = Prompt.ask("\n[bold]>_[/bold] ")

                # if user enter without typing anything then ignore
                if not user:
                    pass

                # --------------------------------------------------------
                #                   BASIC COMMMANDS
                # --------------------------------------------------------

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
                elif user.lower().startswith("changedb"):
                    handle = self.changedb_command(user.lower())
                    if not handle:
                        continue

                    # --------------------------------------------------------
                    #                  MANAGEMENT COMMMANDS
                    # --------------------------------------------------------

                    # to add new package record to referdb including their path + name
                elif user.lower().startswith("addpkg"):
                    handle = self.addpkg_command(user.lower())
                    if not handle:
                        continue

                    # to update existing package path
                elif user.lower().startswith("updatepkg"):
                    handle = self.updatepkg_command(user.lower())
                    if not handle:
                        continue

                    # to delete existing package path
                elif user.lower().startswith("delpkg"):
                    handle = self.delpkg_command(user.lower())
                    if not handle:
                        continue

                    # to rename existing package name
                elif user.lower().startswith("renamepkg"):
                    handle = self.renamepkg_command(user.lower())
                    if not handle:
                        continue

                    # to display all packages from referdb
                elif user.lower() == "listpkgs":
                    listpkgs.listpkgs()

                # to see one specific existing package details
                elif user.lower().startswith("listpkg"):
                    handle = self.listpkg_command(user.lower())
                    if not handle:
                        continue

                    # --------------------------------------------------------
                    #          REFERRAL COMMMANDS (THROUGH REFERDB)
                    # --------------------------------------------------------

                    # to refer by just using downloadable link
                elif user.lower().startswith("refer -pkg"):
                    handle = self.refer_with_db_command(user.lower())
                    if not handle:
                        continue

                # display all available options
                elif user == "help" or user == "h":
                    commands = OnStartup()
                    commands.commands_display()
                else:
                    console.print(f"[red]Wrong command![/red]")
            except EOFError:
                console.print(
                    "[bold]use ctrl + c / cmd + c again to exit[/bold]")
