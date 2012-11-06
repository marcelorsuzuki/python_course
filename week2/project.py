# http://www.codeskulptor.org/#user4-M5cZ9q9T89-28.py

# Template for "Guess the target" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import math
import random

# initialize global variables used in your code
target = 0
try_number = 0
max_num = 100
inp = None

# define event handlers for control panel  
def range100():
    global max_num
    max_num = 100
    start()

def range1000():
    global max_num
    max_num = 1000
    start()
    
def start():
    global target, try_number, max_num
    target = random.randrange(0, max_num)
    try_number = math.ceil(math.log(max_num + 1, 2))
    print
    print "Try to guess the number between 0 and " + str(max_num) + " in " + str(try_number) + " attempts."
    inp.set_text("")
    
def get_input(guess):
    global try_number, inp
    
    if (target == int(guess)):
        print "Yes, you guessed the number " + str(target) + ". You win!"
        print
        start()
    else:
        try_number -= 1
        if (try_number == 0):
            print "Sorry, you didn't guess the number. You lost. The number was " + str(target)
            start(100)
        if (target > int(guess)):
            print "The number is HIGHER then you chose. You have " + str(try_number) + " attempts."
        elif (target < int(guess)):
            print "The number is LOWER then you chose. You have " + str(try_number) + " attempts."
            
    inp.set_text("")

    
# create frame
frame = simplegui.create_frame("Guess the number", 300, 300)

# register event handlers for control elements
frame.add_button("Run", start, 100)
frame.add_button("Game [0-100]", range100, 100)
frame.add_button("Game [0-1000]", range1000, 100)
inp = frame.add_input("Guess...", get_input, 200)

# start frame
frame.start()

# always remember to check your completed program against the grading rubric
