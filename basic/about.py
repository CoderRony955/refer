from rich.console import Console
from rich.markdown import Markdown

console = Console()

about_content = """
# 🚀 **refer** - Project Sharing Made Simple & Secure

## What is refer?

**refer** is a powerful CLI tool that revolutionizes how you share and manage your projects with friends. 
Instead of complex file transfers or cloud uploads, refer generates instant, one-click downloadable links 
directly from your system—making project sharing as easy as a single command.

---

## ✨ Key Features

### 📦 **Smart Package paths Management**
- Add, update, list, rename, and delete your personal project packages paths effortlessly
- Organize all your personal projects in one secure local database
- Change database location anytime without losing any data

### 🔗 **Instant Sharing**
- Generate secure, one-click download links for your personal projects
- Share packages directly from your system to friends
- No cloud uploads, no complicated steps—just pure simplicity

### 🔐 **Secure & Private**
- Keep your personal projects on your local system
- Control who gets access to what
- No third-party servers storing your data

### 🎯 **Developer Friendly**
- Simple command-line interface
- Rich, colorful terminal output
- Built-in documentation and examples

---

## 💡 Perfect For

- **Developers** sharing code samples and projects
- **Teams** distributing project templates
- **Content Creators** sharing digital work
- **Educators** distributing learning materials
- **Anyone** who values simplicity & security

---

**refer** — Because sharing your work should be as easy as a single command! 🎉

**Version:** 0.1.0
"""


def show_about():
    console.print(Markdown(about_content))
