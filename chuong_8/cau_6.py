import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Các loại Style của Button - Tkinter")
root.geometry("500x400")

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Red.TButton",
    foreground="white",
    background="#e74c3c",
    font=("Arial", 12, "bold"),
    padding=6,
)
style.map("Red.TButton", background=[("active", "#c0392b")])

style.configure(
    "Green.TButton",
    foreground="white",
    background="#27ae60",
    font=("Arial", 12, "bold"),
    padding=6,
)
style.map("Green.TButton", background=[("active", "#1e8449")])

style.configure(
    "Blue.TButton",
    foreground="white",
    background="#3498db",
    font=("Arial", 12, "bold"),
    padding=6,
)
style.map("Blue.TButton", background=[("active", "#2980b9")])

style.configure(
    "Outlined.TButton",
    foreground="#2c3e50",
    background="white",
    bordercolor="#2c3e50",
    relief="groove",
    font=("Arial", 12),
    padding=6,
)
style.map("Outlined.TButton", background=[("active", "#ecf0f1")])

style.configure(
    "Flat.TButton",
    foreground="#34495e",
    background="#bdc3c7",
    relief="flat",
    font=("Arial", 12),
    padding=6,
)
style.map("Flat.TButton", background=[("active", "#95a5a6")])

ttk.Button(root, text="Nút đỏ (Red)", style="Red.TButton").pack(pady=10)
ttk.Button(root, text="Nút xanh lá (Green)", style="Green.TButton").pack(pady=10)
ttk.Button(root, text="Nút xanh dương (Blue)", style="Blue.TButton").pack(pady=10)
ttk.Button(root, text="Nút viền (Outlined)", style="Outlined.TButton").pack(pady=10)
ttk.Button(root, text="Nút phẳng (Flat)", style="Flat.TButton").pack(pady=10)

root.mainloop()
