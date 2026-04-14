import customtkinter as ctk
import webbrowser
import cv2
import threading
import requests
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class SplashScreen(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Welcome")
        self.geometry("520x320")
        self.resizable(False, False)
        ctk.CTkLabel(self, text="AI Capstone Assistant", font=("Arial", 30, "bold")).pack(pady=60)
        ctk.CTkLabel(self, text="Developed by Shrut | Secure Login", font=("Arial", 16)).pack(pady=10)
        self.loader = ctk.CTkProgressBar(self, width=300)
        self.loader.pack(pady=20)
        self.loader.start()
        self.after(2000, self.launch_main)

    def launch_main(self):
        self.destroy()
        AIAssistantApp().mainloop()


class AIAssistantApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("AI Capstone Assistant")
        self.geometry("1000x620")
        self.resizable(False, False)
        self.build_ui()

    def build_ui(self):
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")

        ctk.CTkLabel(self.sidebar, text="🤖 AI PANEL", font=("Arial", 24, "bold")).pack(pady=30)
        ctk.CTkButton(self.sidebar, text="🏠 Home", width=180).pack(pady=10)
        ctk.CTkButton(self.sidebar, text="🌐 Browser", width=180, command=lambda: webbrowser.open("https://google.com")).pack(pady=10)
        ctk.CTkButton(self.sidebar, text="▶ YouTube", width=180, command=lambda: webbrowser.open("https://youtube.com")).pack(pady=10)
        ctk.CTkButton(self.sidebar, text="🧹 Clear", width=180, command=self.clear_output).pack(pady=10)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(self.main_frame, text="AI Capstone Dashboard", font=("Arial", 28, "bold")).pack(pady=20)

        self.status = ctk.CTkLabel(self.main_frame, text="● Online", font=("Arial", 16))
        self.status.pack(pady=5)

        self.status_bar = ctk.CTkProgressBar(self.main_frame, width=500)
        self.status_bar.pack(pady=10)
        self.status_bar.set(1)

        self.command_entry = ctk.CTkEntry(self.main_frame, width=550, height=42, placeholder_text="Ask anything...")
        self.command_entry.pack(pady=15)

        ctk.CTkButton(self.main_frame, text="Send", command=self.run_command, width=140).pack(pady=10)

        self.output_box = ctk.CTkTextbox(self.main_frame, width=650, height=320, font=("Consolas", 14))
        self.output_box.pack(pady=20)
        self.output_box.insert("end", "Assistant ready...\n")

    def log(self, text):
        self.output_box.insert("end", text + "\n")
        self.output_box.see("end")

    def clear_output(self):
        self.output_box.delete("1.0", "end")

    def smart_reply(self, command):
        command = command.lower()
        if "hello" in command or "hi" in command:
            return "Hello! How can I help you today?"
        if "time" in command:
            return f"Current time is {datetime.now().strftime('%H:%M:%S')}"
        if "date" in command:
            return f"Today's date is {datetime.now().strftime('%d-%m-%Y')}"
        if "python" in command:
            return "Python is a high-level programming language used for AI, web, and automation."
        if "ai" in command:
            return "Artificial Intelligence enables machines to simulate human intelligence."
        return f"I understood your question: '{command}'. This looks like a general query."

    def run_command(self):
        command = self.command_entry.get().strip()
        if not command:
            return
        self.log(f"You: {command}")
        if "open browser" in command.lower():
            webbrowser.open("https://google.com")
        elif "open youtube" in command.lower():
            webbrowser.open("https://youtube.com")
        reply = self.smart_reply(command)
        self.log(f"Assistant: {reply}")
        self.command_entry.delete(0, "end")


def authenticate_face():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(0)
    authenticated = False
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            authenticated = True
        cv2.imshow("Face Authentication", frame)
        if authenticated:
            break
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
    return authenticated


if __name__ == "__main__":
    if authenticate_face():
        SplashScreen().mainloop()
    else:
        print("Authentication failed")
