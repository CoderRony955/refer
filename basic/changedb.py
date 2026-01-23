from rich.console import Console
import yaml
import shutil

console = Console()


def change_refer_db(path_of_new_location: str):
    """change existing referdb folder location to another location (without lossing data)
    """
    try:
        with open("./referconfig.yaml", "r") as file:
            config = yaml.safe_load(file.read())

        old_location = config['referdb_location']

        # if user has referdb folder
        if old_location:
            shutil.move(f"{old_location}", path_of_new_location)
            console.print(
                f"[bold]referdb shifted to new location![/bold]\nNew location: [green]{path_of_new_location}[/green]")

            config['referdb_location'] = path_of_new_location
            with open("./referconfig.yaml", 'w') as file:
                yaml.safe_dump(config, file, default_flow_style=False)

            return

        # if user doesn't referdb folder
        console.print(
            "[yellow]You haven't any specific referdb folder![/yellow]")
    except Exception:
        pass
