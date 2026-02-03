from rich.console import Console
from validator import Validate
from filterer import Filter
import json
import yaml

console = Console()


def renamepkg(old_name: str, new_name: str):
    """Rename existing package name in referdb
    """
    try:
        if not Validate.path(path="./referconfig.yaml"):
            console.print(
                "[yellow][!] referconfig.yaml not found! Please try to recreate config file with exact required credentials.[/yellow]")
            return

        # read config file
        with open("./referconfig.yaml", "r") as configfile:
            config_data = yaml.safe_load(configfile.read())

        # access referdb path
        dbpath = config_data['referdb_location']

        # check if packages.json file exists or not in referdb dir
        if not Validate.path(path=f"{dbpath}\\packages.json"):
            console.print("[yellow][!] packages.json file not found! It seems like packages.json is deleted or moved to another location. Please check the refer codebase folder and try to recreate manually. (All data in packages.json has been lost)[/yellow]")
            return

        # if dbpath is null
        if dbpath is None:
            console.print("[yellow][!] Unable to find referdb location, it seems like you haven't choose referdb option as a referral & packages path management while setuping refer for the first time.[/yellow]")
            return

        # if dbpath location is not accurate (or maybe someone changed it)
        if not Validate.path(path=dbpath):
            console.print(
                f"[bold]{dbpath}[/bold] [yellow][!] Location not found! Please check the accurate path of referdb if it's exist.[/yellow]")
            return

        # read packages.json
        with open(f"{dbpath}\\packages.json", "r") as jsonfile:
            data = json.load(jsonfile)

        for entry in data:
            if entry["name"] == Filter.word(old_name):
                entry["name"] = Filter.word(new_name)
                # write to packages.json file
                with open(f"{dbpath}\\packages.json", "w") as file:
                    json.dump(data, file, indent=4)

                console.print(
                    f"[bold]Change package name for [bold]{old_name}[/bold] from:\n[bold]Old Name:[/bold] [yellow]{old_name}[/yellow]\n[bold]New Name:[/bold] [green]{new_name}[/green]")
                return

        # if package not found with given specific name
        console.print(
            f"[yellow]with name[/yellow] [bold]{old_name}[/bold] [yellow]there is not package found![/yellow]")
    except Exception as e:
        console.print(e)
