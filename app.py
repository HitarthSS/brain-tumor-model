import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Medical File Browser")
root.geometry("400x400")
root.configure(background="#fff")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("DICOM files", "*.dcm")])
    file_path_label.config(text=file_path)
    if file_path:
        img = ImageTk.PhotoImage(Image.open(file_path).resize((200, 200)))
        image_label.img = img
        image_label.config(image=img)

title_label = tk.Label(root, text="Browse Medical Files", font=("Helvetica", 18, "bold"), bg="#fff", fg="#2c3e50")
title_label.pack(pady=20)

browse_button = tk.Button(root, text="Browse", font=("Helvetica", 14, "bold"), bg="#2980b9", fg="#fff", command=browse_file)
browse_button.pack(pady=10)

file_path_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#fff", fg="#2c3e50")
file_path_label.pack()

image_label = tk.Label(root, bg="#fff")
image_label.pack(pady=20)

root.mainloop()
