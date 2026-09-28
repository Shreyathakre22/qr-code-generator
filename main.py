import qrcode
import tkinter as tk
from tkinter import messagebox

def generate_qr():
    data = entry.get()

    if data == "":
        messagebox.showerror("Error", "Please enter text or URL")
        return

    img = qrcode.make(data)
    img.save("qrcode.png")

    messagebox.showinfo("Success", "QR Code saved as qrcode.png")

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x200")

label = tk.Label(root, text="Enter Text or URL", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

button = tk.Button(root, text="Generate QR Code", command=generate_qr)
button.pack(pady=20)

root.mainloop()

