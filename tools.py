import os
import subprocess
import pyautogui
from langchain_core.tools import tool

@tool
def open_app(app_name: str):
    """Opens a system application. Example: 'notepad', 'calc', 'chrome'."""
    try:
        # Using start command for Windows to decouple the process
        subprocess.Popen(['start', app_name], shell=True)
        return f"Successfully issued command to open {app_name}."
    except Exception as e:
        return f"Failed to open {app_name}: {str(e)}"

@tool
def manage_file(file_path: str, content: str = "", mode: str = "write"):
    """Manages local files. Modes: 'write' (create/overwrite), 'append', 'read'."""
    try:
        if mode == "write":
            with open(file_path, "w") as f:
                f.write(content)
            return f"File '{file_path}' written successfully."
        elif mode == "read":
            with open(file_path, "r") as f:
                return f.read()
        elif mode == "append":
            with open(file_path, "a") as f:
                f.write(content)
            return f"Content appended to '{file_path}'."
    except Exception as e:
        return f"File error: {str(e)}"

@tool
def capture_screen():
    """Takes a screenshot and saves it locally to 'screenshot.png'."""
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        return "Screenshot captured and saved as 'screenshot.png'."
    except Exception as e:
        return f"Vision error: {str(e)}"