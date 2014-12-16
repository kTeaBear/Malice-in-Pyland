# The Adventures of Malice in Py-Land
# CST205 Final Project
# Team Members: Caitlin Kuleck
#               Luciano Avendano
# 12/15/2014

#Global variables

# Main program

def welcome():
  showInformation("Welcome to Py-Land Miss Malice!")
  showInformation("We are pleased to have you here, whether you want to be here or not.")
  showInformation("If you complete our labyrinth, I suppose we MIGHT let you go.")
  showInformation("Are you ready to start?")
  showInformation("No? Good thing that was a rhetorical question! Let's go!")
  
def choosePath(numOfPaths):
    choice = 0
    while (choice < 1 or choice > numOfPaths):        
        choice = raw_input("> ")
        if (choice != '1' and choice != '2' and choice != '3' and choice != '4'):
            choice = 0
        elif (choice == '1' or choice == '2' or choice == '3' or choice == '4'):
            choice = int(choice) 
        else:
           print('Select a path from 1 to ' + str(numOfPaths) + ' > ')  
    print("")
    return choice
  
def startingArea():
  showInformation("You start off in the center of a checkboard hallway.")
  showInformation("1. Will you go to the right? \n2. Will you go to the left?")
  direction = choosePath(2)
  if (direction == 1):
    showInformation("You have chosen the rightbound path.")
    areaTwo()
  elif (direction == 2):
    showInformation("You have chosen the leftbound path.")
    areaOne()
    
def areaOne():
  showInformation("At the end of the hallway, you see a trap door. \nOn top of the trap door are two pill packets.")
  showInformation("Which pill will you take? \n1. The red pill. \n2. The blue pill.")
  #take integer
  direction = choosePath(2)
  if (direction == 1):
    #moreRed function
    #showPic
    showInformation("Your surroundings have changed. You must continue through the trap door.")
    areaFive()
  elif (direction == 2):
    #moreBlue function
    #showPic
    showInformation("You surroundings have changed. You must continue through the trap door.")
    areaThree()

def areaTwo():
  showInformation("At the end of the hallway, you see an enclosed area with an oddly shaped tree. \nUnderneath the tree is a strangely shaped opening.")
  showInformation("Hanging in front of the opening are two packets of pills. Which will you take?")
  showInformation("1. The green pill. \n2. The purple pill.")
  #take integer
  if (direction == 1):
    #moreGreen function
    #showPic
    showInformation("You take the green pill, and the world looks a little strange. \nYou enter the tree.")
    areaFour()
  elif (direction == 2):
    #morePurple function
    #showPic
    showInformation("You take the purple pill, and the world looks a little strange. \nYou enter the tree.")
    areaEight()

# Insert photos

# Photo Functions