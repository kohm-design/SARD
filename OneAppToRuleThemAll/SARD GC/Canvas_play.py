from tkinter import *
from PIL import Image, ImageTk

def start_draw(event):
    x1, y1 = (event.x), (event.y)
    x2, y2 = (event.x+1), (event.y+1)
    w.create_rectangle(event
