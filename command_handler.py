from rich.console import Console
from rich.prompt import Prompt
from filterer import Filter
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

from referral.fromreferdb import (
    refer,
    referwith_message
)

from referral.fromsystem import (
    refer,
    referwith_message
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

        refer.refer_pkg(name=user_command[2])

    def refer_with_local_path_command(self, command: str):
        """Handle refer through system's local path command
        """
        user_command = command.lower().split()
        if len(user_command) != 3:
            console.print(
                "[red]Wrong use of[/red] refer [red]command![/red]\n[bold]Use like this:[/bold] refer -path \'<path>\'\n")
            return False

        exact_command = ["refer", "-path"]

        for parameter in range(2):
            if user_command[parameter] not in exact_command:
                console.print(
                    "[red]Wrong use of[/red] refer [red]command![/red]\n[bold]Use like this:[/bold] refer -path \'<path>\'\n")
                return False

        refer.refer_path(path=user_command[2])

    def referwith_message_through_pkg_names(self, command: str):
        """Handle referwith message command to share multiple packages through their names
        """
        import shlex
        try:
            user_command = shlex.split(command.lower())
        except ValueError:
            console.print("[red]Invalid command format[/red]")
            return False

        # Expected pattern:
        # referwith -message <msg> -pkgs <pkg1> <pkg2> ...

        if len(user_command) < 5:
            console.print(
                "[red]Wrong use of[/red] referwith [red]command! To refer multiple packages through their names[/red]\n"
                "[bold]Use like this:[/bold] referwith -message \"<your_message>\" -pkgs \"health_monitor chatbot clitool guiapp\"\n"
            )
            return False

        if (
            user_command[0] != "referwith"
            or user_command[1] != "-message"
            or "-pkgs" not in user_command
        ):
            console.print("[red]Invalid referwith command[/red]")
            return False

        pkgs_index = user_command.index("-pkgs")

        # message is right after -message
        message = user_command[2]

        # everything after -pkgs is a package name
        pkgs = user_command[pkgs_index + 1:]

        if not pkgs:
            console.print("[red]No package names provided[/red]")
            return False

        pkgs_names = [Filter.word(pkg) for pkg in pkgs]
        referwith_message.referwith_message(
            pkgs=pkgs_names,
            message=Filter.word(message)
        )

        return True
    
    def referwith_message_through_paths(self, command: str):
        """Handle referwith message command to share multiple packages through their system paths
        """
        import shlex

        try:
            user_command = shlex.split(command)
        except ValueError:
            console.print("[red]Invalid command format[/red]")
            return False

        if len(user_command) < 5:
            console.print(
                "[red]Wrong use of[/red] referwith [red]command![/red]\n"
                "[bold]Use like this:[/bold]\n"
                'referwith -message "your message" -paths "path 1" "path 2" "path 3"\n'
            )
            return False

        if (
            user_command[0] != "referwith"
            or user_command[1] != "-message"
            or "-paths" not in user_command
        ):
            console.print("[red]Invalid referwith command[/red]")
            return False

        paths_index = user_command.index("-paths")

        message = user_command[2]

        # collect paths after -paths until another flag appears
        paths = []
        for token in user_command[paths_index + 1:]:
            if token.startswith("-"):
                break
            paths.append(token)

        if not paths:
            console.print("[red]No package paths provided[/red]")
            return False

        pkgs_paths = [Filter.word(p) for p in paths]

        referwith_message.referwith_message_th_path(
            paths=pkgs_paths,
            message=Filter.word(message)
        )

        return True


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

                    # to refer by name and create downloadable link
                elif user.lower().startswith("refer -pkg"):
                    handle = self.refer_with_db_command(user.lower())
                    if not handle:
                        continue

                    # to refer multiple packages with message
                elif user.lower().startswith("referwith -message") and "-pkgs" in user.lower():
                    handle = self.referwith_message_through_pkg_names(
                        user.lower())
                    if not handle:
                        continue

                    # --------------------------------------------------------
                    #        REFERRAL COMMMANDS (THROUGH SYSTEM's PATH)
                    # --------------------------------------------------------

                    # to refer by path and create downloadable link
                elif user.lower().startswith("refer -path"):
                    handle = self.refer_with_local_path_command(user.lower())
                    if not handle:
                        continue
                
                # to refer multiple packages with message through paths
                elif user.lower().startswith("referwith -message") and "-paths" in user.lower():
                    handle = self.referwith_message_through_paths(
                        user.lower())
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
