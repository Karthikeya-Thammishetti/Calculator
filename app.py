import tkinter as tk

def on_click(value):
    if value == "AC":
        entry_var.set("")
    elif value == "⌫":
        entry_var.set(entry_var.get()[:-1])
    elif value == "=":
        try:
            result = eval(entry_var.get().replace("×", "*").replace("÷", "/"))
            entry_var.set(str(result))
        except:
            entry_var.set("Error")
    elif value == "+/-":
        try:
            if entry_var.get().startswith("-"):
                entry_var.set(entry_var.get()[1:])
            else:
                entry_var.set("-" + entry_var.get())
        except:
            pass
    else:
        entry_var.set(entry_var.get() + value)

# Main window
root = tk.Tk()
root.title("Android Style Calculator")
root.config(bg="#000000")
root.geometry("360x550")
root.resizable(False, False)

# Display
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Helvetica", 36), bg="#000000", fg="#ffffff",
                 bd=0, justify='right', insertbackground="#ffffff")
entry.pack(fill='both', ipadx=8, ipady=15, padx=10, pady=20)

# Button configuration
buttons = [
    ["AC", "⌫", "+/-", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["%", "0", ".", "="]
]

# Colors
btn_bg = "#1c1c1c"
btn_fg = "#ffffff"
accent_bg = "#2c2c2c"
blue_fg = "#1e90ff"
equal_bg = "#1e90ff"

# Button layout
for row in buttons:
    frame = tk.Frame(root, bg="#000000")
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        btn = tk.Button(
            frame,
            text=btn_text,
            font=("Helvetica", 20),
            fg=blue_fg if btn_text in ("AC", "⌫", "+/-", "÷", "×", "-", "+", "=") else btn_fg,
            bg=equal_bg if btn_text == "=" else accent_bg,
            relief='flat',
            bd=0,
            command=lambda val=btn_text: on_click(val)
        )
        btn.pack(side='left', expand=True, fill='both', padx=5, pady=5)

root.mainloop()





