from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
from random import randint


class Functionality:
    def __init__(self):
        pass

    def smth(self):
        pass


root = Tk()
root.title('Batch processing GUI')
root.iconbitmap('C:/Users/User/Desktop/finalproj/logo.ico')
root.geometry('528x600')
root.configure(background='#535353')


# Create frame for title
frame_text = LabelFrame(root, padx=12, pady=14, bg='#535353')
frame_text.grid(row=0, column=0, columnspan=3)

# # Create big frame
# frame_big = LabelFrame(root, padx=4, pady=5, bg='#535353')
# frame_big.pack()

# Create title
text = Label(frame_text,
             text="Batch processing GUI",
             font=('OCR A Extended', '30', 'bold'),
             bg='#535353',
             fg='white')
text.pack()

# Buttons
choose_file = Button(root,
                     text='Choose file...',
                     height=4,
                     width=15,
                     font=('OCR A Extended', '10'))
choose_file.grid(row=1, column=1, pady=10)

b_w = Button(root,
             text='B/w filter',
             height=4,
             width=15,
             font=('OCR A Extended', '10'))
b_w.grid(row=2, column=0, pady=10)

size = Button(root,
              text='Size',
              height=4,
              width=15,
              font=('OCR A Extended', '10'))
size.grid(row=1, column=0, pady=10)

watermark = Button(root,
                   text='Add watermark',
                   height=4,
                   width=15,
                   font=('OCR A Extended', '10'))
watermark.grid(row=3, column=0, pady=10)

# Take first images path in IMAGE folder
images_list = os.listdir('C:/Users/User/Desktop/finalproj/IMAGES')
rand_number = randint(1, len(images_list))
image_path = os.path.join('C:/Users/User/Desktop/finalproj/IMAGES',
                          images_list[rand_number])

image_ = ImageTk.PhotoImage(Image.open(image_path))
image_label = Label(image=image_)
image_label.grid(row=2, column=1, rowspan=8, pady=20, padx=20)

root.mainloop()
