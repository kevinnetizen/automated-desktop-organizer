import os
import shutil


folder_path = "C:/Users/Admin/Downloads"


subfolders = ["Images", "Documents", "Videos"]

for folder_name in subfolders:
    target_path = os.path.join(folder_path, folder_name)
    if not os.path.exists(target_path):
        os.makedirs(target_path)


all_files = os.listdir(folder_path)

for file in all_files:
   
    source_path = os.path.join(folder_path, file)

    if os.path.isfile(source_path):
        
       
        file_name, file_extension = os.path.splitext(file)
        file_extension = file_extension.lower()
        
    
        if file_extension in ['.jpg', '.jpeg', '.png']:
            destination_path = os.path.join(folder_path, "Images", file)
            shutil.move(source_path, destination_path)
            print(f"Moved: {file} ---> Images")
            
        elif file_extension in ['.pdf', '.docx', '.txt']:
            destination_path = os.path.join(folder_path, "Documents", file)
            shutil.move(source_path, destination_path)
            print(f"Moved: {file} ---> Documents")
            
        elif file_extension in ['.mp4', '.mov']:
            destination_path = os.path.join(folder_path, "Videos", file)
            shutil.move(source_path, destination_path)
            print(f"Moved: {file} ---> Videos")