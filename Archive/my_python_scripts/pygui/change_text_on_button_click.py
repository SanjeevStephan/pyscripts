'''
    Description : shows a button, and when clicked, it changes the label text
    What It will Do!
    -> tk.Label to display text
    -> tk.Button with a command to trigger an action
    -> .config() to update widget properties dynamically
    @version (25-sep-2025)
    @author (Sanjeev Stephan Murmu)
'''

import tkinter as tk

# function to change the label text
def change_text():
    label.config(text="You Clicked the button!")

# Create the main window
root = tk.Tk()
root.title("Text Changer Python GUI")
root.geometry("400x400")

# Create a label
label = tk.Label(root, text="Click the button", font=("Helvetica", 14))
label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=change_text)
button.pack()

root.mainloop()