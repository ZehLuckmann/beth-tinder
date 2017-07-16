def general_treatments(text):
    text = text.lower()
    return text

def remove_punctuation(text):
    punctuation = ['.',',','!','?',';']
    for p in punctuation:
        text = text.replace(p, '')
    return text
