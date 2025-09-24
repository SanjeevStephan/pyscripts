Tkinter is included by default with most Python installations, especially on Windows and macOS. But just to be sure everything’s set up properly, here’s how you can check and install it:

---

### ✅ Step 1: Check if Tkinter is Already Installed
Open a Python shell and type:
```python
import tkinter
tkinter._test()
```
If a small window pops up saying “This is a Tcl/Tk version…”, you’re good to go!

---

### 🛠️ Step 2: Install Tkinter (if not already installed)

#### On **Windows/macOS** (with Python from [python.org](https://www.python.org)):
Tkinter is bundled. If it’s missing, reinstall Python and make sure to check **“Install Tcl/Tk”** during setup.

#### On **Linux (Ubuntu/Debian)**:
Use the package manager:
```bash
sudo apt-get install python3-tk
```

#### On **Linux (Fedora/Red Hat)**:
```bash
sudo dnf install python3-tkinter
```

---

### 🧪 Step 3: Test It Again
Run this simple script to confirm:
```python
import tkinter as tk

root = tk.Tk()
root.title("Tkinter Test")
tk.Label(root, text="Tkinter is working!").pack()
root.mainloop()
```

Let me know if you’re using a virtual environment or a specific IDE like VS Code or PyCharm—I can help tailor the setup.