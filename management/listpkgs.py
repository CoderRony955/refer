from rich.console import Console
from rich.table import Table
from validator import Validate
import json
import yaml

console = Console()


def listpkgs():
    """List all packages with their names + paths
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

        # table to display all records
        table = Table(title="All Packages")
        table.add_column("Name")
        table.add_column("Path")

        for record in data:
            table.add_row(record.get('name'),
                          f"[cyan]{record.get('path')}[/cyan]")
        console.print(table)

    except Exception as e:
        console.print(e)
