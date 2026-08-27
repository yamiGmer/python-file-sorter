from sorter import extension_sorter, count_files
from .rules import load_categories
from pathlib import Path

categories = load_categories() # Initializes categories from json


'''
Get input folder path and clean

'''
def clean_input(input_path: str) -> str:
    cleaned = input_path.replace("\\", "/").replace('"', "")
    return cleaned

print("File Sorter")
folder_path = Path(clean_input(input("Enter file path: ")))


'''
Breakdown of file type in target folder

'''
file_count = count_files(folder_path, categories)
print("File breakdown in folder")
for file, count in file_count.items():
    print(file,":",count)
    
'''
Confirmation for sorting files

'''
decision = input("Do you wish to proceed(Y/N): ").lower()
confirm = ["yes","y", "confirm"]
deny = ["no", "n", 'cancel']
if decision in confirm:
    extension_sorter(folder_path,categories)
elif decision in deny:
    print("See you next time")
else:
    print("Invalid choice")
