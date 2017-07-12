from microsoftbotframework import ReplyToActivity
from utils import sciencify

def message_handler(activity):
    if activity['type'] == 'message':
        message = message['text']
        ReplyToActivity(fill=message, text=sciencify(message)).send()
