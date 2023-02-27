# Imports go at the top
from microbit import *
import random

#your position
x = 2
y = 4

# object position
OBJ_X = random.randint(0,4)
OBJ_Y = random.randint(0,4)

score = 0

while True:
    #when moving the mircrobit
    if accelerometer.is_gesture('left'):
        x -= 1
    if accelerometer.is_gesture('right'):
        x += 1
    if accelerometer.is_gesture('down'):
        y += 1 
    if accelerometer.is_gesture('up'):
        y -= 1

    if x == -1:
        x = 0
    if x == 5:
        x = 4
    if y == -1:
        y = 0
    if y == 5:
        y = 4

    #when you hit the object
    if OBJ_X == x and OBJ_Y == y: 
        score += 1
        OBJ_X = random.randint(0,4)
        OBJ_Y = random.randint(0,4)

    display.set_pixel(x, y, 9) #show your location
    display.set_pixel(OBJ_X, OBJ_Y, 6) #show object's location
    # the value of sleep can control how fast the bit move.
    # lower the value the bit will move further
    sleep(300)
    display.clear()
    
    if button_a.was_pressed(): #end games
        break
        
display.scroll(score)
reset()
