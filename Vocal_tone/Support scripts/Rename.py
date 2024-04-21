import os

def rename_files(folder_path, new_name_prefix):
    """
    Rename all files in the given folder with a new name prefix.

    Args:
        folder_path (str): The path to the folder containing the files.
        new_name_prefix (str): The new name prefix to use for renaming.
    """
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    i = 1
    # Iterate through each file and rename it
    for index, file_name in enumerate(files):
        # Construct the new file name
        new_file_name = f"Angry_11_out-{i}.m4a"  # Adjust file extension as needed

        # Construct the full paths for the old and new file names
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_file_name)

        # Rename the file
        os.rename(old_file_path, new_file_path)
        i = i+1
        print(f"Renamed {old_file_path} to {new_file_path}")

# Example usage:
folder_path = "C:\\Users\ASUS\Downloads\documents7"
new_name_prefix = "new_file"  # Replace with your new name prefix
rename_files(folder_path, new_name_prefix)
    