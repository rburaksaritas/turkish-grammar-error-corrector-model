from datasets import load_dataset
import pandas as pd

# Load the dataset
dataset = load_dataset("mcemilg/GECTurk-generation")

# Access the train split
train_data = dataset["train"]

# Extract only the target sentences and create a DataFrame
df_targets = pd.DataFrame({'target': [example['target'] for example in train_data]})

# Define the file path where you want to save the CSV (adjust according to your desired location)
directory_path = 'dataset'  # Change this to your preferred path
file_name = "correct.csv"
file_path = directory_path + '/' + file_name
# Save the DataFrame with only targets to a CSV file
df_targets.to_csv(file_path, index=False)

print(f"Target sentences saved to {file_path}")
