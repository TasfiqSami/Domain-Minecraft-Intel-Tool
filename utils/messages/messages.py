import json

def get_message(message):
    with open('utils/messages/messages_en.json') as f:
        f.read()
        return json.load(f)[message]