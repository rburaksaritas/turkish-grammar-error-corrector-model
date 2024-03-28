import pandas as pd

def shuffle_data(input_file_path, output_file_path):
    df = pd.read_csv(input_file_path)
    shuffled_df = df.sample(frac=1).reset_index(drop=True)
    shuffled_df.to_csv(output_file_path, index=False)
    print(f"Data shuffled and saved to {output_file_path}.")
    return shuffled_df