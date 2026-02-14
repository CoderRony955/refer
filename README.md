# refer

## Manage & share projects from your machine

refer is a small CLI tool to manage local project paths and share them instantly with friends by generating one-click downloadable links from your system (no cloud upload required).

Key features
- Manage a local collection of project paths (add / update / list / rename / delete)
- Generate single-package download links or multi-package HTML share pages (with optional templates and messages)
- Keep your data local and secure behind a password stored in `referconfig.yaml`
- Colorful, human-friendly terminal UI
- No cloud upload required

Requirements
- Python 3.13 or newer
- Dependencies listed in `pyproject.toml`
## Installation

### Install via pip

1. Clone the repository:
```bash
git clone https://github.com/CoderRony955/refer.git
cd refer
```

1. Create a virtual environment and install dependencies:
```bash
python -m venv venv
.\.venv\Scripts\Activate.bat
pip install -r requirements.txt
```



### Install via uv

If you have `uv` installed, you can use it as a fast alternative package manager:

1. Clone the repository:
```bash
git clone https://github.com/CoderRony955/refer.git
cd refer
```

2. Create a virtual environment:
```bash
python -m venv venv
.\.venv\Scripts\Activate.bat
```

3. And sync dependencies:

```powershell
uv venv .venv
.\.venv\Scripts\Activate.ps1
uv pip install flask maskpass pyngrok pyyaml rich
```

Run
---
Start the CLI:

```powershell
python main.py
```

On first run `refer` will prompt to create `referconfig.yaml` (set a password and optionally create a local `referdb` folder). After setup you can run any command.

### Config and data
- `referconfig.yaml` — stores your password, optional `referdb` location, and ngrok auth (created on first run)
- If you enable local DB, a `referdb` folder is created and a `packages.json` file is used to store package records.


### Where to start
- Run `usage` inside the app to see full documentation and examples.
- See the full [command reference](COMMANDS.md) for concise examples and flags.
- Run `about` for a quick project description and version.

## Contributing

Thank you for considering contributing! A minimal workflow:

- Fork the repository and create a feature branch: `git checkout -b feat/my-change`
- Make changes and run the CLI locally to verify behavior: `python main.py`
- Commit, push, and open a Pull Request describing your change.

If you plan to add tests or CI, include instructions in your PR. Use the `contribute` command to open the project GitHub page.

## License

refer is distributed under the [MIT License](https://github.com/CoderRony955/refer/blob/main/LICENSE).

