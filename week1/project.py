# http://www.codeskulptor.org/#user2-urSPV2fmJzphdNG-1.py

# Rock-paper-scissors-lizard-Spock mini projet

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors


# imports

import random


# helper functions

### This function receive a target between 0 and 4, and return a relative string name ###
  
def number_to_name(target):
    
    name = "rock"
    
    if target == 1:
        name = "Spock"

    if target == 2:
        name = "paper"

    if target == 3:
        name = "lizard"

    if target == 4:
        name = "scissors"
        
    return name
        
    
### This function receive a name and return a relative target between 0 and 4 ###
    
def name_to_number(name):

    target = 0
    
    if name == "Spock":
        target = 1

    if name == "paper":
        target = 2
        

    if name == "lizard":
        target = 3
        

    if name == "scissors":
        target = 4
        
    return target


### This function receive a name play with a computer by a random choose, and show the winnter ###

def rpsls(name): 

    # get the target to player and to computer    
    player_number = name_to_number(name)
    comp_number = random.randrange(0, 5)

    # calculate
    result = (player_number - comp_number + 5) % 5

    # test the result
    if (result == 0):
        result = "Player and computer tie!"
    elif (result  < 3):
        result = "Player wins!"
    else:
        result = "Computer wins!"

    comp_name = number_to_name(comp_number)
    
    # show the results
    print "Player chooses " + name
    print "Computer chooses " + comp_name
    print result
    print
    

# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


