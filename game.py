# Modules
import tkinter
import time
import random
import ballclass
import paddleclass

# Initilization
tk = tkinter.Tk()
tk.title('Game')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = tkinter.Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness = 0)
canvas.pack()
tk.update()

playerPaddle = paddleclass.Paddle(canvas, 'blue')
ball = ballclass.Ball(canvas, playerPaddle, 'red')

# Animation
while 1:
    if ball.hitBottom == False:
        playerPaddle.draw()
        ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)


