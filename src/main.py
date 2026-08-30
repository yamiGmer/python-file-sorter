from pathlib import Path
import customtkinter as ctk
from tkinter import filedialog, messagebox

from window import window_start, folder_list
from window_widgets import toggle_frame, radio_selection, confirm_action
from sorter import extension_sorter, count_files, date_sorter
from rules import load_categories
from path_utils import get_folder_path

class FileSorterApp:
    def __init__(self):
        
        # Load the sorting categories from the JSON file
        self.categories = load_categories()

        # Create the main application window and the two main frames
        self.app, self.settings_frame, self.breakdown_frame = window_start()

        # Place the settings frame inside the main application window
        self.settings_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Variable used to store and track the folder path entered by the user
        self.path_var = ctk.StringVar()
        
        # Create the different sections of the user interface
        self.create_path_input()
        self.create_sort_selection()
        self.create_buttons()
    
    # Called whenever the folder path changes
    def path_changed(self, *args):
        path = self.path_var.get()
        print("Path changed:", path)

        # Reset the analysis because the selected folder has changed
        self.reset_analysis()
        
    # Resets the analysis-related parts of the interface
    def reset_analysis(self):
        # Disable the Sort button
        self.sort_button.configure(state="disabled")

        # Hide the toggle button
        self.toggle_button.pack_forget()
        
        # Hide the folder breakdown frame
        self.breakdown_frame.grid_remove()
    
    # Opens a folder selection dialog
    def browse_folder(self):
        path = filedialog.askdirectory()

        # If the user selected a folder, update the path variable
        if path:
            self.path_var.set(str(Path(path)))
    
    # Analyzes the selected folder and displays the results
    def analyze_folder(self, folder_path):
        # Count the files in the selected folder
        file_count = count_files(folder_path,self.categories)
        
        # Display the file count/breakdown
        folder_list(self.breakdown_frame,file_count)
        
        # Show the breakdown frame
        self.breakdown_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        # Show the Show/Hide button
        self.toggle_button.pack(side="left", padx=5)
        
        # Enable the Sort button now that analysis is complete
        self.sort_button.configure(state="normal")
        
    # Handles the Analyze Folder button
    def handle_file_list(self):
        try:
            # Temporarily disable the Analyze button while processing
            self.analyze_button.configure(state="disabled")

            # Validate and retrieve the folder path from the entry field
            folder_path = get_folder_path(self.entry)

            # Analyze the selected folder
            self.analyze_folder(folder_path)
            
        # Display an error if the folder path is invalid
        except ValueError as e:
            messagebox.showerror("Error: ",str(e))

        # Always re-enable the Analyze button after processing
        finally:
            self.analyze_button.configure(state="normal")
            
    # Handles the Sort Files button
    def handle_sort(self):
        try:
            # Ask the user to confirm before sorting
            if confirm_action() != "Yes":
                return
            
            # Get the sorting method selected by the user
            selected_sort = self.sort_selection.get()

            # Validate and retrieve the folder path
            folder_path = get_folder_path(self.entry)
            
            # Print information for debugging
            print("Sort selected:", selected_sort)
            print("Folder:", folder_path)
            
            # Perform the appropriate sorting operation
            if selected_sort == "extension":
                extension_sorter(folder_path,self.categories)
            elif selected_sort == "modified":
                date_sorter(folder_path, "modified")
            elif selected_sort == "created":
                date_sorter(folder_path, "created")
            else:
                # Display an error if no valid sorting method was selected
                messagebox.showerror("Method is unavailable")
            
            # Recalculate the folder breakdown after sorting
            file_count = count_files(folder_path, self.categories)

            # Refresh the displayed breakdown
            folder_list(self.breakdown_frame, file_count)
                
        # Display an error if the folder path is invalid
        except ValueError as e:
            messagebox.showerror("Error: ",str(e))
    

    # Creates the folder path input section
    def create_path_input(self):
        # Create the "Folder:" label
        folder_label = ctk.CTkLabel(self.settings_frame, text="Folder:")
        folder_label.pack(pady=(10, 2), padx=10, anchor="w") 

        # Create a frame to contain the entry field and Browse button
        browse_frame = ctk.CTkFrame(self.settings_frame, fg_color='transparent')
        browse_frame.pack(pady=5, padx=10, fill="x")

        # Create the folder path entry field
        self.entry = ctk.CTkEntry(browse_frame, placeholder_text="Enter File Path...", textvariable=self.path_var)
        self.entry.pack(side="left", fill="x", expand=True)

        # Create the Browse button
        browse_btn = ctk.CTkButton(browse_frame, text="Browse", width=80, command=self.browse_folder)
        browse_btn.pack(side="left", padx=(5,0))

        # Watch for changes to the folder path
        self.path_var.trace_add("write", self.path_changed)

    
    # Creates the radio buttons for selecting the sorting method
    def create_sort_selection(self):
        # Create the sorting method label
        sort_label = ctk.CTkLabel(self.settings_frame, text="Sorting Method")
        sort_label.pack(pady=1, padx=10, anchor="w")

        # Define the available sorting methods
        sort_selections = {
            "extension": "File Extension (.pdf, .docx, .xlsx)",
            "modified": "Date Modified",
            "created": "Date Created",
        }

        # Create the radio button selection and store it for later use
        self.sort_selection = radio_selection(self.settings_frame, sort_selections)
    
    # Creates the Analyze, Sort, and Show/Hide buttons
    def create_buttons(self):
        # Create a frame to hold the buttons
        button_frame = ctk.CTkFrame(self.settings_frame,fg_color="transparent")
        button_frame.pack(pady=20)

        # Create the Analyze Folder button
        self.analyze_button = ctk.CTkButton(
            button_frame,
            text="Analyze Folder",
            command=self.handle_file_list,
            
        )
        self.analyze_button.pack(side="left", padx=5)
        
        # Create the Sort Files button
        self.sort_button = ctk.CTkButton(
            button_frame,
            text="Sort Files",
            command=self.handle_sort,
        )

        # Disable sorting until a folder has been analyzed
        self.sort_button.configure(state="disabled")
        self.sort_button.pack(side="left", padx=5)
        
        # Create the Show/Hide breakdown button
        self.toggle_button = ctk.CTkButton(
            button_frame,
            text="Hide",
            command=lambda: toggle_frame(self.breakdown_frame,self.toggle_button),
            
        )
    
    

# Create an instance of the application
app = FileSorterApp()

# Start the Tkinter event loop
app.app.mainloop()

        
    
