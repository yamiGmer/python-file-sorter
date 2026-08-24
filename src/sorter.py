from pathlib import Path
import shutil

from rules import load_categories

# categories = load_categories()

'''
Handles duplicate

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
Counts file

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

'''

def file_sorter(folder_path:Path, categories):
    
    for file in folder_path.iterdir():
        # Ignore folders
        if not file.is_file():
            continue
        
        category = get_category(file, categories)
        
        # Create category folder
        category_folder = folder_path / category
        category_folder.mkdir(exist_ok=True)
        
        # Create destination path
        destination = category_folder / file.name
        # Handle duplicate
        destination = get_unique_destination(destination)
        print(file, "->", destination)
        shutil.move(file,destination)
        
