from rich.console import Console
from rich.prompt import Prompt
from filterer import Filter
from operations.basic import about, redirect
from operations.referral import refer, referwith_template
from operations.referral import (
    referwith_message
)

from startup import OnStartup
from operations.basic import (
    usage,
)

import sys

console = Console()


class Handler:
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

    def referwith_message_with_template_through_paths(self, command: str):
        """Handle referwith template command to share multiple packages through their local paths in cool template with message
        """
        import shlex
        try:
            user_command = shlex.split(command)
        except ValueError:
            console.print("[red]Invalid command format[/red]")
            return False

        # Expected pattern:
        # referwith -template -message <msg> -paths <path1> <path2> ...

        if len(user_command) < 5:
            console.print(
                "[red]Wrong use of[/red] referwith [red]command! To refer multiple packages through their local paths in cool template with custom message[/red]\n"
                "[bold]Use like this:[/bold] referwith -template -message \"<your_message>\" -paths \"path 1\" \"path 2\" \"path 3\"  \"path 3\"\n"
            )
            return False

        if (
            user_command[0] != "referwith"
            or user_command[1] != "-template"
            or user_command[2] != "-message"
            or "-paths" not in user_command
        ):
            console.print("[red]Invalid referwith -template command[/red]")
            return False

        paths_index = user_command.index("-paths")

        # message is right after -message
        message = user_command[3]

        # everything after -paths is a package name
        paths = user_command[paths_index + 1:]

        if not paths:
            console.print("[red]No package paths provided[/red]")
            return False

        local_paths = [Filter.word(path) for path in paths]
        referwith_template.referwith_template_th_path(
            paths=local_paths,
            message=Filter.word(message)
        )

        return True

    def main_handler(self):
        """Main handler
        """
        while True:
            try:
                user = Prompt.ask("\n[bold]>_[/bold] ")
                user_lower = user.lower()

                # if user enter without typing anything then ignore
                if not user:
                    pass

                # --------------------------------------------------------
                #                   BASIC COMMMANDS
                # --------------------------------------------------------

                # display about refer in proper markdown format
                elif user_lower == "about":
                    about.show_about()

                # display usage documentation
                elif user_lower == "usage":
                    usage.show_usage()
                    usage.show_command_quick_reference()

                # redirect to official github repository
                elif user_lower == "contribute":
                    redirect.to_official_repository()

                    # --------------------------------------------------------
                    #                   REFERRAL COMMMANDS
                    # --------------------------------------------------------

                    # to refer by path and create downloadable link
                elif user_lower.startswith("refer -path"):
                    handle = self.refer_with_local_path_command(user)
                    if not handle:
                        continue

                # to refer multiple packages with message through paths
                elif user_lower.startswith("referwith -message") and "-paths" in user_lower:
                    handle = self.referwith_message_through_paths(
                        user)
                    if not handle:
                        continue

                # to refer multiple packages through paths with message and with cool available template options
                elif user_lower.startswith("referwith -template") and "-paths" in user_lower:
                    handle = self.referwith_message_with_template_through_paths(
                        user)
                    if not handle:
                        continue

                # display all available options
                elif user_lower == "help" or user_lower == "h":
                    commands = OnStartup()
                    commands.commands_display()

                # to quit application
                elif user_lower == "q" or user_lower == "quit" or user_lower == "exit":
                    sys.exit(0)
                else:
                    console.print(f"[red]Wrong command![/red]")
            except EOFError:
                console.print(
                    "[bold]use ctrl + c / cmd + c again to exit[/bold]")
