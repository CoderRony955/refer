from rich.console import Console
import yaml
import shutil
import os

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
            # if referdb folder path found wrong or modified
            if not str(old_location).endswith("referdb"):
                console.print("[yellow]It looks like referdb folder path isn't correct in config file. It's modifyed, please check the config file and paste the exact path of referdb folder to makes easy to perform operations.[/yellow]")
                return

            if os.path.exists(path_of_new_location):
                shutil.move(f"{old_location}", path_of_new_location)
                console.print(
                    f"[bold]referdb shifted to new location![/bold]\nNew location: [green]{path_of_new_location}[/green]")

                config['referdb_location'] = f"{path_of_new_location}\\referdb"
                with open("./referconfig.yaml", 'w') as file:
                    yaml.safe_dump(config, file, default_flow_style=False)
                return

            # if user given path for new location does not exist
            console.print(
                f"[bold]{path_of_new_location}[/bold] [yellow][!] does not exist![/yellow]")
            return

        # if user doesn't have referdb folder
        console.print(
            "[yellow]You haven't any specific referdb folder![/yellow]")

    except Exception as e:
        console.print(e)
