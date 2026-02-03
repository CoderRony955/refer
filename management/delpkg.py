from rich.console import Console
from validator import Validate
from filterer import Filter
import json
import yaml

console = Console()


def delpkg(name: str):
    """delete existing package path in referdb
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
            if entry["name"] == Filter.word(name):
                data.remove(entry)  # delete path

                # write to packages.json file
                with open(f"{dbpath}\\packages.json", "w") as file:
                    json.dump(data, file, indent=4)

                console.print(
                    f"[bold]Deletion Path for Package [bold]{name}[/bold]\n")
                return

        # if package not found with given specific name
        console.print(
            f"[yellow]with name[/yellow] [bold]{name}[/bold] [yellow]there is not package found![/yellow]")
    except Exception as e:
        console.print(e)
