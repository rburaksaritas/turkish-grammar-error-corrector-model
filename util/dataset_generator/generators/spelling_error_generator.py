import pandas as pd
import random
import string

def change_case(sentence):
    char_index = random.randint(0, len(sentence) - 1)
    sentence_list = list(sentence)
    sentence_list[char_index] = sentence_list[char_index].swapcase()
    return ''.join(sentence_list)

def change_case_upper_to_lower(sentence):
    uppercase_indices = [i for i, char in enumerate(sentence) if char.isupper()]
    if not uppercase_indices:
        return sentence
    char_index = random.choice(uppercase_indices)
    sentence_list = list(sentence)
    sentence_list[char_index] = sentence_list[char_index].lower()
    return ''.join(sentence_list)

def add_letter(sentence):
    char_index = random.randint(0, len(sentence) - 1)
    random_letter = random.choice(string.ascii_letters)
    return sentence[:char_index] + random_letter + sentence[char_index:]

def remove_letter(sentence):
    if len(sentence) > 1:
        char_index = random.randint(0, len(sentence) - 1)
        return sentence[:char_index] + sentence[char_index+1:]
    return sentence

def swap_adjacent_letters(sentence):
    if len(sentence) > 1:
        char_index = random.randint(0, len(sentence) - 2)
        return (sentence[:char_index] + sentence[char_index+1] + sentence[char_index] +
                sentence[char_index+2:])
    return sentence

def substitute_letter(sentence):
    if len(sentence) > 0:
        char_index = random.randint(0, len(sentence) - 1)
        substitute_letter = random.choice(string.ascii_letters)
        return sentence[:char_index] + substitute_letter + sentence[char_index+1:]
    return sentence

def introduce_errors(sentence, error_rate=0.1):
    error_functions = [change_case, change_case_upper_to_lower, add_letter, remove_letter, swap_adjacent_letters, substitute_letter]
    new_sentence = sentence
    for error_function in error_functions:
        if random.random() < error_rate:
            new_sentence = error_function(new_sentence)
    return new_sentence

# Load the dataset
df = pd.read_csv('dataset/correct.csv')

df_errors = pd.DataFrame({
    'source': df['target'].apply(lambda x: introduce_errors(x, error_rate=0.2)), 
    'target': df['target'] 
})

df_errors.to_csv('dataset/spelling_errors.csv', index=False)

print("Dataset saved as 'spelling_errors.csv' with 'source' as the errored sentence and 'target' as the fixed one.")
