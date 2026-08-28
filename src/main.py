from pathlib import Path
import customtkinter as ctk
from tkinter import filedialog

from window import window_start, folder_list
from window_widgets import toggle_frame, radio_selection
from sorter import extension_sorter, count_files, date_sorter
from rules import load_categories
from path_utils import clean_input



'''
==================================================================
Initialize categories and ui app and frame
==================================================================
'''
list_opened = False
categories = load_categories() # Initializes categories from json
app, frame1, frame2 = window_start()
frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

'''
==================================================================
Folder path input
==================================================================
'''
def browse_folder():
    path = filedialog.askdirectory()
    
    if path:
        path = Path(path)
        entry.delete(0,"end")
        entry.insert(0,str(path))
    
folder_label = ctk.CTkLabel(frame1, text="Folder:")
folder_label.pack(pady=(10, 2), padx=10, anchor="w")

browse_frame = ctk.CTkFrame(frame1, fg_color='transparent')
browse_frame.pack(pady=5, padx=10, fill="x")

entry = ctk.CTkEntry(browse_frame, placeholder_text="Enter File Path...")
entry.pack(side="left", fill="x", expand=True)

browse_btn = ctk.CTkButton(browse_frame, text="Browse", width=80, command=browse_folder)
browse_btn.pack(side="left", padx=(5,0))

'''
==================================================================
Radio button for choosing what type of sorting
==================================================================
'''
sort_label = ctk.CTkLabel(frame1, text="Sorting Method")
sort_label.pack(pady=1, padx=10, anchor="w")
sort_selections = ["File Extension(.pdf, .docx, .xlsx)", "Date Modified", "Date Created"]
sort_selection = radio_selection(frame1, sort_selections)


'''
==================================================================
Analyze Button
==================================================================
'''
def handle_file_list():
    global list_opened
    try:
        # Get the current entry value
        folder_path = Path(clean_input(entry.get()))

        # Validate path
        if not folder_path.exists():
            raise ValueError("Folder does not exist")

        if not folder_path.is_dir():
            raise ValueError("Path is not a folder")
        
        # Analyze folder
        file_count = count_files(folder_path,categories)
        
        # Display results
        folder_list(frame2,file_count)
        
        # Show frame2
        if not list_opened: frame2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        list_opened = True

        # Show Show/Hide button
        button2.pack(side="left", padx=5)
        
        # Enable Sort Button
        button3.configure(state="enabled")
        

    except ValueError as e:
        print("Error:", e)

# Initializes button frame
button_frame = ctk.CTkFrame(frame1,fg_color="transparent")
button_frame.pack(pady=20)

button = ctk.CTkButton(
    button_frame,
    text="Analyze Folder",
    command=handle_file_list,
    
)
button.pack(side="left", padx=5)


'''
==================================================================
Sort Button
==================================================================
'''
def handle_sort():
    try:
        selected_sort = sort_selection.get()
        folder_path = Path(clean_input(entry.get()))

        if not folder_path.exists():
            raise ValueError("Folder does not exist")

        if not folder_path.is_dir():
            raise ValueError("Path is not a folder")

        print("Sort selected:", selected_sort)
        print("Folder:", folder_path)
        
        if selected_sort == 1:
            extension_sorter(folder_path,categories)
        elif selected_sort == 2:
            date_sorter(folder_path, "modified") 
        elif selected_sort == 3:
            date_sorter(folder_path, "created")
        else:
            raise ValueError("Method is Unavailable")
             

    except ValueError as e:
        print("Error:", e)

    
    


button3 = ctk.CTkButton(
    button_frame,
    text="Sort Files",
    command=handle_sort,
)
button3.configure(state="disabled")
button3.pack(side="left", padx=5)

'''
==================================================================
Show/Hide Button
==================================================================
'''

button2 = ctk.CTkButton(
    button_frame,
    text="Hide",
    command=lambda: toggle_frame(frame2,button2),
    
)


# file_count = count_files(folder_path, categories)
# folder_list(frame2, file_count)






# print("File Sorter")
# folder_path = Path(clean_input(input("Enter file path: ")))


# '''
# Breakdown of file type in target folder

# '''

# print("File breakdown in folder")
# for file, count in file_count.items():
#     print(file,":",count)
    
# '''
# Confirmation for sorting files

# '''


# decision = input("Do you wish to proceed(Y/N): ").lower()
# confirm = ["yes","y", "confirm"]
# deny = ["no", "n", 'cancel']
# if decision in confirm:
#     extension_sorter(folder_path,categories)
# elif decision in deny:
#     print("See you next time")
# else:
#     print("Invalid choice")

app.mainloop()