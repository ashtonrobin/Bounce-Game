# Modules
import tkinter
import time
import random
import ballclass

# Initilization
tk = tkinter.Tk()
tk.title('Game')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = tkinter.Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness = 0)
canvas.pack()
tk.update()

# Object creation
ball = ballclass.Ball(canvas, 'red')

#Animation
while 1:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
