from rich.console import Console
import yaml

console = Console()


def display_referdb_location():
    with open("./referconfig.yaml", "r") as file:
        config = yaml.safe_load(file.read())

    location = config['referdb_location']
    if location:
        console.print(
            f"[bold]Location:[/bold] [green]{location}[/green]")
        return
    console.print(
        "It looks like you haven't choose refer db to store and do referral of your projects with your friends.")
