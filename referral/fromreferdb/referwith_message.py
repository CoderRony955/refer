from rich.console import Console
from validator import Validate
from filterer import Filter
from server.flask_server import Start_server
import shutil
import json
import yaml
import os

console = Console()


def referwith_message(pkgs: list[str], message: str):
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
            all_packages = json.load(datafile)

        packages_paths = []  # to store all packages paths that are valid and found

        final_pkgs = []
        for item in pkgs:
            final_pkgs.extend(item.split())

        final_pkgs = [Filter.word(p) for p in final_pkgs]

        for pkg in all_packages:
            if Filter.word(pkg["name"]).lower() in [p.lower() for p in final_pkgs]:
                # validate package path
                pkg_path = Filter.word(pkg["path"])
                if Validate.packages(pkgs=[pkg_path]):
                    packages_paths.append(pkg_path)

        if len(packages_paths) < 1:
            console.print(
                f"[yellow] [!] Unable to find packages with such names.[/yellow]")
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

        # remove sharelable_packages tree after converting it to arhive
        shutil.rmtree("./temphold/shareable_packages")

        # start process to start server
        Server = Start_server(
            shareable_folder=".\\temphold\\shareable_packages.zip", message=message)
        return Server.run()  # run
    except Exception as e:
        console.print(f"[yellow] [!] {e} [/yellow]")
