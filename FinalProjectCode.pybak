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
  direction = choosePath(2)
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
    
def areaThree():
  showInformation("There's a trap door directly in front of you.")
  showInformation("Or you can walk further ahead and see what lies ahead.")
  showInformation("1. Take the trap door. \n2. Keep walking. ")
  direction = choosePath(2)
  if (direction == 1):
    # Go back to areaOne
    showInformation("You chose the trap door.")
    areaOne()
  elif (direction == 2):
    # Walk into areaFour
    showInformation("Keep walking, see what mistery lies ahead.")
    areaFour()

def areaFour():
  showInformation("There's something shiny over yonder, go take a look and see what it is.")
  showInformation("Oh wait, those are Kramer's Jewels next to that door")
  showInformation("1. Take the trap door. \n2. Take Kramer's jewels. ")
  direction = choosePath(2)
  if (direction == 1):
    # Go back to areaOne
    showInformation("You chose the trap door.")
    areaOne()
  elif (direction == 2):
    # Walk into areaFour
    showInformation("Keep walking, see what mistery lies ahead.")
    areaFour()

def areaFive():
  showInformation("Leaves cover the ground and a fire can be seen to the north. \nA coffin rests nearby.")
  showInformation("You see two leaves on the ground, but you also can't stop thinking about the fire.")
  showInformation("This leaves you with three options: \n1. Head north towards the fire. \n2. Pick up the red leaf. \n3. Pick up the green leaf.")
  direction = choosePath(3)
  if (direction == 1):
    showInformation("You head north towards the fire. It looks so inviting.")
    areaSix()
  elif (direction == 2):
    #rosecolored glasses function
    #showpic
    showInformation("You pick up the red leaf, and the world starts to look a little silly.")
    areaThree()
  elif (direction == 3):
    #negative function
    #showpic
    showInformation("You pick up the green leaf, and the world turns stark.")
    areaNine()
    
def areaSix():
  showInformation("The fire nearby provides warmth against the cold air.")
  showInformation("To the north of the fire lies a treasure trove. Will you pick up a piece of treasure? Y/N?")
  string = raw_input("> ")
  lcstr  = string.lower()
  if (lcstr == 'y'):
    showInformation("You take the treasure, and nothing appears to happen. \nYou head through the trap door.")
    areaEight()
  elif (lcstr == 'n'):
    showInformation("You ignore the treasure, leaving yourself with other options.")
    showInformation("1. The fire is attracting the attention of wildlife. You may put it out. \n2. You may go through the trap door. \n3. You may pass through and head west.")
    direction = choosePath(3)
    if (direction == 1):
      #darkenUp
      #showpic
      showInformation("You can no longer find the trap door. Your only option is to head west.")
      areaSeven()
    elif (direction == 2):
      showInformation("You open the trap door, and slowly climb in.")
      areaFour()
    elif (direction == 3):
      showInformation("You head west, admiring the greenery.")
      areaSeven()
  else:
    printNow("That's not a valid entry.")
  return
  
def areaSeven():
  #showpic
  showInformation("You enter a labyrinthine hallway, turning a corner. \nWould you like to continue on or go back?")
  showInformation("1. Continue on. \n2. Go back.")
  direction = choosePath(2)
  if (direction == 1):
    showInformation("You have chosen to continue on.")
    areaEight()
  elif (direction ==2):
    showInformation("You have chosen to return the way you came.")
    areaSix()
    
def areaEight():
  #showpic
  showInformation("Looking around, you see an enclosed area, with a golden door. Next to that is a pathway up the coast.")
  showInformation("A trap door stands open slightly south of a you, with the ocean directly to your west.")
  showInformation("You have some hard choices to make, my dear. \n1. Walk up to the golden door. \n2. Go through the trap door. \n3. Walk up the coast. \n4. You're thirsty. Go to the ocean.")
  direction = choosePath(4)
  if (direction == 1):
    showInformation("You walk up to the golden door, and try to push it open. \nIt appears you need a key of sorts.")
    #global variable if key was picked up in area six
    #if key = yes
      #door opens
      #area10
    #if key = no
      #door stays closed
      #area8
  elif (direction == 2):
    showInformation("You go through the trap door quickly and quietly.")
    areaTwo()
  elif (direction == 3):
    showInformation("You take a walk up the coast, admiring the scenery as you go.")
    areaNine()
  elif (direction == 4):
    #doublemirror function
    #showpic
    showInformation("Drinking from the ocean might have been a bad idea. What was in that water?")
    showInformation("You stumble away, tripping through the trap door.")
    areaSix()

def areaNine():
  #showpic
  showInformation("This is the creepiest area you've seen by far. Coffins cover a small cliffside, two appearing to be open.")
  #if you have treasure from area four
    #YOU KILLED MUHFUKKKAAA
  #else:
    showInformation("What would you like to do? \n1. Climb to the higher open coffin. \n2. Scramble to the lower coffin. \n3. Walk back down along the coast.")
    direction = choosePath(3)
    if (direction == 1):
      #vertmirror
      #showpic
      showInformation("You expend too much energy getting to the higher coffin. Dizziness washes over you and you fall in.")
      areaFive()
    elif (direction == 2):
      #sepia
      #showpic
      showInformation("Your vision blurs slightly as you make it up, crawling into the lower coffin.")
      areaFour()
    elif (direction == 3):
      showInformation("You walk down the coastline, sticking close to the ocean.")
      areaEight()
      
def areaTen():
  #showpic
  showInformation("You've made it to the end!")
  showInformation("It's time for Miss Malice to go home.")
  showInformation("We'll see you soon, I'm sure.")

# Insert photos

# Photo Functions
#
# Makes the picture more blue.
def moreBlue(per):
  for pix in pixels:
    b = getBlue(pix)
    setBlue(pix, b + b * per * .01)

# Makes the picture more red.   
def moreRed(per):
  for pix in pixels:
    r = getRed(pix)
    setRed(pix, r + r * per * .01)

# Makes the picture more purple.    
def morePurple(per):
  for pix in pixels:
    r = getRed(pix)
    b = getBlue(pix)
    setRed(pix, r + r * per *.01)
    setBlue(pix, b + b * per * .01)

#Makes the picture more green.    
def moreGreen(per):
  for pix in pixels:
    g = getGreen(pix)
    setGreen(pix, g + g * per * .01)
    
def vertMirror(picture):
    for x in range(0, getWidth(picture) / 2):
      for y in range(0, getHeight(picture)):
        leftpix = getPixel(picture, x, y)
        rightpix = getPixel(picture, getWidth(picture) - x - 1, y)
        reflect = getColor(leftpix)
        setColor(rightpix, reflect)
    repaint(picture)