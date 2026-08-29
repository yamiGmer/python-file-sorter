from pathlib import Path
import customtkinter as ctk
from tkinter import filedialog, messagebox


from window import window_start, folder_list
from window_widgets import toggle_frame, radio_selection, confirm_action
from sorter import extension_sorter, count_files, date_sorter
from rules import load_categories
from path_utils import clean_input, get_folder_path




'''
==================================================================
Initialize categories and ui app and frame
==================================================================
'''
list_opened = False
categories = load_categories() # Initializes categories from json
app, settings_frame, breakdown_frame = window_start()
settings_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

'''
==================================================================
Folder path input
==================================================================
'''
path_var = ctk.StringVar()

def reset_analysis():
    global list_opened
    
    # disables sort button and hides frame and toggle button
    sort_button.configure(state="disabled")
    toggle_button.pack_forget()
    
    # Removes breakdown frame
    breakdown_frame.grid_remove()

def path_changed(*args):
    path = path_var.get()
    print("Path changed:", path)
    reset_analysis()
    
    
    
    
def browse_folder():
    path = filedialog.askdirectory()
    
    if path:
        path_var.set(str(Path(path)))
    
folder_label = ctk.CTkLabel(settings_frame, text="Folder:")
folder_label.pack(pady=(10, 2), padx=10, anchor="w") 

browse_frame = ctk.CTkFrame(settings_frame, fg_color='transparent')
browse_frame.pack(pady=5, padx=10, fill="x")

entry = ctk.CTkEntry(browse_frame, placeholder_text="Enter File Path...", textvariable=path_var)
entry.pack(side="left", fill="x", expand=True)

browse_btn = ctk.CTkButton(browse_frame, text="Browse", width=80, command=browse_folder)
browse_btn.pack(side="left", padx=(5,0))

path_var.trace_add("write", path_changed)



'''
==================================================================
Radio button for choosing what type of sorting
==================================================================
'''
sort_label = ctk.CTkLabel(settings_frame, text="Sorting Method")
sort_label.pack(pady=1, padx=10, anchor="w")

sort_selections = {
    "extension": "File Extension (.pdf, .docx, .xlsx)",
    "modified": "Date Modified",
    "created": "Date Created",
}
sort_selection = radio_selection(settings_frame, sort_selections)


'''
==================================================================
Analyze Button
==================================================================
'''    
def analyze_folder(folder_path):
    # Analyze folder
    file_count = count_files(folder_path,categories)
    
    # Display results
    folder_list(breakdown_frame,file_count)
    
    # Show breakdown_frame
    breakdown_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    
    # Show Show/Hide button
    toggle_button.pack(side="left", padx=5)
    
    # Enable Sort Button
    sort_button.configure(state="normal")
    

def handle_file_list():
    global list_opened
    try:
        analyze_button.configure(state="disabled")

        # Validate path
        folder_path = get_folder_path(entry)

        analyze_folder(folder_path)
        

    except ValueError as e:
        messagebox.showerror("Error: ",str(e))
    finally:
        analyze_button.configure(state="normal")

# Initializes button frame
button_frame = ctk.CTkFrame(settings_frame,fg_color="transparent")
button_frame.pack(pady=20)

analyze_button = ctk.CTkButton(
    button_frame,
    text="Analyze Folder",
    command=handle_file_list,
    
)
analyze_button.pack(side="left", padx=5)


'''
==================================================================
Sort Button
==================================================================
'''
def handle_sort():
    try:
        if confirm_action() != "Yes":
            return
        
        selected_sort = sort_selection.get()

        # Validate path
        folder_path = get_folder_path(entry)
        
        
        print("Sort selected:", selected_sort)
        print("Folder:", folder_path)
        
        if selected_sort == "extension":
            extension_sorter(folder_path,categories)
        elif selected_sort == "modified":
            date_sorter(folder_path, "modified")
        elif selected_sort == "created":
            date_sorter(folder_path, "created")
        else:
            messagebox.showerror("Method is unavailable")
        
        # Refreshes folder breakdown
        file_count = count_files(folder_path, categories)
        folder_list(breakdown_frame, file_count)
             

    except ValueError as e:
        messagebox.showerror("Error: ",str(e))

    
    


sort_button = ctk.CTkButton(
    button_frame,
    text="Sort Files",
    command=handle_sort,
)
sort_button.configure(state="disabled")
sort_button.pack(side="left", padx=5)

'''
==================================================================
Show/Hide Button
==================================================================
'''

toggle_button = ctk.CTkButton(
    button_frame,
    text="Hide",
    command=lambda: toggle_frame(breakdown_frame,toggle_button),
    
)

app.mainloop()