from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table

console = Console()

usage_content = """
# 📚 refer 0.1.0 - Complete Usage Documentation

---

## 🎯 Getting Started

REFER is a CLI tool for managing and sharing your projects securely. All commands follow this pattern:

### For basic & Management commands
```
<command> [options]
```
### For Referral commands
```
refer <command> [options]
```

---

## 📋 Basic Commands

These are utility commands to help you navigate REFER.

| Command | Purpose |
|---------|---------|
| `about` | View REFER version, features & quick info |
| `usage` | Display this documentation |
| `contribute` | Open REFER's GitHub repository |
| `wheredb` | Show the location of your local database |
| `changedb` | Change database location (data stays intact) |

### Examples:

```bash
about
wheredb
changedb
```

---

## 📦 Personal Package Management Commands

Manage your project packages paths securely in the locally based refer database.

### Add a Package Path with their specific name
```bash
addpkg -name 'project-name' -path 'C:\\Users\\YourName\\Projects\\my-project'
```
**Purpose:** Add a new project folder path to your collection  
**Example:**
```bash
addpkg -name 'clitool' -path 'C:\\Users\\John\\Myprojects\\tool'
```

---

### Update a existing Package path
```bash
updatepkg -name 'project-name' -path 'C:\\Users\\YourName\\Projects\\updated-project'
```
**Purpose:** Update an existing package path to new path with specific name  
**Example:**
```bash
updatepkg -name 'clitool_modified' -path 'C:\\Users\\John\\Myprojects\\modified'
```

---

### List All Packages
```bash
listpkgs
```
**Purpose:** View all existing packages in your collection (including name and path)  
**Example:**
```bash
listpkgs
```

---

### Delete or Remove a Package
```bash
delpkg -name 'project-name'
```
**Purpose:** Remove a package from your collection  
**Example:**
```bash
delpkg -name 'clitool'
```

---

### Rename Package name
```bash
renamepkg -name 'current-name' -newname 'new-name'
```
**Purpose:** Rename an existing package  name
**Example:**
```bash
renamepkg -name 'clitool' -newname 'clitool_pro'
```

---

## 🔗 Sharing Commands - From Database

Share projects that are stored in your REFER database. It makes easy referral because of refer local db stores your personal projects paths with their specific names that makes easy for you to directly refer any project just by typing their name.

### Quick Share Single Package
```bash
refer -pkg 'project-name'
```
**Purpose:** Generate an instant one-click download link for a single package  
**Features:**
- Creates a direct download link from your system
- Friends can download instantly
- No cloud upload required

**Example:**
```bash
refer -pkg 'guiapp'
```

---

### Share Multiple Packages with Message
```bash
refer referwith -message 'Your message here' -pkgs 'package1 package2 package3'
```
**Purpose:** Share multiple packages with a custom message in an HTML webpage  
**Features:**
- Creates a structured HTML page
- Includes your custom message
- Multiple download links in organized format

**Example:**
```bash
refer referwith -message 'This is a GUI apps for xyz.' -pkgs 'gui_app1 gui_app2 gui_app3'
```

---

### Share Multiple Packages with Template
```bash
refer referwith -template -message 'Your message here' -pkgs 'package1 package2 package3'
```
**Purpose:** Share packages using professional HTML templates  
**Features:**
- Choose from available templates
- Professional look & feel
- Custom message support
- Multiple downloads in one page

**Example:**
```bash
refer referwith -template -message 'This is the cli tools for xyz.' -pkgs 'cli_app1 cli_app2 cli_app3'
```

---

## 🔗 Sharing Commands - From Local Path

Share projects directly using path. If you don't prefer to use refer local db.

### Quick Share from Path
```bash
refer -path 'C:\\Users\\YourName\\Projects\\my-project'
```
**Purpose:** Generate a download link for any local folder without adding it to database  
**Example:**
```bash
refer -path 'C:\\Users\\John\\Myprojects\\tool'
```

---

### Share Multiple project folders using their Paths with Message
```bash
refer referwith -message 'Your message' -paths 'path1 path2 path3'
```
**Purpose:** Share multiple projects from different locations with a message  
**Example:**
```bash
refer referwith -message 'This is a GUI apps for xyz.' -paths 'C:\\Users\\John\\GUIApps\\gui_app1 C:\\Users\\John\\GUIApps\\gui_app2'
```

---

### Share Multiple project folders using their from Paths with Template
```bash
refer referwith -template -message 'Your message' -paths 'path1 path2 path3'
```
**Purpose:** Share multiple projects with a professional template  
**Example:**
```bash
refer referwith -template -message 'This is the cli tools for xyz.' -paths 'C:\\Users\\John\\CLITools\\cli_tool1 C:\\Users\\John\\CLITools\\cli_tool2'
```

---

## 💡 Command Comparison

### Packages path Management vs Direct Sharing

| Aspect | Database (addpkg) | Direct Share (from path) |
|--------|-------------------|-------------------------|
| **Storage** | Stored in REFER DB just using name | No storage required |
| **Organization** | Organized collection | Ad-hoc sharing |
| **Management** | Can rename, update, delete | Spontaneous |
| **Best For** | Regular projects | Quick one-off shares |

---

## 🎯 Workflow Examples

### Scenario 1: Regular Project Owner
```bash
# Add your personal projects path to database
addpkg -name 'webapp' -path 'C:\\Projects\\webapp'
addpkg -name 'api' -path 'C:\\Projects\\api'

# View your collection
listpkgs

# Share with friends
refer -pkg 'webapp'
refer referwith -message 'Check out my API!' -pkgs 'api'
```

---

### Scenario 2: Sharing Multiple Projects with Template
```bash
# Create a professional sharing page
refer referwith -template -message 'My collection of tools' -pkgs 'tool1 tool2 tool3'

# Share the generated link with your friends
```

---

### Scenario 3: Quick Share from Any Location
```bash
# Share a project directly without adding to database
refer -path 'C:\\Downloads\\RandomProject'

# Share multiple folders with a template
refer referwith -template -paths 'C:\\Folder1 C:\\Folder2'
```

---

## ⚙️ Options & Flags

| Flag | Purpose | Example |
|------|---------|---------|
| `-name` | Specify package name | `addpkg -name 'myapp'` |
| `-path` / `-paths` | Specify folder path(s) | `refer -path 'C:\\\\Projects\\\\app'` |
| `-pkg` / `-pkgs` | Specify package name(s) | `refer -pkg 'myapp'` |
| `-message` | Add custom message | `refer referwith -message 'Check this out!'` |
| `-template` | Use HTML template | `refer referwith -template -pkgs 'app1'` |

---

## 🔐 Best Practices

✅ **DO:**
- Keep package names simple and descriptive
- Use templates for professional sharing
- Organize projects in your database for easy management
- Use `-message` to provide context when sharing

❌ **DON'T:**
- Use special characters in package names
- Share sensitive credentials or private keys
- Store irrelevant files in shared projects
- Forget to use `wheredb` if you lose track of your database

---

## ❓ Need Help?

- Run `about` for quick info
- Run `usage` to see this documentation again
- Check `contribute` to report issues on GitHub
- Use `wheredb` to verify your database location

---

**Happy Sharing! 🚀**

Make project sharing simple, secure, and fun with refer!
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

    # Basic commands
    table.add_row("about", "View version & features")
    table.add_row("usage", "View documentation")
    table.add_row("contribute", "GitHub repository")
    table.add_row("wheredb", "Database location")
    table.add_row("changedb", "Change DB location")

    table.add_row("", "")  # Separator

    # Management commands
    table.add_row("addpkg", "Add package to DB")
    table.add_row("updatepkg", "Update package")
    table.add_row("listpkgs", "List all packages")
    table.add_row("delpkg", "Delete package")
    table.add_row("renamepkg", "Rename package")

    table.add_row("", "")  # Separator

    # Sharing commands
    table.add_row("refer -pkg", "Share single package")
    table.add_row("refer referwith", "Share multiple packages")
    table.add_row("refer -path", "Share from local path")

    console.print(table)
