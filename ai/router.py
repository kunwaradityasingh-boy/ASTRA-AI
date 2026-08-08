from rich.console import Console
from ai.commands import execute_command
from ai.nlu import detect_intent
from ai.brain import ask_brain
from speech.speaker import speak

console = Console()

def route_command(command):
    console.print(f"[cyan]Received Command:[/cyan] {command}")
    
    intent = detect_intent(command)
    
    if intent == "OPEN_CHROME":
        execute_command("open chrome")
        return True
    elif intent == "OPEN_NOTEPAD":
        execute_command("open notepad")
        return True
    elif intent == "OPEN_VSCODE":
        execute_command("open vscode")
        return True
    elif intent == "OPEN_GITHUB":
        execute_command("open github")
        return True
    elif intent == "OPEN_YOUTUBE":
        execute_command("open youtube")
        return True
    elif intent == "OPEN_GOOGLE":
        execute_command("open google")
        return True
    elif intent == "OPEN_WHATSAPP":
        execute_command("open whatsapp")
        return True
    elif intent == "EXIT":
        console.print("[red]Goodbye! ASTRA AI Stopped.[/red]")
        raise SystemExit
    elif command.lower().startswith("open "):
        execute_command(command)
        return True
    
    if "edge" in command.lower():
        console.print("[green]Routing to Automation Module[/green]")
    elif "remember" in command.lower():
        console.print("[green]Routing to Memory Module[/green]")
    else:
        console.print("[yellow]Routing to AI Brain[/yellow]")
        response = ask_brain(command)
        if response:
            console.print(response)
            speak(response)
        return response
    