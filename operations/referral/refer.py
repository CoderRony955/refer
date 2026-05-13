from rich.console import Console
from validator import Validate
from filterer import Filter
from server.non_flask_server import Start_server

console = Console()


def refer_path(path: str):
    try:
        # if given path is not valid
        if not Validate.path(path=Filter.word(path)):
            console.print(
                f"[bold]{path}[/bold] [yellow] [!] Path not found![/yellow]")
            return

        # if path is valid then futher take action upon it
        Start_server.non_flask(pkg_path=Filter.word(path))
    except Exception as e:
        console.print(e)
