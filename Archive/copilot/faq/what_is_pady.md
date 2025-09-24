In Tkinter, `pady` stands for **"padding in the Y (vertical) direction"** — it adds vertical space around a widget.

### 🧱 How It Works
When you use `.pack()` or `.grid()`, you can specify `pady` to create space **above and below** the widget.

### 🧪 Example
```python
label = tk.Label(root, text="Hello")
label.pack(pady=20)  # Adds 20 pixels of vertical space above and below the label
```

This helps prevent your widgets from looking cramped and improves layout readability.

### 🔁 Related Option
- `padx` → Horizontal padding (left and right)

Want to see how `pady` compares with `ipady` (internal padding)? I can show you a side-by-side demo.