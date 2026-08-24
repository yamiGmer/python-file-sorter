import customtkinter as ctk

# Appearance
ctk.set_appearance_mode("System") # "Light", "Dark"
ctk.set_default_color_theme("dark-blue")

# Main window
app = ctk.CTk()
app.title("File Sorter")
app.geometry("600x400")

# Configure Grid
app.grid_columnconfigure(0,weight=1)
app.grid_columnconfigure(1,weight=1)

container = {
    "Images": 1,
    "Documents": 2,
    "Videos": 2
}

def folder_list(file_count):
    counter = 1
    for file, count in file_count.items():
        file_header = ctk.CTkLabel(app,text="Folder Breakdown")
        file_header.grid(row=0, column=0,padx=20,pady=5)
        file_list = ctk.CTkLabel(app, text=f"{file} => {count}")
        file_list.grid(row=counter, column=0, padx=20,pady=1)
        counter+=1
        
folder_list(container)


# # Widget
# label = ctk.CTkLabel(app, text="Hello World!")
# label.pack(pady=20)



# def button_click_event():
#     dialog = ctk.CTkInputDialog(text="Type in a number:", title="Test")
#     label = ctk.CTkLabel(app,text=f"Number: {dialog.get_input()}")
#     label.pack()


# button = ctk.CTkButton(app, text="Open Dialog", command=button_click_event)
# button.pack(padx=20, pady=20)


app.mainloop()