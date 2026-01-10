import tkinter as tk

root = tk.Tk()
root.title("Hello Tkinter")
root.geometry("150x150")

text = tk.Label(root, text="Hello Tkinter")
text.pack(pady=10)
root.mainloop()