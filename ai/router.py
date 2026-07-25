from rich.console import Console
from ai.commands import execute_command

console = Console()

def route_command(command):
    console.print(f"[cyan]Received Command:[/cyan] {command}")
    
    if "edge" in command.lower():
        console.print("[green]Routing to Automation Module[/green]")
    elif "remember" in command.lower():
        console.print("[green]Routing to Memory Module[/green]")
    else:
        console.print("[yellow]Routing to AI Brain[/yellow]")
        
    execute_command(command)