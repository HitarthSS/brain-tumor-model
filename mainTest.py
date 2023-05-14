import cv2
from keras.models import load_model
from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox

# Load the model
model = load_model('BrainTumor10Epochs.h5')

# Create a Tkinter window
root = tk.Tk()
root.title('Brain Tumor Detection')
root.geometry('500x300')
root.config(bg='#1a1a2e')

# Create a label for the selected image
selected_image_label = tk.Label(root, text='No image selected.', font=('Helvetica', 14), bg='#1a1a2e', fg='#e6e6e6')
selected_image_label.pack(pady=10)

# Create a button to select an image
select_image_button = tk.Button(root, text='Select Image', font=('Helvetica', 14), bg='#e6e6e6', fg='#1a1a2e', command=lambda: select_image())
select_image_button.pack(pady=10)

# Function to open the file dialog and select an image
def select_image():
    file_path = filedialog.askopenfilename(filetypes=[('Image Files', '*.jpg;*.png;*.jpeg')])
    if file_path:
        selected_image_label.config(text=file_path)
        # Read the selected image
        image = cv2.imread(file_path)
        # Resize the image to 64x64
        img = Image.fromarray(image)
        img = img.resize((64, 64))
        img = np.array(img)
        # Feed the image to the model and get the prediction
        input_img = np.expand_dims(img, axis=0)
        prediction = model.predict(input_img)
        # Show the prediction in a message box
        if prediction > 0.5:
            messagebox.showinfo('Prediction', 'The image is likely to have a brain tumor.', icon='warning')
        else:
            messagebox.showinfo('Prediction', 'The image is unlikely to have a brain tumor.', icon='info')

root.mainloop()
