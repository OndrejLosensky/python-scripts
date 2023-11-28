import os
import shutil
import time

def move_files(source_folder, destination_folder, extensions):
    # Creates folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # List of all files in the source folder
    files = os.listdir(source_folder)

    # Move files to the specified folder
    for file in files:
        if file.endswith(extensions):
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)
            shutil.move(source_path, destination_path)
            print(f"Moved: {file}")

def monitor_and_move(desktop_path, destination_folder, extensions):
    while True:
        move_files(desktop_path, destination_folder, extensions)
        time.sleep(5)

if __name__ == "__main__":
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    destination_folder = os.path.join(desktop_path, "_old")
    allowed_extensions = (".jpg", ".png", ".txt", ".pdf", ".webp", ".docx", ".xlsx", ".ai", ".zip", ".rtf")

    monitor_and_move(desktop_path, destination_folder, allowed_extensions)