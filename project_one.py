# Imports the dependency
from microbit import *
import random

# your initial position at (2,4)
x = 2
y = 4

# random target object position 
OBJ_X = random.randint(0,4)
OBJ_Y = random.randint(0,4)

# initialize score to zero
score = 0

# start of the infinite loop
while True:
    # move microbit according the accelerometer guesture. 
    # NOTE: (0,0) is top left corner.  Therefore, "Down" gesture means y increasing
    if accelerometer.is_gesture('left'):
        x -= 1
    if accelerometer.is_gesture('right'):
        x += 1
    if accelerometer.is_gesture('down'):
        y += 1 
    if accelerometer.is_gesture('up'):
        y -= 1

    # if user object move to boundary, it will stay there without going beyond.
    if x == -1:
        x = 0
    if x == 5:
        x = 4
    if y == -1:
        y = 0
    if y == 5:
        y = 4

    # increase the score when you hit the object and generate a new object position
    if OBJ_X == x and OBJ_Y == y: 
        score += 1
        OBJ_X = random.randint(0,4)
        OBJ_Y = random.randint(0,4)

    display.set_pixel(x, y, 9) # show your location (with brighter dot)
    display.set_pixel(OBJ_X, OBJ_Y, 6) # show object's location (with lighter dot)
    # the value of sleep can control how fast the bit move.
    # lower the value the bit will move further
    sleep(300)
    display.clear()
    
    # end games if button A is pressed
    if button_a.was_pressed(): 
        break

# display the score if the game ends (breaking the infinite loop)
display.scroll(score)
reset()
