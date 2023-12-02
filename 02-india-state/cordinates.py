from turtle import Turtle, Screen
import pandas as pd

t = Turtle()
s = Screen()

IMG = "india_map.gif"

def get_mouse_click_coor(x, y):
    print(x, y)

s.setup(width=655, height=750)
s.screensize(canvwidth=600, canvheight=700)
s.addshape(IMG)
t.shape(IMG)


s.onscreenclick(get_mouse_click_coor)


s.mainloop()
