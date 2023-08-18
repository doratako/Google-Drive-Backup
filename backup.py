import os
import json

from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from authentication import drive_service


class BackUpFiles():

    source_folder = None
    target_folder_name = None
    target_folder_drive_id = None
    selected_option = None

    def __init__(self):
        self.name = None 
        self.abs_path = None
        self.file_id = None

    def display(self):
        print(self.name)

    def set_abs_path(self):
        self.abs_path = os.path.join(self.source_folder, self.name)
        return self.abs_path
    
    def retrive_uploaded_files(self):
        results = drive_service.files().list(
                                        q=f"parents='{self.target_folder_drive_id}' and trashed=false",
                                        fields="files(id, name)").execute()
        
        uploaded_files = results.get('files', [])  # returns list of dictionaries
        return uploaded_files


    def upload(self):
        try:
            file_metadata = {'name': self.name,
                            'parents': [self.target_folder_drive_id]}
            
            media = MediaFileUpload(
                                    self.abs_path,
                                    mimetype='*/*',
                                    resumable=True)

            file = drive_service.files().create(body=file_metadata,
                                                media_body=media,
                                                fields='id, parents').execute()
            self.file_id = file.get('id')

        except HttpError as error:
            print(F'An error occurred: {error}')
            file = None

        return self.file_id
       

    def update(self, existing_id):
        try:

            file_metadata = {'name': self.name}

            media = MediaFileUpload(
                                    self.abs_path,
                                    mimetype='*/*',
                                    resumable=True)

            file = drive_service.files().update(
                                                fileId=existing_id,
                                                addParents=self.target_folder_drive_id,
                                                removeParents=self.target_folder_drive_id,
                                                body=file_metadata,
                                                media_body=media,
                                                fields='id, parents').execute()
  
        except HttpError as error:
            print(F'An error occurred: {error}')
            file = None


if __name__ == "__main__":
    # generate backup files instances based on parameters in the config file
    backup_files = BackUpFiles()

    with open("config.json", encoding="utf-8") as input_json:
        config_data = json.load(input_json)
    
    backup_files.source_folder = config_data["source_folder"]
    backup_files.target_folder_name = config_data["target_folder_name"]  
    backup_files.target_folder_drive_id = config_data["target_folder_drive_id"]
    backup_files.selected_option = config_data["selected_option"]


    # upload/update files to the target location
    uploaded_files_name_list = []

    if backup_files.selected_option == "F":
        selected_files = os.listdir(backup_files.source_folder)

    if backup_files.selected_option == "S":
        selected_files = config_data["selected_files"]   

    
    for file in selected_files:
        backup_files.name = file
        file_path = backup_files.set_abs_path()
        #backup_files.display()

        uploaded_files_list = backup_files.retrive_uploaded_files()
        
        for uploaded_files_dict in uploaded_files_list:  
            uploaded_files_name_list.append(uploaded_files_dict["name"])

        if backup_files.name not in uploaded_files_name_list and backup_files.name in selected_files:
            backup_files.upload()

        if backup_files.name in uploaded_files_name_list:
            if backup_files.name == uploaded_files_dict["name"]:
                backup_files.update(uploaded_files_dict["id"])

