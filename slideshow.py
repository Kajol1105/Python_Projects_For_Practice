from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("Image slider")

image_paths = [
    r"C:\Users\kajol\OneDrive\Desktop\PYjects\slider\0a88b39e6ae67472b53cfc7f3f0ce0d2.jpg",
    r"C:\Users\kajol\OneDrive\Desktop\PYjects\slider\328988a745013e9aba5b35313bf2145a.jpg",
    r"C:\Users\kajol\OneDrive\Desktop\PYjects\slider\3abbdaae8c7532c1788ff904c1a1fa5a.jpg",
    r"C:\Users\kajol\OneDrive\Desktop\PYjects\slider\0a558b9a860123c64cf8c473d576700d.jpg",
    r"C:\Users\kajol\OneDrive\Desktop\PYjects\slider\6d3c3ccb3c07546f30651b2cead7910a.jpg",
    r"C:\Users\kajol\OneDrive\Desktop\PYjects\slider\3b96f20f79bb81e0fd02c060958d4334.jpg",
    r"C:\Users\kajol\OneDrive\Desktop\PYjects\slider\18a6ed32ac5ab8f2ebfa0615f05254d9.jpg",
    r"C:\Users\kajol\OneDrive\Desktop\PYjects\slider\cdb7ff412b694fe2c8bdc80d0e90f748.jpg"
]

image_size = (500, 500)  # smaller is better for display
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(img) for img in images]

label = tk.Label(root)
label.pack()

slideshow = cycle(photo_images)

def update_image():
    img = next(slideshow)
    label.config(image=img)
    label.image = img  # prevent garbage collection
    root.after(3000, update_image)  # call again after 3 sec

def start_slideshow():
    update_image()

play_button = tk.Button(root, text='Play Slideshow', command=start_slideshow)
play_button.pack()

root.mainloop()
