

import pgzrun
from random import randint

WIDTH = 300
HEIGHT = 200

def draw():
    r = 0
    g = 255
    b = randint(110,200)

    width = WIDTH -100
    height = HEIGHT +100
    
    for i in range(2):
        circle = Circle((0,0),(width,height))
        circle.center = 150 , 150
        screen.draw.rect(rect,(r,g,b))

    
    


        

    
pqzrun.go()

        