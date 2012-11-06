# http://www.codeskulptor.org/#user4-h5j1Icp53ZQg0ZR-1.py

# Canvas and Drawing
# Structure


# The draw handler allows the user to draw things on the 
#    canvas. Make sure you read all the way to the end of the
#    program to find out how to register a function as the
#    draw handler.

import simplegui

# The draw method is a type of event handler. It takes 
#    exactly one parameter, commonly called the canvas. The
#    canvas can be passed as a parameter to other methods, 
#    if needed.
        
def draw(canvas):

    # Draw two circles with radius 20 and white lines of width 10. One is centered at (90,200) and one at (210,200).
    # Draw a red line of width 40 from (50,180) to (250,180).
    # Draw two red lines of width 5 from (55,170) to (90,120) and from (90,120) to (130,120).
    # Draw a red line of width 140 from (180,108) to (180,160).
    
    canvas.draw_circle((90,200), 20, 10, "White")
    canvas.draw_circle((210,200), 20, 10, "White")
    canvas.draw_line((50,180), (250,180), 40, "Red")
    canvas.draw_line((55,170), (90,120), 5, "Red")
    canvas.draw_line((90,120), (130,120), 5, "Red")
    canvas.draw_line((180,108), (180,160), 140, "Red")
    

# Frame

frame = simplegui.create_frame("Draw", 300, 300) 
frame.set_draw_handler(draw)
frame.start()