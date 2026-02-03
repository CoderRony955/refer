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
    async def main_handler(self):
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
                    if len(user.lower().split()) != 2:
                        console.print(
                            "[red]Wrong use of[/red] changedb [red]command![/red]\n[bold]Use like this:[/bold] changedb C:\\Users\\Your-Name\\OneDrive\\SecretFolder\n")
                        continue

                    changedb.change_refer_db(user.lower().split()[1])

                # --------------------------------------------------------
                #                  MANAGEMENT COMMMANDS
                # --------------------------------------------------------

                # to add new package record to referdb including their path + name
                elif user.lower().startswith("addpkg"):
                    readable = fr"{user.lower()}"
                    command = readable.split()
                    if len(command) != 5:
                        console.print(
                            "[red]Wrong use of[/red] addpkg [red]command![/red]\n[bold]Use like this:[/bold] addpkg addpkg -name \'clitool\' -path \'C:\\Users\\<name>\\Myprojects\\tool\'\n")
                        continue

                    addpkg.addpkg(name=command[2], path=command[4])

                # to update existing package path
                elif user.lower().startswith("updatepkg"):
                    readable = fr"{user.lower()}"
                    command = readable.split()
                    if len(command) != 5:
                        console.print(
                            "[red]Wrong use of[/red] updatepkg [red]command![/red]\n[bold]Use like this:[/bold] updatepkg -name \'clitool\' -path \'C:\\Users\\<name>\\Myprojects\\tool\'\n")
                        continue

                    updatepkg.updatepkg(name=command[2], path=command[4])

                # to delete existing package path
                elif user.lower().startswith("delpkg"):
                    readable = fr"{user.lower()}"
                    command = readable.split()
                    if len(command) != 3:
                        console.print(
                            "[red]Wrong use of[/red] delpkg [red]command![/red]\n[bold]Use like this:[/bold] delpkg -name \'clitool\'\n")
                        continue

                    delpkg.delpkg(name=command[2])

                # to rename existing package name
                elif user.lower().startswith("renamepkg"):
                    readable = fr"{user.lower()}"
                    command = readable.split()
                    if len(command) != 5:
                        console.print(
                            "[red]Wrong use of[/red] renamepkg [red]command![/red]\n[bold]Use like this:[/bold] renamepkg -from \'clitool\' -to \'myclitool\'\n")
                        continue

                    renamepkg.renamepkg(
                        old_name=command[2], new_name=command[4])

                # to display all packages from referdb
                elif user.lower() == "listpkgs":
                    listpkgs.listpkgs()
                
                # to see one specific existing package details
                elif user.lower().startswith("listpkg"):
                    readable = fr"{user.lower()}"
                    command = readable.split()
                    if len(command) != 3:
                        console.print(
                            "[red]Wrong use of[/red] listpkg [red]command![/red]\n[bold]Use like this:[/bold] listpkg -name \'clitool\'\n")
                        continue

                    listpkg.listpkg(
                        name=command[2])

                # display all available options
                elif user == "help" or user == "h":
                    commands = OnStartup()
                    commands.commands_display()
                else:
                    console.print(f"[red]Wrong command![/red]")
            except EOFError:
                console.print(
                    "[bold]use ctrl + c / cmd + c again to exit[/bold]")
