# refer

## Share local project folders from your machine

`refer` is a CLI tool that helps you share local folders quickly by generating one-click downloadable links and simple HTML share pages.

## Key Features

- Share one local folder instantly with `refer -path`.
- Share multiple folders with a custom message using `referwith -message ... -paths ...`.
- Share multiple folders with template output using `referwith -template -message ... -paths ...`.
- Simple terminal UX with built-in `about`, `usage`, and `help`.

## Requirements

- Python `3.13+`
- Dependencies from `requirements.txt` (or `pyproject.toml`)

## Installation

### Option 1: pip

```bash
git clone https://github.com/CoderRony955/refer.git
cd refer
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### Option 2: uv

```bash
git clone https://github.com/CoderRony955/refer.git
cd refer
uv venv .venv
.\.venv\Scripts\activate
uv pip install -r requirements.txt
```

## Run

```powershell
python main.py
```

## Commands

### Basic

- `about` - Show project intro and version.
- `usage` - Show full usage docs and quick command reference.
- `contribute` - Open the official GitHub repository.
- `help` / `h` - Show command tables.
- `quit` / `q` / `exit` - Exit the CLI.

### Sharing (local paths)

- `refer -path "<folder_path>"`
- `referwith -message "<message>" -paths "<path1>" "<path2>" ...`
- `referwith -template -message "<message>" -paths "<path1>" "<path2>" ...`

### Examples

```bash
refer -path "C:\Users\You\Projects\my-tool"
referwith -message "Useful utilities" -paths "C:\Tools\a" "C:\Tools\b"
referwith -template -message "My tool bundle" -paths "C:\Tools\a" "C:\Tools\b" "C:\Tools\c"
```

## Where to Start

- Run `about` for a quick overview.
- Run `usage` for detailed docs.
- Run `help` to see categorized command tables.

## Contributing

- Fork the repository.
- Create a branch: `git checkout -b feat/my-change`
- Make your changes and test locally: `python main.py`
- Commit, push, and open a PR.

Use `contribute` inside the CLI to open the repo page.

## License

Distributed under the [MIT License](https://github.com/CoderRony955/refer/blob/main/LICENSE).
