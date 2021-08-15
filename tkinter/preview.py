#!/usr/bin/python
import Tkinter as tk
import RPi.GPIO as GPIO
import picamera
from time import sleep

camera = picamera.PiCamera()
choices = ['off', 'auto', 'sunlight','cloudy','shade','tungsten','fluorescent','incandescent','flash','horizon']
effects = ['none','negative','solarize','sketch','denoise','emboss','oilpaint','hatch','gpen','pastel','watercolor','film','blur','saturation','colorswap','washedout','posterise','colorpoint','colorbalance','cartoon','deinterlace1','deinterlace2']

def CameraON():
    camera.preview_fullscreen=False
    camera.preview_window=(90,100, 320, 240)
    camera.resolution=(640,480)
    camera.start_preview()

def CameraOFF():
    camera.stop_preview()

def EXIT():
    root.destroy
    camera.stop_preview()
    camera.close()
    quit()

def UpdateBrightness(value):
    camera.brightness = int(value)

def UpdateContrast(value):
    camera.contrast = int(value)

def UpdateSharpness(value):
    camera.sharpness = int(value)

def UpdateSaturation(value):
    camera.saturation = int(value)

def SetAWB(var):
    camera.awb_mode = var

def SetEFFECTS(var):
    camera.image_effect = var

def Zoom(var):
    x = float("0."+var)
    camera.zoom = (0.5,0.5,x,x)

root = tk.Tk()
root.resizable(width=False, height=False)
root.geometry("320x300+89+50")
root.title("Camera Button Test")

root.buttonframe = tk.Frame(root)
root.buttonframe.grid(row=5, column=3, columnspan=2)

tk.Button(root.buttonframe, text='Start Camera', command=CameraON).grid(row=1, column = 1)
tk.Button(root.buttonframe, text='Kill Camera', command=CameraOFF).grid(row=1, column = 2)
tk.Button(root.buttonframe, text='Exit Program', command=EXIT).grid(row=1, column = 3)

tk.Scale(root.buttonframe, from_=30, to=100, orient=tk.HORIZONTAL, label = "Brightness", command=UpdateBrightness).grid(row=2,column=1)
tk.Scale(root.buttonframe, from_=-100, to=100, orient=tk.HORIZONTAL, label = "Contrast", command=UpdateContrast).grid(row=2,column=2)
tk.Scale(root.buttonframe, from_=-100, to=100, orient=tk.HORIZONTAL, label = "Sharpness", command=UpdateSharpness).grid(row=2,column=3)
tk.Scale(root.buttonframe, from_=-100, to=100, orient=tk.HORIZONTAL, label = "Saturation", command=UpdateSaturation).grid(row=3,column=1)
tk.Scale(root.buttonframe, from_=10, to=99, orient=tk.HORIZONTAL, label = "Zoom", command=Zoom).grid(row=4,column=1)

AWB_Var = tk.StringVar(root)
AWB_Var.set(choices[0])
AWB_Option = tk.OptionMenu(root.buttonframe, AWB_Var, *choices, command=SetAWB).grid(row=3,column=2)

EFFECT_Var = tk.StringVar(root)
EFFECT_Var.set(effects[0])
EFFECT_Option = tk.OptionMenu(root.buttonframe, EFFECT_Var, *effects, command=SetEFFECTS).grid(row=3,column=3)

#enable next line to lock window in place
#root.overrideredirect(True)

root.mainloop()