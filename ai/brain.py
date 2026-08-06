from rich.console import Console
from rich.panel import Panel
from dotenv import load_dotenv
from google import genai
import os
from speech.speaker import speak

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
        response = client.models.generate_content(
            model="models/gemini-3.5-flash",
            contents=prompt,
        )
        
        text = response.text or "No response received."
        
        console.print(
            Panel.fit(
                text,
                title="🤖 ASTRA AI",
                border_style="green"
            )
        )
        speak(text)
        return text
    except Exception as e:
        console.print(
            Panel(
                f"Brain Error: {e}",
                title="⚠️ ASTRA AI Error",
                border_style="red"
            )
        )
        return f"Brain Error: {e}"