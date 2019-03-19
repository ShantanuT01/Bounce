from tkinter import *;
import random;
import time;

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas;
        self.id = canvas.create_rectangle(0,0,100,10,fill=color);
        self.canvas.move(self.id, 200, 300);
        self.x = 0;
        self.canvasWidth = self.canvas.winfo_width();
    def draw(self):
        pass;
