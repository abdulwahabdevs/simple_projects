import os
import shutil

def create_folder(path: str, extension: str) -> str:
    """Create a folder at the given path with given extension"""

    folder_name: str = extension[1:0] # .png to png
    folder_path: str = os.path.join(path, folder_name)

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    return folder_path

def sort_files(source_path: str):
    """Sorts files by their extension"""

    for root_dir, sub_dir, filenames in os.walk(source_path):
        for filename in filenames:
            file_path: str = os.path.join(root_dir, filename)
            extension: str = os.path.splitext(filename)[1]

            if extension:
                target_folder: str = create_folder(source_path, extension)
                target_path: str = os.path.join(target_folder, filename)

                shutil.move(file_path, target_path)

def remove_empty_folders(source_path: str):
    """Removes empty folders"""

    for root_dir, sub_dir, filenames in os.walk(source_path, topdown=False):
        for current in sub_dir:
            folder_path: str = os.path.join(root_dir, current)

            if not os.listdir(folder_path):
                os.rmdir(folder_path)

def main():
    user_input: str = input("Enter the path of the folder to sort: ")

    if os.path.exists(path=user_input):
        sort_files(user_input)
        remove_empty_folders(user_input)
        print("Folder sorted successfully!")
    else:
        print("Sorry, the folder does not exist")

if __name__ == "__main__":
    main()

