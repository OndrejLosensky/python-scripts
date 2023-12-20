import os
import shutil
import time

def move_files(source_folder, destination_folder, extensions):
    # Creates folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # List of all files and folders in the source folder
    items = os.listdir(source_folder)

    # Move files and folders to the specified folder
    for item in items:
        item_path = os.path.join(source_folder, item)
        if os.path.isfile(item_path) and item.endswith(extensions):
            # Move files
            destination_path = os.path.join(destination_folder, item)
            shutil.move(item_path, destination_path)
            print(f"Moved file: {item}")
        elif os.path.isdir(item_path):
            # Move folders
            destination_path = os.path.join(destination_folder, item)
            shutil.move(item_path, destination_path)
            print(f"Moved folder: {item}")

def monitor_and_move(desktop_path, destination_folder, extensions):
    while True:
        move_files(desktop_path, destination_folder, extensions)
        time.sleep(5)

if __name__ == "__main__":
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    destination_folder = os.path.join(desktop_path, "_old")
    allowed_extensions = (".jpg", ".png", ".txt", ".pdf", ".webp", ".docx", ".xlsx", ".ai", ".zip", ".rtf", ".mp4")

    monitor_and_move(desktop_path, destination_folder, allowed_extensions)
