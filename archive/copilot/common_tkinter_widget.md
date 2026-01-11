Great question, Sam! Tkinter offers a rich set of widgets to build interactive GUI applications. Here’s a curated list of the most commonly used ones, along with what they do:

---

### 🧰 Common Tkinter Widgets

| Widget        | Purpose                                                                 |
|---------------|-------------------------------------------------------------------------|
| `Label`       | Displays text or images                                                 |
| `Button`      | Triggers an action when clicked                                         |
| `Entry`       | Single-line text input                                                  |
| `Text`        | Multi-line text input                                                   |
| `Checkbutton` | Checkbox for toggling options                                           |
| `Radiobutton` | Allows selection of one option from a group                            |
| `Listbox`     | Displays a list of items for selection                                  |
| `Combobox`    | Dropdown menu (via `ttk`)                                               |
| `Spinbox`     | Numeric input with up/down arrows                                      |
| `Scale`       | Slider for selecting a numeric value                                    |
| `Frame`       | Container to group other widgets                                        |
| `Canvas`      | Drawing area for shapes, images, and custom graphics                    |
| `Menu`        | Creates dropdown or context menus                                       |
| `Messagebox`  | Popup dialogs for alerts, confirmations, etc. (`tkinter.messagebox`)    |
| `Notebook`    | Tabbed interface (via `ttk`)                                            |
| `Progressbar` | Shows progress of a task (via `ttk`)                                    |

---

### 🧪 Example: Entry + Button + Label
```python
import tkinter as tk

def greet():
    name = entry.get()
    label.config(text=f"Hello, {name}!")

root = tk.Tk()
root.title("Greeting App")

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Greet", command=greet)
button.pack()

label = tk.Label(root, text="Enter your name above")
label.pack(pady=10)

root.mainloop()
```

---

Want to build a student quiz app with `Radiobuttons`, or a file uploader using `Canvas` and `Button`? I can help you scaffold it with examples tailored to your classroom or UPSC prep.