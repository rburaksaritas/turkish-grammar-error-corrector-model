import re
import random
import re

def find_question_suffix_indices(sentence):
    question_suffix_regex = r'(\S+?)(\s*)((mı|mi|mu|mü)(sın|sin|sun|sün|sa|se|lar|ler|nız|niz|yız|yiz|dir|dır|dur|dür|mış|mıs|müş|müs|dı|di|du|dü|yor)?)(?=\s|[.,?!;:]|$)'
    matches = re.finditer(question_suffix_regex, sentence, re.IGNORECASE)
    suffix_indices = [(match.start(3), match.end(3)) for match in matches]
    print(sentence, suffix_indices)
    for indices in suffix_indices:
        print(sentence[indices[0]:indices[1]])
    return suffix_indices, sentence

def transform_suffix(sentence, start, end):
    suffix = sentence[start:end]
    if sentence[start - 1] == ' ':
        # If "{prefix}{whitespace}{suffix}" format, convert to "{prefix}{suffix}"
        sentence = sentence[:start-1] + suffix + sentence[end:]
    else:
        # If "{prefix}{suffix}" format, convert to "{prefix}{whitespace}{suffix}"
        sentence = sentence[:start] + ' ' + suffix + sentence[end:] 
    return sentence

def transform_sentence(sentence, suffix_indices):
    transformed_sentence = sentence
    for start, end in reversed(suffix_indices):
        # Randomly choose whether to transform the suffix. 
        # Uncomment below if you want untransformed examples as well.
        # if (random.choice([True, True, False])):
            transformed_sentence = transform_suffix(transformed_sentence, start, end)
    return transformed_sentence

def process_sentences(sentences):
    processed_sentences = []
    for sentence in sentences:
        suffix_indices, sentence = find_question_suffix_indices(sentence)
        if suffix_indices:
            sentence = transform_sentence(sentence, suffix_indices)
        processed_sentences.append(sentence)
    return processed_sentences

