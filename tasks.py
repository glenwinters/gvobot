from microsoftbotframework import ReplyToActivity
from utils import sciencify

def message_handler(activity):
    if activity['type'] == 'message':
        message = activity['text']
        ReplyToActivity(fill=activity, text=sciencify(message)).send()
