
from p5 import *



def my_setup():
    size(1200,1200)





def my_draw():
        background(50, 50, 99)
        translate(mouse_x, mouse_y)
        fill(mouse_x, mouse_y/2, mouse_x/3)
        stroke(180, 150, 0)
        stroke_weight(2)
        begin_shape()
        vertex(0, -50)
        vertex(14, -20)
        vertex(47, -15)
        vertex(23, 7)
        vertex(29, 40)
        vertex(0, 25)
        vertex(-29, 40)
        vertex(-23, 7)
        vertex(-47, -15)
        vertex(-14, -20)
        end_shape("CLOSE")


if __name__ == '__main__':
    run(sketch_setup=my_setup, sketch_draw=my_draw)    