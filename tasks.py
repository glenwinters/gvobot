from microsoftbotframework import ReplyToActivity
from utils import sciencify

def message_handler(activity):
    if activity['type'] == 'message':
        message = activity['text']

        # Strip mention if it's at the beginning
        if len(message) >= 7 and message[:7] == '@gvobot':
            message = message[7:]

        # Be snarky when no message is sent; otherwise, S.C.I.E.N.C.E.
        if len(message) == 0:
            response = 'Has anyone really been far even as decided to use ' +
                'even go want to do look more like?'
        else:
            response = sciencify(message)
        ReplyToActivity(fill=activity, text=response).send()
