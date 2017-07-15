from microsoftbotframework import ReplyToActivity
from utils import sciencify, unescape

FIXED_RESPONSES = {
    'what is this?':
        'THIS IS GRINDIE VOLUME ONE',
    'should i mess around?':
        'DON\'T MESS AROUND',
    '!yakisoba':
        'https://www.youtube.com/watch?v=sLGTc3x7-38'
}

def activity_handler(activity):
    if activity['type'] == 'message':
        message = activity['text']
        response = _message_handler(message)
        ReplyToActivity(fill=activity, text=response).send()

def _message_handler(message):
        mention = '@gvobot'
        print(message)
        # Strip mention if it's at the beginning
        if message == mention:
            message = ''
        elif message.startswith(mention):
            # Remove the extra space added after the mention, too
            message = message[len(mention) + 1:]

        # Unescape message (skype encodes &, <, >, ', and ")
        message = unescape(message)

        # Be snarky when no message is sent; otherwise, S.C.I.E.N.C.E.
        if len(message) == 0:
            response = 'Has anyone really been far even as decided to use ' \
                'even go want to do look more like?'
        elif FIXED_RESPONSES.get(message.lower(), None) is not None:
            response = FIXED_RESPONSES[message.lower()]
        else:
            response = sciencify(message)

            # The bot's name is unscienceable.
            response = response.replace('@G.V.O.B.O.T.', '@gvobot')

        return response
