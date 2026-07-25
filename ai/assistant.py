from rich.console import Console
from ai.router import route_command
from ai.brain import start_brain
from time import sleep
from speech.listener import listen
from ai.nlu import detect_intent

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
            command = listen()
            if not command:
                continue
            intent = detect_intent(command)
            
            route_command(command)