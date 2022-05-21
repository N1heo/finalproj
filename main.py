from tkinter import *


class Funcionallity:
    def __init__(self):
        pass

    def smth(self):
        pass


root = Tk()
root.title('Batch processing GUI')
root.iconbitmap('C:/Users/User/Desktop/finalproj/logo.ico')
root.geometry('1000x600')
root.configure(background='#535353')

# empty = Label(root, text= '                ')
# empty.grid(row=0, column=0, )
frame = LabelFrame(root, padx=9, pady=7, bg='#535353')
frame.pack(pady=8)

frame_for_window = LabelFrame(root, padx=900, pady=300, bg='#535353')
frame_for_window.pack(padx=30, pady=25)

text = Label(frame,
             text="Batch processing GUI",
             font=('OCR A Extended', '30', 'bold'),
             bg='#535353',
             fg='white')
text.pack()

empty_label = Label(frame_for_window, text='')
empty_label.pack()
# text.grid(row=0, column=0, columnspan=3)

root.mainloop()
