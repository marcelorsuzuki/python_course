##
# This module simulate the enviroment "Code Skulptor" (www.codeskulptor.org). Here is used "Tkinter" to make
# the Frames, Buttons, etc.
# I developed this module just to test my codes local, in my computer, when I don't have internet conection.
#
# @author: Marcelo Suzuki
#
from Tkinter import *  

##
# Crate a "FrameSimple" object
#
# @param title: Title to Frame
# @param width: Frame width
# @param height: Frame height
#     
def create_frame(title, width, height):
    
    # create a root window
    root = Tk()
    root.title(title)
    root.geometry(str(width) + "x" + str(height))
    
    # create a frame in the window to hold other widgets
    app = Frame(root)
    app.pack()
    
    return FrameSimple(app)

##
# Class that represent a Frame object
class FrameSimple:

    __app = None
    
    ##
    # Constructor
    def __init__(self, app):
        self.__app = app

    ##
    # Add a Button in a Frame object
    def add_button(self, title, handle, w):
        button = Button(self.__app, text = title, command = handle, width = w)
        button.pack()

    ## 
    # Add a Textbox in a Frame object, with a Label object
    def add_input(self, title, handler, w):
        label = Label(self.__app, text = title)
        label.pack()
        
        text = Text(self.__app, width = w, height = 2)
        text.pack()

    ## 
    # Add a Textbox in a Frame object, with a Label object
    def add_label(self, title, handler, w):
        label = Label(self.__app, text = title)
        label.pack()

    ##
    # Start a frame object
    def start(self):
        mainloop()
    