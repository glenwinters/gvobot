import random
from microsoftbotframework import ReplyToActivity

from music import get_random_song
from utils import sciencify, unescape
from food2fork import get_random_recipe

FIXED_RESPONSES = {
    'what is this?':
        'THIS IS GRINDIE VOLUME ONE',
    'should i mess around?':
        'DON\'T MESS AROUND',
    '!yakisoba':
        'https://www.youtube.com/watch?v=sLGTc3x7-38',
    '!pacefog':
        'https://www.youtube.com/watch?v=TDkhl-CgETg',
    '!bigwheel':
        'https://www.youtube.com/watch?v=0TrishCMmpc'
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
        elif message.startswith('!number'):
            usage = 'Usage: !number [<start num> <end num>]'
            args = message.split()
            if len(args) == 1:
                response = str(random.randint(1, 6))
            elif len(args) == 3:
                try:
                    start = int(args[1])
                    end = int(args[2])
                    response = str(random.randint(start, end))
                except ValueError:
                    response = usage
            else:
                response = usage
        elif message.startswith('!song'):
            args = message.split()
            if len(args) == 1:
                song = get_random_song()
                response = song.to_message()
            else:
                response = 'Usage: !song'
        elif message.startswith('!recipe'):
            usage = 'Usage: !recipe'
            args = message.split()
            if len(args) == 1:
                response = get_random_recipe()
            else:
                response = usage
        else:
            response = sciencify(message)

            # Allow bot to do actions with /me
            if response.startswith('/M.E. '):
                response = response.replace('/M.E.', '/me', 1)

            # The bot's name is unscienceable.
            response = response.replace('@G.V.O.B.O.T.', '@gvobot')

        print(response)
        return response
