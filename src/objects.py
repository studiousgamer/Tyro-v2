import tkinter as tk
from tkinter import ttk
import PIL
from PIL import Image as img, ImageTk
import json



class CanvasObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        if self.type == "image":
            self.image = img.open(self.path)
            self.image = self.image.resize((int(self.width*self.scale), int(self.height*self.scale)), PIL.Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(self.image)
            self.root.image = self.image
    
    def moveX(self, x):
        self.x += x
    
    def moveY(self, y):
        self.y += y
    
    def changeWidth(self, width):
        self.width = width
    
    def changeHeight(self, height):
        self.height = height
    
    def changeScale(self, scale):
        self.scale = scale
        
    def draw(self, canvas):
        if self.type == "image":
            canvas.create_image(self.x, self.y, image=self.image, anchor="nw")
        elif self.type == "text":
            canvas.create_text(self.x, self.y, text=self.text, font=(self.font, self.fontSize), fill=self.fill, anchor="nw")
        elif self.type == "rectangle":
            canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.fill)
        elif self.type == "ellipse":
            canvas.create_oval(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.fill)
        elif self.type == "line":
            canvas.create_line(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.fill)