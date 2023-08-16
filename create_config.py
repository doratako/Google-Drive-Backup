import json

from local_directory import SourceFolder, SelectedLocalFiles
from drive_directory import TargetFolder
from authentication import drive_service


def set_up():

# Source
    # local folder
    source_object = SourceFolder()

    # list files in the local folder
    listed_objects = source_object.list_files()

    # set path of the local folder
    source_folder = source_object.select_path()

    # instances of files in the local folder
    folder_content = SelectedLocalFiles(listed_objects)
    folder_content.display_files()
    
    # selected files with given option
    selected_option = folder_content.select_choice()
    selected_files = folder_content.select_files(selected_option)


# Target
    print("\n")
    print("-----Select destination-----")

    target = TargetFolder()

    # listing folders in MyDrive
    drive_folders = target.list_drive_folders(drive_service)

    # selecting a folder as destination
    target_folder = target.choose_target(drive_folders)
    
    # Drive folder name
    target_folder_name = target_folder["name"]  
    # Drive folder ID
    target_folder_drive_id = target_folder["id"] 


# Config file
    if selected_option == "F":
        data = {"source_folder": source_folder,
                "target_folder_name": target_folder_name,
                "target_folder_drive_id": target_folder_drive_id,
                "selected_option": selected_option}

    if selected_option == "S":
        data = {"source_folder": source_folder,
                "target_folder_name": target_folder_name,
                "target_folder_drive_id": target_folder_drive_id,
                "selected_option": selected_option,
                "selected_files": selected_files}
 

    with open("config.json", "w", encoding="utf-8") as config_file:
        json.dump(data, config_file, ensure_ascii=False)


if __name__ == "__main__":
    set_up()

