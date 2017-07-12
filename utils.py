import string

def sciencify(text):
    """Science that text!

    - Uppercase every letter
    - Add a period after every letter
    - Remove periods in the message if they follow a scienced letter
    """
    scienced_text = ''
    text_lowercase = text.lower()
    for i, c in enumerate(text_lowercase):
        if c in string.ascii_lowercase:
            scienced_text += c.upper() + '.'
        elif c == '.':
            # Don't keep the period if the previous character was a letter
            if i == 0 or text_lowercase[i - 1] not in string.ascii_lowercase:
                scienced_text += c
        else:
            scienced_text += c
    return scienced_text
