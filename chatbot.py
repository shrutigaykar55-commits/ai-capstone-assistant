def process_dialog(command):
    rules = {
        "hello": "Hello! How can I help?",
        "time": "I can help you check time.",
        "open browser": "Opening browser now.",
        "exit": "Goodbye!"
    }

    for key in rules:
        if key in command:
            return rules[key]

    return "Command not recognized."
