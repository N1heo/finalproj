from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
from random import randint


class Items:
    def __init__(self):
        frame_text = LabelFrame(root, padx=12, pady=14, bg='#535353')
        frame_text.grid(row=0, column=0, columnspan=3)

        text = Label(frame_text,
                     text="Batch processing GUI",
                     font=('OCR A Extended', '30', 'bold'),
                     bg='#535353',
                     fg='white')
        text.pack()

    def buttons(self, button_text, height, width):
        self.button = Button(root,
                             text=button_text,
                             height=height,
                             width=width,
                             font=('OCR A Extended', '10'))

    def grid(self, row, column, columnspan, pady, padx):
        self.button.grid(row=row, column=column, columnspan=columnspan,
                         pady=pady, padx=padx)

    def image(self):
        images_list = os.listdir('C:/Users/User/Desktop/finalproj/IMAGES')
        rand_number = randint(1, len(images_list)-1)
        image_path = os.path.join('C:/Users/User/Desktop/finalproj/IMAGES',
                                  images_list[rand_number])

        image = Image.open(image_path)
        image = image.resize((200, 200))
        image = ImageTk.PhotoImage(image)

        image_label = Label(image=image)
        image_label.photo = image
        image_label.grid(row=2, column=1, rowspan=8, pady=20, padx=20)

    def call(self):
        self.buttons(button_text='Choose file...', height=4, width=15)
        self.grid(row=1, column=1, columnspan=1, pady=10, padx=0)
        self.buttons(button_text='Size', height=4, width=15)
        self.grid(row=1, column=0, columnspan=1, pady=10, padx=0)
        self.buttons(button_text='B/W', height=4, width=15)
        self.grid(row=2, column=0, columnspan=1, pady=10, padx=0)
        self.buttons(button_text='Watermark', height=4, width=15)
        self.grid(row=3, column=0, columnspan=1, pady=10, padx=0)
        self.image()


root = Tk()
root.title('Batch processing GUI')
root.iconbitmap('C:/Users/User/Desktop/finalproj/logo.ico')
root.geometry('528x600')
root.configure(background='#535353')

i = Items()
i.call()

root.mainloop()
