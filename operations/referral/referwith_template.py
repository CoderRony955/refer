from rich.console import Console
from validator import Validate
from filterer import Filter
from server.flask_server import Start_server
import shutil
import json
import os
from urllib.parse import urlparse

console = Console()


def choose_template():
    """Ask user to choose template from available options
    """
    try:
        # read templates.json
        with open("./operations/referral/templates.json", "r") as file:
            templates = json.load(file)

        while True:
            console.print(
                "\n[bold]please choose the template from available options[/bold]: \n")
            for template in templates:
                console.print(f"[bold]{template["id"]}. {template["name"]}")
            console.print(
                "just enter the name of template e.g. [bold]developer[/bold]")

            user = input(":_ ")
            # if user does not provide anything
            if not user:
                console.print(
                    "\n[yellow][!] Please choose the template from given options![/yellow]")
                continue

            for option in templates:
                if user.lower() == option["name"]:
                    return user

            # if user select unkown template
            console.print(
                f"[red]\"{user}\"[/red] [yellow][!] Unkown template![/yellow]")
            continue
    except KeyboardInterrupt:
        pass


def referwith_template_th_path(paths: list[str], message: str):
    try:

        package_paths = []
        package_urls = []
        invalid_inputs = []

        for raw in paths:
            item = Filter.word(raw)
            parsed = urlparse(item)
            if parsed.scheme in ("http", "https"):
                package_urls.append(item)
            elif Validate.path(path=item):
                package_paths.append(item)
            else:
                invalid_inputs.append(item)

        if len(package_paths) < 1 and len(package_urls) < 1:
            console.print(
                f"[yellow] [!] Unable to find packages with such paths.[/yellow]")
            return
        if invalid_inputs:
            console.print(
                f"[yellow][!] Ignoring invalid inputs:[/yellow] {', '.join(invalid_inputs)}")

        template = choose_template()

        # create temp zip folder of target package in ./temphold dir
        console.print(
            f"\n[cyan]Copying all shareable packages and creating single temp .zip folder to share of temp just wait for couple of seconds![/cyan]")

        destination = "./temphold/shareable_packages"

        os.makedirs(destination, exist_ok=True)

        for folder in package_paths:
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
            shareable_folder=".\\temphold\\shareable_packages.zip", message=message, template=f"{template}.html")
        return Server.run()  # run
    except Exception as e:
        console.print(f"[yellow] [!] {e} [/yellow]")
