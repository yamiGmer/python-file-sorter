from pathlib import Path
from tkinter import messagebox
'''
Get input folder path and clean

'''
def clean_input(input_path: str) -> str:
    cleaned = input_path.strip().strip('"')

    if not cleaned:
        raise ValueError("Folder path cannot be empty")

    return cleaned

def get_folder_path(entry):
    folder_path = Path(clean_input(entry.get()))

    if not folder_path.exists():
        messagebox.showerror("Invalid Folder")

    if not folder_path.is_dir():
        messagebox.showerror("Path is not a folder")
    
    return folder_path
        


