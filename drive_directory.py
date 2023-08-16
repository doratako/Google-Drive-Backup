from googleapiclient.errors import HttpError
from authentication import drive_service


class TargetFolder():

    def list_drive_folders(self, service):
        try:
            results = service.files().list(
                                            q="mimeType='application/vnd.google-apps.folder'",
                                            fields="files(id, name, mimeType)").execute()
            folders = results.get('files', [])

            if not folders:
                print('No folders found.')
                return
        
        except HttpError as error:
            print(f'An error occurred: {error}')
        return folders


    def choose_target(self, folders):
        nums = []
        selected_folder = None

        for i, folder in enumerate(folders):
            if folder["mimeType"] == "application/vnd.google-apps.folder":
                print(f"({i+1}).- {folder['name']}")
                nums.append(i+1)
        
        while not selected_folder:
            try:
                num_target = int(input(f"Please choose a destination by entering a folder number.\t"))
                
                if num_target in nums:
                    selected_folder = folders[num_target-1]
                    return selected_folder

                else: 
                    print("Please choose from the folder numbers.")

            except (TypeError, ValueError):
                print("Please provide the selected folder number as an integer.")
            
            continue


if __name__ == "__main__":
    target = TargetFolder()
    drive_folders = target.list_drive_folders(drive_service)
    target_folder = target.choose_target(drive_folders)
    print(target_folder)
