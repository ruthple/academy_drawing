from p5 import *



def setup():
    size(600,600)
    
    fill(5, 0, 99)
    background(0, 0, 199)


def draw():
    
    #background(0, 0, 99)
    
    if mouse_is_pressed:
        stroke_weight(0.5)
        stroke(mouse_x, mouse_y, 50)

    else:
        # stroke_weight(5)
        # stroke(50, 50, 99)
        background(50,50,99)
  

    line((mouse_x - 40, mouse_y), (mouse_x + 40, mouse_y))
    line((mouse_x, mouse_y - 40), (mouse_x, mouse_y + 40))
    line((mouse_x- 30, mouse_y - 30),(mouse_x + 30, mouse_y + 30))
    line((mouse_x - 30, mouse_y + 30), (mouse_x + 30, mouse_y - 30))

    
   



if __name__ == '__main__':
    run()