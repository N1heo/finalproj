import os
from PIL import Image


class Functions:
    def __init__(self):
        self.startfolder = 'C:/Users/User/Desktop/finalproj/IMAGES'

    def black_white(self):
        for imagePath in os.listdir(self.startfolder):
            folderPath = os.path.join(self.startfolder, imagePath)

            img = Image.open(folderPath)
            img = img.convert('L')
            img.save(folderPath)

    def resize(self, size):
        for imagePath in os.listdir(self.startfolder):
            folderPath = os.path.join(self.startfolder, imagePath)

            img = Image.open(folderPath)
            img = img.resize(tuple(size))
            img.save(folderPath)

    def watermark(self):
        for imagePath in os.listdir(self.startfolder):
            folderPath = os.path.join(self.startfolder, imagePath)
            img = Image.open(folderPath)
            width, height = img.size

            watermark =\
                Image.open('C:/Users/User/Desktop/finalproj/watermark.png')
            watermark = watermark.resize((width//3, height//3))

            img.paste(watermark,
                      (int(width-width*0.4), int(height-width*0.3)),
                      watermark)
            img.save(folderPath)
