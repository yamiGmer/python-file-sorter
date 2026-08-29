import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

def toggle_frame(frame, button):
    if frame.winfo_ismapped():
        frame.grid_forget()
        button.configure(text="Show")
    else:
        frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        button.configure(text="Hide")


def radio_selection(frame, selections):
    radio_var = ctk.IntVar(value=1)

    for value, selection in enumerate(selections, start=1):
        radiobutton = ctk.CTkRadioButton(
            frame,
            text=selection,
            variable=radio_var,
            value=value
        )
        radiobutton.pack(anchor="w", padx=10, pady=5)

    return radio_var

def confirm_action():
    answer = CTkMessagebox(
        title="Confirm",
        message="Are you sure you want to sort the folder?",
        icon="warning",
        option_1="Yes",
        option_2="No"
    ).get()
    
    return answer