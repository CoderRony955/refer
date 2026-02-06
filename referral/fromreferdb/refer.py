from rich.console import Console
from validator import Validate
from filterer import Filter
from server.non_flask_server import Start_server
import json
import yaml

console = Console()


def refer_pkg(name: str):
    try:
        # if config is not found
        if not Validate.path(path="./referconfig.yaml"):
            console.print(
                "[yellow][!] referconfig.yaml not found! Please try to recreate config file with exact required credentials.[/yellow]")
            return

        # read config file to check referdb path
        with open("./referconfig.yaml", "r") as configfile:
            config_data = yaml.safe_load(configfile.read())

        dbpath = config_data["referdb_location"]

        # if dbpath is null
        if dbpath is None:
            console.print("[yellow][!] Unable to find referdb location, it seems like you haven't choose referdb option as a referral & packages path management while setuping refer for the first time.[/yellow]")
            return

        # read packages.json to check if package exist of not with given name
        with open(f"{dbpath}\\packages.json", "r") as datafile:
            pkgs = json.load(datafile)

        for pkg in pkgs:
            if pkg["name"] == Filter.word(name):
                # validate package path
                if Validate.packages(pkgs=[pkg["path"]]):
                    return Start_server.non_flask(pkg_path=pkg["path"])
                
                elif not Validate.packages(pkgs=[pkg["path"]]):
                    console.print(
                        f"[yellow] [!] The path of package[/yellow] '[bold]{pkg["name"]}[/bold]' [yellow]is outdated because it's not valid path. Please check the path and update it![/yellow]\n[bold]Path: [/bold] [yellow]{pkg["path"]}[/yellow]")
                    return

        # if package not found with given specific name
        console.print(
            f"[yellow]with name[/yellow] [bold]{name}[/bold] [yellow]there is not package found![/yellow]")

    except Exception as e:
        console.print(e)
