import string

def sciencify(text):
    """Uppercase every letter and add a dot after every letter"""
    scienced_text = ''
    for c in text.lower():
        if c in string.lowercase:
            scienced_text += c.upper() + '.'
        else:
            scienced_text += c
    return scienced_text
