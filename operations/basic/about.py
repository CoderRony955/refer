from rich.console import Console
from rich.markdown import Markdown

console = Console()

about_content = """
# refer - Project Sharing from Local Paths

## What is refer?

**refer** is a CLI tool that helps you share local project folders quickly.
It creates one-click downloadable links and simple share pages directly from paths on your system.

---

## Key Features

### Fast Sharing
- Generate a direct download link from a local folder path
- Share multiple folders in one go with a custom message
- Use a template output for cleaner presentation

### Local and Simple
- Works directly with your local paths
- No package database setup required
- Minimal command flow for day-to-day sharing

### Developer Friendly
- Clear command structure
- Rich terminal output
- Built-in usage documentation

---

**Version:** 0.2.0
"""


def show_about():
    console.print(Markdown(about_content))
