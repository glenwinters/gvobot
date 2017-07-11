from microsoftbotframework import ReplyToActivity

def science(message):
    print(message)
    if message['type'] == 'message':
        text = message['text']
        scienced_text = ''.join([c.upper() + '.' for c in text])
        ReplyToActivity(fill=message, text=scienced_text).send()
