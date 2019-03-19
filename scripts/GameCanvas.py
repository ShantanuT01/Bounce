from tkinter import *;
import random;
import time;
from scripts import Ball;
from Ball import Ball;
from scripts import Paddle;
from Paddle import Paddle;


tk = Tk();
tk.title("Game");
tk.resizable(0,0);
tk.wm_attributes("-topmost", 1);
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0);
canvas.pack();
tk.update();
paddle = Paddle(canvas, 'blue');
ball = Ball(canvas, paddle,'red');


def main():
    while not ball.hitBottom:
        ball.draw();
        paddle.draw();
        tk.update_idletasks();
        tk.update();
        time.sleep(0.01);


main();