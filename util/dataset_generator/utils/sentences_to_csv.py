import pandas as pd
import csv
import os

def clean_newlines(sentence):
    # Replace new line characters within the sentence with a space
    return sentence.replace('\n', '').replace('\r', '')

def create_csv(source_sentences, target_sentences, file_name):
    # Clean newlines from sentences
    source_sentences = [clean_newlines(sentence) for sentence in source_sentences]
    target_sentences = [clean_newlines(sentence) for sentence in target_sentences]
    
    df = pd.DataFrame({
        'source': source_sentences,
        'target': target_sentences
    })
    # Save dataframe to CSV
    df.to_csv(file_name, index=False, quoting=csv.QUOTE_MINIMAL)

def append_to_csv(source_sentences, target_sentences, file_name):
    # Clean newlines from sentences
    source_sentences = [clean_newlines(sentence) for sentence in source_sentences]
    target_sentences = [clean_newlines(sentence) for sentence in target_sentences]
    
    new_data = pd.DataFrame({
        'source': source_sentences,
        'target': target_sentences
    })
    
    # Check if the CSV file exists
    if os.path.exists(file_name):
        # If it does, read the existing data and append the new data
        existing_data = pd.read_csv(file_name)
        updated_data = pd.concat([existing_data, new_data], ignore_index=True)
    else:
        # If not, just use the new data
        updated_data = new_data
    
    # Save updated data to CSV
    updated_data.to_csv(file_name, index=False, quoting=csv.QUOTE_MINIMAL)
