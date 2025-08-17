import tkinter as tk
from calculator import smart_calculate

def evaluate():
    user_input = entry.get()
    result = smart_calculate(user_input)
    result_label.config(text=result)

# Setup window
root = tk.Tk()
root.title("🧠 Smart Calculator")
root.geometry("400x250")
root.configure(bg="#f8f8f8")

# Heading
heading = tk.Label(root, text="Smart Calculator Bot", font=("Arial", 16), bg="#f8f8f8")
heading.pack(pady=10)

# Input field
entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=10)

# Button
button = tk.Button(root, text="Calculate", command=evaluate, font=("Arial", 12))
button.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14), fg="green", bg="#f8f8f8")
result_label.pack(pady=10)

# Run app
root.mainloop()
