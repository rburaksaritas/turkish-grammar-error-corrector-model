import nltk
from nltk.tokenize import sent_tokenize

# Ensure you have the 'punkt' tokenizer models downloaded
nltk.download('punkt')

def separate_sentences(text):
    # Use NLTK's sent_tokenize to separate sentences
    sentences = sent_tokenize(text)
    return sentences
