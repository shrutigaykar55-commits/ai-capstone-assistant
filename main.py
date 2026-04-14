from auth.face_auth import authenticate_face
from voice.speech_input import get_text_command
from dialog.chatbot import process_dialog
from executor.command_executor import execute_command


def main():
    if not authenticate_face():
        print("Authentication failed")
        return

    print("Assistant Ready")

    running = True

    while running:
        command = get_text_command()

        response = process_dialog(command)
        print("Assistant:", response)

        running = execute_command(command)


if __name__ == "__main__":
    main()
