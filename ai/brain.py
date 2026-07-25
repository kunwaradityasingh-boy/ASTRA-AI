from rich.console import Console
from rich.panel import Panel

console = Console()

def start_brain():
    console.print(
        Panel.fit(
            "🧠 Brain Module Loaded Successfully",
            title = "ASTRA AI Brain",
            border_style = "cyan",
        )
    )