import tkinter as tk

def change_text():
    button.config(text="Test")

root = tk.Tk()
root.title("Button Demo")

button = tk.Button(root, text="Click me", command=change_text)
button.pack(pady=20)

root.mainloop()
