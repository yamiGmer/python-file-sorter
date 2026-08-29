import customtkinter as ctk
from pathlib import Path


def window_start():
    # Appearance
    ctk.set_appearance_mode("System") # "Light", "Dark"
    ctk.set_default_color_theme("dark-blue")

    # Main window
    app = ctk.CTk()
    app.title("File Sorter")
    app.geometry("700x500")

    # Configure Grid
    app.grid_columnconfigure(0,weight=1)
    app.grid_columnconfigure(1,weight=0)
    # Expand row
    app.grid_rowconfigure(0,weight=1)
    
    #  Creates 2 frame and put in grid
    frame1 = ctk.CTkFrame(app)
    frame2 = ctk.CTkFrame(app)
    
    return app, frame1, frame2


def folder_list(frame, file_count):
    # Refreshes the frame in case of path changes
    for widget in frame.winfo_children():
        widget.destroy()
    
    header = ctk.CTkLabel(
        frame,
        text="Folder Breakdown"
    )
    header.pack(padx=20, pady=(10, 5))

    # Container for the table
    table = ctk.CTkFrame(frame)
    table.pack(fill="x", padx=20, pady=5)

    # Make the first column expand
    table.grid_columnconfigure(0, weight=1)

    # Headers
    type_header = ctk.CTkLabel(
        table,
        text="Type"
    )
    type_header.grid(row=0, column=0, sticky="w", padx=10, pady=5)

    count_header = ctk.CTkLabel(
        table,
        text="Count"
    )
    count_header.grid(row=0, column=1, sticky="e", padx=10, pady=5)

    # File counts
    total_files = 0

    for row, (file, count) in enumerate(file_count.items(), start=1):
        type_label = ctk.CTkLabel(
            table,
            text=file
        )
        type_label.grid(row=row, column=0, sticky="w", padx=10, pady=3)

        count_label = ctk.CTkLabel(
            table,
            text=str(count)
        )
        count_label.grid(row=row, column=1, sticky="e", padx=10, pady=3)

        total_files += count

    # Total
    total_label = ctk.CTkLabel(
        table,
        text="Total Files"
    )
    total_label.grid(
        row=len(file_count) + 1,
        column=0,
        sticky="w",
        padx=10,
        pady=(10, 5)
    )

    total_count = ctk.CTkLabel(
        table,
        text=str(total_files)
    )
    total_count.grid(
        row=len(file_count) + 1,
        column=1,
        sticky="e",
        padx=10,
        pady=(10, 5)
    )



        

