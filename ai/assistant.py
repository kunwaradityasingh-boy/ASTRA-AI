from rich.console import Console
from ai.router import route_command
from ai.brain import start_brain
from time import sleep

console = Console()

class Assistant:
    
    def start(self):
        console.print("[bold green]Starting ASTRA AI...[/bold green]")
        
        modules = [
            "Brain",
            "Memory",
            "Speech",
            "Vision",
            "Automation",
        ]
        
        for module in modules:
            console.print(f"[yellow]Loading {module} Module...[/yellow]")
            sleep(0.5)
            
            if module == "Brain":
                start_brain()
            else:
                console.print(f"[green]{module} Module Loaded Successfully![/green]\n")
        
        console.print("[bold cyan]ASTRA AI is Ready![/bold cyan]")
        
        while True:
            command = input("\nYou:")
            if command.lower() == "exit":
                break
            route_command(command)