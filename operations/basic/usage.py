from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table

console = Console()

usage_content = """
# refer 0.1.0 - Usage Documentation

---

## Getting Started

**refer** is a CLI tool for sharing local project folders using instant downloadable links and simple HTML share pages.

### Command Pattern
```bash
<command> [options]
```

---

## Basic Commands

| Command | Purpose |
|---------|---------|
| `about` | View version, features, and quick info |
| `usage` | Display this documentation |
| `contribute` | Open refer's GitHub repository |
| `help` / `h` | Show startup command tables |
| `quit` / `q` / `exit` | Exit refer |

### Examples

```bash
about
usage
help
quit
```

---

## Sharing Commands (Local Paths)

### Quick Share from Path
```bash
refer -path 'C:\\Users\\YourName\\Projects\\my-project'
```
**Purpose:** Generate a download link for any local folder.

### Share Multiple Folders with Message
```bash
referwith -message 'Your message' -paths "path1" "path2" "path3"
```
**Purpose:** Share multiple projects from different locations with a custom message.

### Share Multiple Folders with Template + Message
```bash
referwith -template -message 'Your message' -paths "path1" "path2" "path3"
```
**Purpose:** Share multiple projects in a template with your custom message.

---

## Options & Flags

| Flag | Purpose | Example |
|------|---------|---------|
| `-path` | Specify one folder path | `refer -path 'C:\\\\Projects\\\\app'` |
| `-paths` | Specify multiple folder paths | `referwith -message 'Check this out!' -paths "path1" "path2"` |
| `-message` | Add custom message for referwith | `referwith -message 'Check this out!' -paths "path1"` |
| `-template` | Use a template for referwith output | `referwith -template -message 'Tools' -paths "path1" "path2"` |

---

## Need Help?

- Run `about` for quick info
- Run `usage` to see this documentation again
- Run `help` to see the command tables
- Run `contribute` to report issues on GitHub
"""


def show_usage():
    """Display comprehensive usage documentation"""
    console.print(Markdown(usage_content))


def show_command_quick_reference():
    """Display a quick reference table of all commands"""
    table = Table(title="refer - Quick Command Reference",
                  show_header=True, header_style="bold magenta")

    table.add_column("Command", style="cyan")
    table.add_column("Purpose", style="green")

    table.add_row("about", "View version & features")
    table.add_row("usage", "View documentation")
    table.add_row("contribute", "GitHub repository")
    table.add_row("help / h", "Show command tables")
    table.add_row("quit / q / exit", "Exit refer")

    table.add_row("", "")

    table.add_row("refer -path", "Share single folder path")
    table.add_row("referwith -message ... -paths ...", "Share multiple folders with message")
    table.add_row("referwith -template -message ... -paths ...", "Share multiple folders with template")

    console.print(table)
