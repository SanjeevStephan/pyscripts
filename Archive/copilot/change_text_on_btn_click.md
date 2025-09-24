Here’s a clean and simple Tkinter app that does exactly what you asked for, Sam — it shows a button, and when clicked, it changes the label text:

---

### 🖥️ Basic Tkinter App: Change Text on Button Click

```python
import tkinter as tk

# Function to change the label text
def change_text():
    label.config(text="You clicked the button!")

# Create the main window
root = tk.Tk()
root.title("Text Changer")
root.geometry("300x150")

# Create a label
label = tk.Label(root, text="Click the button", font=("Helvetica", 14))
label.pack(pady=20)

# Create a button
button = tk.Button(root, text="Click Me", command=change_text)
button.pack()

# Run the application
root.mainloop()
```

---

### 🧠 What You Learn
- `tk.Label` to display text
- `tk.Button` with a `command` to trigger an action
- `.config()` to update widget properties dynamically

Want to add an input box next so the label shows custom text from the user? Or maybe animate the button or change colors? I can help you level it up!