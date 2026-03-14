def display_messages (*message):
    message = list(message)
    for messages in message:
        print(messages.upper())
    return


result = display_messages("Hola", "Que haces", "Como estas", "Que dia es", "Tomas mate?")


