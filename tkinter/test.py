from tkinter import *
from PIL import Image, ImageTk

#main
window = Tk()
window.title("Test Window")

#photo
img = Image.open("testImage.jpg")
photo1 = ImageTk.PhotoImage(img)
Label(window, image=photo1, background="black").grid(row = 1, column = 1, sticky=E)#sticky East, 左西


window.mainloop()