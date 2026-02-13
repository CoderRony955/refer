from rich.console import Console
from validator import Validate
from filterer import Filter
from server.flask_server import Start_server
import shutil
import os

console = Console()


def referwith_message_th_path(paths: list[str], message: str):
    try:
        packages_paths = []  # to store all packages paths that are valid and found

        for path in paths:
            if Validate.path(path=Filter.word(path)):
                packages_paths.append(path)

        if len(packages_paths) < 1:
            console.print(
                f"[yellow] [!] Unable to find packages with such paths.[/yellow]")
            return

        # create temp zip folder of target package in ./temphold dir
        console.print(
            f"[cyan]Copying all shareable packages and creating single temp .zip folder to share of temp just wait for couple of seconds![/cyan]")

        destination = "./temphold/shareable_packages"

        os.makedirs(destination, exist_ok=True)

        for folder in packages_paths:
            name = os.path.basename(folder)   # only folder name
            dst = os.path.join(destination, name)
            shutil.copytree(folder, dst, ignore=shutil.ignore_patterns('.git'))

        shutil.make_archive(
            "./temphold/shareable_packages", "zip", destination
        )

        # remove shareable_packages tree after converting it to archive
        shutil.rmtree("./temphold/shareable_packages")

        # start process to start server
        Server = Start_server(
            shareable_folder=".\\temphold\\shareable_packages.zip", message=message)
        return Server.run()  # run
    except Exception as e:
        console.print(f"[yellow] [!] {e} [/yellow]")
