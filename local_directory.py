import os


class SourceFolder():
    def __init__(self):
        self.path = ""
        self.select_path()

    def select_path(self):
        while self.path == "": 
            self.path = input("Please provide the absolute path of the folder containing the subfolders and files you wish to sync. \n"
                                        "Example: C:/ or C:/Folder_name\t")
            
            if os.path.exists(self.path):
                return self.select_path
            
            else:
                self.path = ""
                print("The path is not valid or inaccessable")
                continue
        return self.path


    def list_files(self):
        objects = os.listdir(self.path)
        return objects


class SelectedLocalFiles():
    def __init__(self, objects):
        self.objects = objects    # all files in the source folder


    def display_files(self):
        for i, object in enumerate(self.objects):
            print(f"({i+1}). - {object}")

    
    def select_choice(self):
        choice = ""

        while choice not in ["F", "S"]:
            choice = input("To sync the entire folder, press 'F'. To select specific files, press 'S'\t").upper()
            continue
        return choice
    
    def select_files(self, option):
        s_files = []
   
        # selecting the entire folder
        if option == "F":
            return self.objects
        
        # selecting specific files
        if option == "S":
            number = None
            numbers = []
            while not isinstance(number, int):
                try:
                    while True:
                        number = int(input("Provide the file number you want to synchronize. Press Enter for multiple files, and enter 0 (zero) to finish\t"))
                        if number in range(1, len(self.objects)+1):
                            if number not in numbers:
                                numbers.append(number)
                                print(f"({number}). - {self.objects[number-1]}")
                            else:
                                print("This file is already selected")
                           
                        elif number == 0 and not numbers:
                            print("You did not select any files")

                        elif number == 0 and numbers:   
                            break

                        else:
                            print("Please choose from the files numbers")

                except (ValueError, TypeError):
                    print("Please provide the selected file number as an integer.")
                    number = None
                continue

            # retrieving the names of selected files
            for number in numbers:
                file = self.objects[number-1]
                s_files.append(file)

            return s_files

if __name__ == "__main__":
    # Source
    source_object = SourceFolder()

    # create instances of the listed objects
    listed_objects = source_object.list_files()

    source_folder = source_object.select_path()

    folder_content = SelectedLocalFiles(listed_objects)
    folder_content.display_files()

    selected_option = folder_content.select_choice()
    selected_files = folder_content.select_files(selected_option)

