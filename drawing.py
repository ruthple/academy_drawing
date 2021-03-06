from p5 import *

window_height = 640
window_width = 360


def my_setup():
    size(window_width, window_height)
    stroke(255)


def my_draw():
    background(0)
    y = window_height * 0.5
    line((0, y), (window_width, y))
    circle(window_width*0.5, window_height*0.5, 100)


if __name__ == '__main__':
    run(sketch_setup=my_setup, sketch_draw=my_draw)
