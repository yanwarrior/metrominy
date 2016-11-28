import string

def tokenizing(doc=''):
    result = doc.lower()
    # hapus tanda baca
    replace_punctuation = string.maketrans(string.punctuation, ' ' * len(string.punctuation))
    result = str(result).translate(replace_punctuation)
    # hapus spasi berlebih
    result = ' '.join(result.split())
    return result
