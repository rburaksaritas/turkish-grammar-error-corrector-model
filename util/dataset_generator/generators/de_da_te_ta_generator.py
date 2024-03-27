import re
import random

def find_suffix_indices(sentence):
    # Find indices of "de/da/te/ta" suffices along with their preceding prefix
    matches = re.finditer(r'(\S+?)(\s*)(de|da|te|ta)(?=\s|$)', sentence)
    suffix_indices = [(match.start(3), match.end(3)) for match in matches]
    return suffix_indices, sentence

def transform_sentence(sentence, suffix_indices):
    transformed_sentence = sentence
    for start, end in reversed(suffix_indices):
        suffix = transformed_sentence[start:end]
        print("start", "-" + transformed_sentence[:start-1] + "-", "suffix:", "-" + suffix + "-", "end:", "-" + transformed_sentence[end:] + "-")
        if transformed_sentence[start - 1] == ' ':
            # If "{prefix}{whitespace}{suffix}" format, convert to "{prefix}{suffix}"
            transformed_sentence = transformed_sentence[:start-1] + suffix + transformed_sentence[end:]
        else:
            # If "{prefix}{suffix}" format, convert to "{prefix}{whitespace}{suffix}"
            transformed_sentence = transformed_sentence[:start] + ' ' + suffix + transformed_sentence[end:]
    return transformed_sentence

def process_sentences(sentences):
    processed_sentences = []
    for sentence in sentences:
        suffix_indices, sentence = find_suffix_indices(sentence)
        if suffix_indices:
            sentence = transform_sentence(sentence, suffix_indices)
        processed_sentences.append(sentence)
    return processed_sentences
