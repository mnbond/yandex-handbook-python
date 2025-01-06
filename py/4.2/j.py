def secret_replace(text, **replaces):
    encoded_text = ""
    for ind, char in enumerate(text):
        replace = replaces.get(char, (char, ))
        encoded_text += replace[text[:ind].count(char) % len(replace)]
    return encoded_text
