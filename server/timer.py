from rich.console import Console
from rich.live import Live
from rich.text import Text
import time

console = Console()

def timer(seconds: int):
    with Live(console=console, refresh_per_second=10) as live:
        for i in range(seconds, -1, -1):
            live.update(Text(f"Please wait for {i} seconds...", style="cyan"))
            time.sleep(1)
