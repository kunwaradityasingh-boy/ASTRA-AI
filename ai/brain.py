from rich.console import Console
from rich.panel import Panel
from dotenv import load_dotenv
from google import genai
import os
from speech.speaker import speak
from rich.live import Live
from rich.text import Text
from rich.spinner import Spinner
from time import sleep
from memory.context import add_message, get_context
from memory.long_term import remember, recall

load_dotenv()

console = Console()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def start_brain():
    console.print(
        Panel.fit(
            "🧠 Brain Module Loaded Successfully",
            title = "ASTRA AI Brain",
            border_style = "cyan",
        )
    )
    
def ask_brain(prompt: str):
    try:
        prompt_lower = prompt.lower()
        print("DEBUG 1:", prompt_lower)
        
        if "my name is" in prompt_lower:
            name = prompt.split("is",1)[1].strip()
            remember("name", name)
            print("DEBUG Saved:",recall("name"))
            return f"Okay! I'll remember your name is {name}."
        
        if "what is my name" in prompt_lower or "who am i" in prompt_lower:
            print("DEBUG Recall:",recall("name"))
            name = recall("name")
            if name:
                return f"Your name is {name}."
            return "I don't know your name yet."
        
        spinner = Spinner(
            "dots",
            text="[cyan]🧠ASTRA is Thinking...[/cyan]"
        )
        with Live(spinner, console=console, refresh_per_second=12):
            response = client.models.generate_content_stream(
                model="models/gemini-3.5-flash",
                contents=prompt,
            )
        
        text = Text()
        
        with Live(text, console=console, refresh_per_second=20):
            for chunk in response:
                if chunk.text:
                    for ch in chunk.text:
                        text.append(ch)
                        sleep(0.008)
        
        final_text = text.plain
        
        console.print(
            Panel(
                final_text,
                title="🤖 ASTRA AI",
                border_style="green"
            )
        )
        
        console.print("[green]✅Response completed[/green]")
        
        speak(final_text)
        
        return final_text
    except Exception as e:
        console.print(
            Panel(
                f"Brain Error: {e}",
                title="⚠️ ASTRA AI Error",
                border_style="red"
            )
        )
        return f"Brain Error: {e}"