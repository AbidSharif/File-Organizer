import os
import shutil

# Path of folder to organize
source_folder = "Test_Files"

# File type folders
folders = {
    ".jpg": "Images",
    ".png": "Images",
    ".pdf": "Documents",
    ".mp3": "Music",
    ".mp4": "Videos"
}

# Read all files
for file in os.listdir(source_folder):

    file_path = os.path.join(source_folder, file)

    # Check if it is a file
    if os.path.isfile(file_path):

        # Get file extension
        extension = os.path.splitext(file)[1]

        # Check extension in dictionary
        if extension in folders:

            folder_name = folders[extension]

            destination_folder = os.path.join(source_folder, folder_name)

            # Create folder if not exists
            os.makedirs(destination_folder, exist_ok=True)

            # Move file
            shutil.move(file_path,
                        os.path.join(destination_folder, file))

            print(f"{file} moved to {folder_name}")

print("Files Organized Successfully!")