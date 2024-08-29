import os
import shutil

# Define the directory to be organized
directory = "D:/Pictures"

# File type folders
folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".avi", ".mov"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar"],
}

def organize_files():
    # Create folders if they don't exist
    for folder in folders:
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to respective folders
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            for folder, extensions in folders.items():
                if any(file_name.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(directory, folder, file_name))
                    break

if __name__ == "__main__":
    organize_files()
    print("Files organized successfully!")
