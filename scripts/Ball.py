from tkinter import *;
import random;
import time;

class Ball:
    def __init__(self, canvas, paddle,color):
        self.canvas = canvas;
        self.paddle = paddle;
        self.hitBottom = False;
        self.id = canvas.create_oval(10,10,25,25, fill = color);
        self.canvas.move(self.id, 245, 100);
        startX = list(range(-3,4));
        startX.remove(0);
        random.shuffle(startX);
        self.x = startX[0];
        self.y = -3;
        self.canvasHeight = self.canvas.winfo_height();
        self.canvasWidth = self.canvas.winfo_width();

    def draw(self):
        self.canvas.move(self.id, self.x, self.y);
        pos = self.canvas.coords(self.id);
        if(pos[1] <= 0):
            self.y = 2;
        if(pos[3] >=  self.canvasHeight):
            self.y = -2;
            self.hitBottom = True;
        if(self.hitPaddle(pos)):
            self.y = -3;
        if(pos[0] <= 0):
            self.x = 2;
        if(pos[2] >= self.canvasWidth):
            self.x = -2;
    def hitPaddle(self, pos):
        paddlePos = self.canvas.coords(self.paddle.id);
        if(pos[2] >= paddlePos[0] and pos[0] <= paddlePos[2]):
            if(pos[3] >= paddlePos[1] and pos[3] <= paddlePos[3]):
                return True;
        return False;






