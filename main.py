import os
import shutil
import functionality as fn
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image

fn = fn.Functions()


class Items:
    def __init__(self):
        # Here I just create title
        self.img_number = 0
        frame_text = LabelFrame(root, padx=12, pady=14, bg='#535353')
        frame_text.grid(row=0, column=0, columnspan=3)

        text = Label(frame_text,
                     text="Batch processing GUI",
                     font=('OCR A Extended', '30', 'bold'),
                     bg='#535353',
                     fg='white')
        text.pack()

    def buttons(self, place, button_text, height, width, bd=0,
                relief=FLAT, command=None, ):
        # Button function
        self.button = Button(place,
                             text=button_text,
                             height=height,
                             width=width,
                             font=('OCR A Extended', '10'),
                             relief=relief,
                             activebackground='#535353',
                             command=command,
                             bd=bd)

    def frames(self, text, height, width, padx, pady):
        # Frame function
        self.frame = LabelFrame(root,
                                text=text,
                                height=height,
                                width=width,
                                padx=padx,
                                pady=pady,
                                bg='#535353',
                                font=('OCR A Extended', '12'),
                                fg='white')

    def grid(self, row, column, columnspan, sticky=None, pady=0, padx=0):
        # Grid function
        self.button.grid(row=row, column=column, columnspan=columnspan,
                         pady=pady, padx=padx, sticky=sticky)

    def next_image(self):
        # Function to switch to next image
        self.image_label.grid_forget()
        self.img_number += 1
        self.image()  # to refresh

    def prev_image(self):
        # Function to switch to previous image
        self.image_label.grid_forget()
        self.img_number -= 1
        self.image()  # to refresh

    def image(self):
        # Shows image in the GUI, try except method used to avoid index error
        images_list = os.listdir('C:/Users/User/Desktop/finalproj/IMAGES')
        try:
            image_path = os.path.join('C:/Users/User/Desktop/finalproj/IMAGES',
                                      images_list[self.img_number])
        except IndexError:
            self.img_number = 0
            self.image()

        try:
            image = Image.open(image_path)
            image = image.resize((200, 200))
            image = ImageTk.PhotoImage(image)

            self.image_label = Label(image=image)
            self.image_label.photo = image
            self.image_label.grid(row=2, column=1, rowspan=2,
                                  columnspan=2, pady=10, padx=10)

        except UnboundLocalError:
            pass

    def b_w_call(self):
        # Must be like this to refresh image shown in gui
        fn.black_white()
        self.image()  # to refresh image

    def watermark_call(self):
        # Must be like this to refresh image shown in gui
        fn.watermark()
        self.image()  # to refresh image

    def set_size(self):
        # Function that changes the size of an image, tuple method
        # used to change str(from the size_list) to tuple
        fn.resize(tuple(map(int, self.size.get().split(' x '))))

    def size(self):
        # Function to create size buttons
        size_list = ["128 x 128", "170 x 170", "200 x 200",
                     "320 x 320", "400 x 400", "500 x 500"]
        self.size = StringVar()
        self.size.set(size_list[0])

        self.frames(text='Choose size...', height=4, width=10,
                    padx=12, pady=14)
        self.frame.grid(row=1, column=0, columnspan=1,
                        pady=10, padx=10, sticky=W)

        self.buttons(place=self.frame, button_text='Select',
                     height=1, width=8, command=self.set_size)
        self.button.pack(pady=3)

        drop = OptionMenu(self.frame, self.size, *size_list)
        drop.pack()

    def open_watermark(self):
        # Function to open filedialog and choose watermark file
        # It's that strange indented to fit for rules of pep8
        # Try except method used to avoid error when closing the filedialog
        try:
            root.filename =\
                filedialog.askopenfilename(initialdir="/Desktop",
                                           title='Choose watermark',
                                           filetypes=(('PNG files',
                                                       '*.png'),
                                                      ('JPEG files',
                                                       '*.jpg'),
                                                      ('ALL files',
                                                       '*.*')))
            original = root.filename
            target = r'C:/Users/User/Desktop/finalproj/watermark.png'
            shutil.copyfile(original, target)
        except FileNotFoundError:
            pass

    def add_image(self):
        # Function to open filedialog and choose image file
        # It's that strange indented to fit for rules of pep8
        # Try except method used to avoid error when closing the filedialog
        try:
            root.filename =\
                filedialog.askopenfilename(initialdir="/Desktop",
                                           title='Choose file to add',
                                           filetypes=(('JPEG files',
                                                       '*.jpg'),
                                                      ('PNG files',
                                                       '*.png'),
                                                      ('ALL files',
                                                       '*.*')))
            original = root.filename
            name = os.path.basename(root.filename)
            target = r'C:/Users/User\Desktop/finalproj/IMAGES/'+str(name)
            shutil.copyfile(original, target)
        except FileNotFoundError:
            pass

    def about(self):
        # About/copyright messagebox function
        messagebox.showinfo('About', '''This is a simple batch processing GUI,
it takes images and applies on them filters,
resize them or add watermarks.

The app was developed for final project by Ala-Too University student.




Copyright © 2022 by Nazar Apsatarov''')

    def call(self):
        # Function that calls everything: buttons, frames etc.
        self.frames(text='', height=4, width=10, padx=12, pady=14)
        self.frame.grid(row=3, column=0, columnspan=1,
                        pady=0, padx=10, sticky=W)

        self.buttons(place=self.frame, button_text='Choose watermark...',
                     height=2, width=20,
                     relief=SUNKEN, command=self.open_watermark)
        self.grid(row=4, column=0, columnspan=1, pady=3, padx=0)

        self.buttons(place=self.frame, button_text='Apply watermark',
                     height=2, width=20,
                     relief=FLAT, command=self.watermark_call)
        self.grid(row=3, column=0, columnspan=1, pady=3, padx=0)

        self.buttons(place=root, button_text='B/W', height=4,
                     width=15, command=self.b_w_call)
        self.grid(row=2, column=0, columnspan=1, pady=10, padx=10, sticky=W)

        self.buttons(place=root, button_text='<', height=1,
                     width=3, command=self.prev_image)
        self.grid(row=4, column=1, columnspan=1,)

        self.buttons(place=root, button_text='>', height=1,
                     width=3, command=self.next_image)
        self.grid(row=4, column=2, columnspan=1)

        self.buttons(place=root, button_text='Add image..', height=4,
                     width=15, command=self.add_image)
        self.grid(row=1, column=1, columnspan=2)

        self.buttons(place=root, button_text='About', height=2,
                     width=13, command=self.about)
        self.grid(row=6, column=0, columnspan=1, pady=40, padx=20, sticky=SW)

        self.image()
        self.size()


# Root creation
root = Tk()
root.title('Batch processing GUI')
root.iconbitmap('C:/Users/User/Desktop/finalproj/logo.ico')
root.geometry('528x535')
root.configure(background='#535353')

i = Items()
i.call()

root.mainloop()
