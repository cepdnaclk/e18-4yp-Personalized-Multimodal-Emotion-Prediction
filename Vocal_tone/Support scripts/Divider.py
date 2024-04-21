import os
import shutil

# Path to the folder containing the files
folder_path = "C:\\Users\ASUS\Downloads\\vocal_data\AudioWA"

output_folder_path = "C:\Ruchira\Academic\.IMMEDIATE\FYP\FYP\Datasets\Common\Vocal"

# Create folders A, B, C, D if they don't exist
output_folders = ['HAP', 'SAD', 'ANG', 'NEU', 'DIS', 'FEA']

# Iterate through files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".wav"):
        # Extract the third part of the filename
        parts = filename.split('_')
        if len(parts) >= 3:
            category = parts[2]
            # Move the file to the corresponding folder
            if category in output_folders:
                src = os.path.join(folder_path, filename)
                dst = os.path.join(output_folder_path,category, filename)
                shutil.move(src, dst)
                print(f"Moved {filename} to folder {category}")
            else:
                print(f"Category {category} not recognized for file {filename}")
        else:
            print(f"Filename {filename} does not match the expected pattern")