import pandas as pd
import csv
import os

def clean_newlines(sentence):
    return sentence.replace('\n', '').replace('\r', '')


def create_csv_from_list(source_sentences, target_sentences, file_name):
    source_sentences = [clean_newlines(sentence) for sentence in source_sentences]
    target_sentences = [clean_newlines(sentence) for sentence in target_sentences]
    
    df = pd.DataFrame({
        'source': source_sentences,
        'target': target_sentences
    })
    df.to_csv(file_name, index=False, quoting=csv.QUOTE_MINIMAL)
    print(f"CSV created from list at: {file_name}")


def create_csv_from_df(df, file_name):
    df.to_csv(file_name, index=False, quoting=csv.QUOTE_MINIMAL)
    print(f"CSV created from DataFrame at: {file_name}")


def append_to_csv_from_list(source_sentences, target_sentences, file_name):
    source_sentences = [clean_newlines(sentence) for sentence in source_sentences]
    target_sentences = [clean_newlines(sentence) for sentence in target_sentences]
    
    new_data = pd.DataFrame({
        'source': source_sentences,
        'target': target_sentences
    })
    
    if os.path.exists(file_name):
        existing_data = pd.read_csv(file_name)
        updated_data = pd.concat([existing_data, new_data], ignore_index=True)
        print(f"Data appended to existing CSV from list at: {file_name}")
    else:
        updated_data = new_data
        print(f"CSV created and data added from list at: {file_name}")
    
    updated_data.to_csv(file_name, index=False, quoting=csv.QUOTE_MINIMAL)


def append_to_csv_from_df(df, file_name):
    if os.path.exists(file_name):
        existing_data = pd.read_csv(file_name)
        updated_data = pd.concat([existing_data, df], ignore_index=True)
        print(f"Data appended to existing CSV from DataFrame at: {file_name}")
    else:
        updated_data = df
        print(f"CSV created and data added from DataFrame at: {file_name}")
    
    updated_data.to_csv(file_name, index=False, quoting=csv.QUOTE_MINIMAL)


def read_csv_as_df(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Reading the entire CSV as DataFrame from: {file_path}")
        print(df)
        return df
    except Exception as e:
        print(f"CSV read error: {e}")
        return None


def read_csv_as_list(file_path):
    try:
        df = pd.read_csv(file_path)
        data_list = [df[col].tolist() for col in df.columns]
        print(f"Reading the entire CSV as list of columns from: {file_path}")
        print(data_list)
        return data_list
    except Exception as e:
        print(f"CSV read error: {e}")
        return None


def read_csv_columns_as_df(file_path, columns):
    try:
        df = pd.read_csv(file_path, usecols=columns)
        print(f"Reading specified columns as DataFrame from: {file_path}")
        print(f"Columns: {columns}")
        print(df)
        return df
    except Exception as e:
        print(f"CSV read error: {e}")
        return None


def read_csv_columns_as_list(file_path, columns):
    try:
        df = pd.read_csv(file_path, usecols=columns)
        data_list = [df[col].tolist() for col in df.columns]
        print(f"Reading specified columns as list of columns from: {file_path}")
        print(f"Columns: {columns}")
        print(data_list)
        return data_list
    except Exception as e:
        print(f"CSV read error: {e}")
        return None

