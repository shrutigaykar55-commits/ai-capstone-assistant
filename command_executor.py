import os
import webbrowser
from datetime import datetime

def execute_command(command):
    if "open browser" in command:
        webbrowser.open("https://google.com")

    elif "time" in command:
        print(datetime.now())

    elif "open notepad" in command:
        os.system("notepad")

    elif "exit" in command:
        return False

    return True
