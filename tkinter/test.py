from tkinter import *
from PIL import Image

#main
window = Tk()
window.title("Test Window")

#photo

photo1 = PhotoImage(file="/home/pi/Desktop/ProtoVIS-V1/tkinter/testImage.jpg")
Label(window, image=photo1, background="black").grid(row = 1, column = 1, sticky=E)#sticky East, 左西
