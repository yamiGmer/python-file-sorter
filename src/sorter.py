from pathlib import Path
import shutil
from datetime import datetime

# from rules import load_categories
# categories = load_categories()

TEST_FOLDER_PATH = Path(r"C:/Users/Fred/Downloads/test_folder")

'''
Handles duplicate by adding counter at the end of file

'''
def get_unique_destination(destination:Path) -> Path:
    if not destination.exists():
        return destination
    
    counter = 1
    
    while True:
        new_name = f"{destination.stem}_{counter}{destination.suffix}"
        new_destination = destination.parent / new_name
        
        if not new_destination.exists():
            return new_destination
        
        counter += 1

'''
Gets input file path and categorizes based on extension

'''
def get_category(file:Path, categories):
    extension = file.suffix.lower()
    
    for category, extensions in categories.items():
        if extension in extensions:
            return category
        
    return "Others"

'''
Gets input file path and returns year and month

'''
def get_date(file:Path, date_type):
    stat = file.stat()        
    timestamp = stat.st_mtime if date_type == "modified" else stat.st_birthtime
    date = datetime.fromtimestamp(timestamp).strftime("%Y-%m")
    
    return date

'''
Sort and count files by extension

'''    
def count_files(folder_path:Path, categories):
    categories_container = {}
    
    for file in folder_path.iterdir():
        if not file.is_file():
            continue
        
        category = get_category(file, categories)

        if category not in categories_container:
            categories_container[category] = 0

        categories_container[category] += 1
    
    return categories_container

'''
Sort and count files by month or year modified or created

'''
def count_date(folder_path:Path, date_type):
    date_container = {}
    for file in folder_path.iterdir():
        date = get_date(file, date_type)
                
        if date not in date_container: # initializes date
            date_container[date] = 0
            
        date_container[date] += 1
    
    return date_container

'''
Creates folder based on modifier and moves file to destination

'''
def move_file(folder_path: Path, file:Path, modifier):
    # Create folder
    target_folder = folder_path / modifier
    target_folder.mkdir(exist_ok=True)
    
    # Create destination path
    destination = target_folder / file.name
    
    # Handle duplicate
    destination = get_unique_destination(destination)
    print(file, "->", destination)
    shutil.move(file,destination)
        
'''
Sorts file based on extension

'''
def extension_sorter(folder_path:Path, categories):
    
    for file in folder_path.iterdir():
        # Ignore folders
        if not file.is_file():
            continue
        
        category = get_category(file, categories)
        
        move_file(folder_path, file, category)
    
'''
Sorts file based on date

'''
def date_sorter(folder_path:Path, date_type):
    for file in folder_path.iterdir():
        # Ignore folders
        if not file.is_file():
            continue
        
        date = get_date(file,date_type)
        
        move_file(folder_path, file, date)
 

date_sorter(TEST_FOLDER_PATH, "modified")  
# date_container = count_date(TEST_FOLDER_PATH, "modified")
# for date, count in date_container.items():
#         print(date,":",count)