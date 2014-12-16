# The Adventures of Malice in Py-Land
# CST205 Final Project
# Team Members: Caitlin Kuleck
#               Luciano Avendano
# 12/15/2014

# Global variables need to be set so functions
# can access the objects stored in them.
weapon = 0
item = 0
gameOver = 0
imgPath='/home/avendanl/My_SVN_Repo/CSIT-CST205/CST205-Final-Project/trunk/'

# Main program

def welcome():
  showInformation("Welcome to Py-Land Miss Malice! \nWe are pleased to have you here, whether you want to be here or not. \nIf you complete our labyrinth, I suppose we MIGHT let you go. \nAre you ready to start? \nNo? Good thing that was a rhetorical question! Let's go! \nType start to begin this journey.")
  
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

s1=makePicture(imgPath + 'Images/Starting_Area.jpg')
def startingArea():
  show(s1)
  showInformation("You start off in the center of a checkboard hallway. \n\n1. Will you go to the right? \n2. Will you go to the left?")
  direction = choosePath(2)
  if (direction == 1):
    showInformation("You have chosen the rightbound path.")
    areaTwo()
  elif (direction == 2):
    showInformation("You have chosen the leftbound path.")
    areaOne()

a1=makePicture(imgPath + 'Images/Area_One.jpg')    
def areaOne():
  show(a1)
  showInformation("At the end of the hallway, you see a trap door and a sign, \"You must take one pill, or you will never leave this place\". \nOn top of the trap door are two pill packets.")
  showInformation("Which pill will you take? \n1. The red pill. \n2. The blue pill.")
  direction = choosePath(2)
  if (direction == 1):
    #moreRed function
    moreRed(a1)
    showInformation("Your surroundings have changed. You must continue through the trap door.")
    areaFive()
  elif (direction == 2):
    #moreBlue function
    moreBlue(a1)
    showInformation("You surroundings have changed. You must continue through the trap door.")
    areaThree()
    
a2=makePicture(imgPath + 'Images/Area_Two.jpg')
def areaTwo():
  show(a2)
  showInformation("At the end of the hallway, you see an enclosed area with an oddly shaped tree. \nUnderneath the tree is a strangely shaped opening.")
  showInformation("Hanging in front of the opening are two packets of pills. Which will you take?")
  showInformation("1. The green pill. \n2. The purple pill.")
  direction = choosePath(2)
  if (direction == 1):
    #moreGreen function
    moreGreen(a2)
    showInformation("You take the green pill, and the world looks a little strange. \nYou enter the tree.")
    areaFour()
  elif (direction == 2):
    #morePurple function
    morePurple(a2)
    showInformation("You take the purple pill, and the world looks a little strange. \nYou enter the tree.")
    areaEight()
    
a3=makePicture(imgPath + 'Images/Area_Three.jpg')    
def areaThree():
  show(a3)
  showInformation("There's a trap door directly in front of you. \nOr you can walk further ahead and see what lies ahead.")
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
    
a4=makePicture(imgpath + 'Images/Area_Four.jpg')
hand=makePicture(imgpath + 'Images/KramersHand.png')
def areaFour():
  global item
  show(a4)
  showInformation("There's something shiny over yonder, go take a look and see what it is. \nOh wait, its Kramer's Hand statue next to that door.")
  showInformation("1. Take the trap door. \n2. Keep walking. \n3. Take Kramer's Hand.")
  direction = choosePath(3)
  if (direction == 1):
    # Go back to areaOne
    showInformation("You chose the trap door.")
    areaOne()
  elif (direction == 2):
    # Walk into areaFour
    showInformation("Keep walking, see what mistery lies ahead.")
    areaFour()
  elif (direction == 3):
    # Take jewels
    show(hand)
    showInformation("You took Kramer's Hand! It might come in 'handy'.")
    vertMirror(a4)
    item = 1
    areaTwo()

a5=makePicture(imgpath + 'Images/Area_Five.jpg')        
def areaFive():
  show(a5)
  showInformation("Leaves cover the ground and a fire can be seen to the north. \nA coffin rests nearby. \nYou see two leaves on the ground, but you also can't stop thinking about the fire.")
  showInformation("This leaves you with three options: \n1. Head north towards the fire. \n2. Pick up the red leaf. \n3. Pick up the green leaf.")
  direction = choosePath(3)
  if (direction == 1):
    showInformation("You head north towards the fire. It looks so inviting.")
    areaSix()
  elif (direction == 2):
    showInformation("You pick up the red leaf, and the world starts to look a little silly.")
    #rosecolored glasses function
    roseColoredGlasses(a5)
    areaThree()
  elif (direction == 3):
    showInformation("You pick up the green leaf, and the world turns stark.")
    #negative function
    makeNegative(a5)
    areaNine()

a6=makePicture(imgpath + 'Images/Area_Six.jpg')    
def areaSix():
  global item
  show(a6)
  showInformation("The fire nearby provides warmth against the cold air.")
  showInformation("To the north of the fire lies a treasure trove. Will you pick up a piece of treasure? Y/N?")
  string = raw_input("> ")
  lcstr  = string.lower()
  if (lcstr == 'y'):
    showInformation("You take the treasure, and nothing appears to happen. \nYou head through the door next to the treasure.")
    item = 2
    areaEight()
  elif (lcstr == 'n'):
    showInformation("You ignore the treasure, leaving yourself with other options. \n1. The fire is attracting the attention of wildlife. You may put it out. \n2. You may go through the trap door. \n3. You may pass through and head west.")
    direction = choosePath(3)
    if (direction == 1):
      showInformation("You can no longer find the trap door. Your only option is to head west.")
      darkenUp(a6)
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

a7=makePicture(imgpath + 'Images/Area_Seven.jpg')    
def areaSeven():
  show(a7)
  showInformation("You enter a labyrinthine hallway, turning a corner. \nWould you like to continue on or go back?")
  showInformation("1. Continue on. \n2. Go back.")
  direction = choosePath(2)
  if (direction == 1):
    showInformation("You have chosen to continue on.")
    areaEight()
  elif (direction ==2):
    showInformation("You have chosen to return the way you came.")
    areaSix()
    
door=makePicture(imgpath + 'Images/goldenDoor.jpg')    
def areaEight():
  show(a8)
  showInformation("Looking around, you see an enclosed area, with a golden door. Next to that is a pathway up the coast.")
  showInformation("A trap door stands open slightly south of a you, with the ocean directly to your west.")
  showInformation("You have some hard choices to make, my dear. \n1. Walk up to the golden door. \n2. Go through the trap door. \n3. Walk up the coast. \n4. You're thirsty. Go to the ocean.")
  direction = choosePath(4)
  if (direction == 1):
    showInformation("You walk up to the golden door, and try to push it open. \nIt appears you need a key of sorts or maybe the fingers from a hand statue will do.")
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

a9=makePicture(imgpath + 'Images/Area_Nine-HangingCoffins.jpg')
def areaNine():
  show(a9)
  showInformation("This is the creepiest area you've seen by far. Coffins cover a small cliffside, two appearing to be open. But wait! MooFakka jumps out demanding some kind of payment if you want to get home.")
  # if you have treasure from area six
  if (item == 2):
    # Use your jewels to pay MooFakka so he can send you home
    if (item == 2):
      showInformation("You currently have some jewels from the treasure trove")
      showInformation("Would you like to give them to MooFakka? Y/N")
      string = raw_input("> ")
      lcStr = string.lower()
      if (lcStr == 'y'):
        showInformation("\"As a beast of my word, I shall send you back home where you came from...")
        areaTen()
      elif (lcStr == 'n'):
        showInformation("\"Well, its back to the beginning for you. Next time, think twice about taking things that don't belong to you.\"")
        areaOne()
      else:
        printNow("That is not a valid choice. Y/N")
  else:
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

a10=makePicture(imgpath + 'Images/Area_Ten.jpg')            
def areaTen():
  global gameOver
  show(a10)
  showInformation("You've made it to the end! \nIt's time for Miss Malice to go home. \nWe'll see you soon, I'm sure.")
  gameOver = 1
  
# Insert photos

# Photo Functions
#
# Makes the picture more blue.
def moreBlue(picture):
  pixels = getPixels(picture)
  for pix in pixels:
    b = getBlue(pix)
    setBlue(pix, b + b * 80 * .01)
  repaint(picture)
  
# Makes the picture more red.   
def moreRed(picture):
  pixels = getPixels(picture)
  for pix in pixels:
    r = getRed(pix)
    setRed(pix, r + r * 80 * .01)
  repaint(picture)
  
# Makes the picture more purple.    
def morePurple(picture):
  pixels = getPixels(picture)
  for pix in pixels:
    r = getRed(pix)
    b = getBlue(pix)
    setRed(pix, r + r * 80 *.01)
    setBlue(pix, b + b * 80 * .01)
  repaint(picture)
  
#Makes the picture more green.    
def moreGreen(picture):
  pixels = getPixels(picture)
  for pix in pixels:
    g = getGreen(pix)
    setGreen(pix, g + g * 80 * .01)
  repaint(picture)
    
# Split image vertically and mirror    
def vertMirror(picture):
    for x in range(0, getWidth(picture) / 2):
      for y in range(0, getHeight(picture)):
        leftpix = getPixel(picture, x, y)
        rightpix = getPixel(picture, getWidth(picture) - x - 1, y)
        reflect = getColor(leftpix)
        setColor(rightpix, reflect)
    repaint(picture)

# Appears to be wearing rose colored glasses
def roseColoredGlasses(picture):
  pixels = getPixels(picture)
  for pix in pixels:
    r = getRed(pix)
    g = getGreen(pix)
    b = getBlue(pix)
    setRed(pix, r * .93)
    setGreen(pix, g * .07)
    setBlue(pix, b * .54)
  repaint(picture)

def makeNegative(picture):
  pixels = getPixels(picture)
  for pix in pixels:
    r= getRed(pix)
    g = getGreen(pix)
    b = getBlue(pix)
    invertColor = makeColor(255 - r, 255 - g, 255 - b)
    setColor(pix, invertColor)
  repaint(picture)

def darkenUp(picture):
  pixels = getPixels(picture)
  for pix in pixels:
    oldColor = getColor(pix)
    newColor = makeDarker(oldColor)
    setColor(pix, newColor)                                
  repaint(picture)
    
# Once this file is loaded into JES, the game will start
# automatically.
welcome() # Display Welcome message

while (gameOver != 1):
  string = raw_input("> ")
  lcstr = string.lower()
  #if (lcstr == "help"):
    # Print the instructions for play
    # help()
  if (lcstr == "start"):
    # Start the Adventure
    startingArea()
  elif (lcstr == "exit"):
    gameOver = 1
    printNow("Game Over!")
    printNow("The night is still young, let us play again.")
    break
  else:
    printNow("You typed: " + string)
    printNow("Try typing Help or Exit")
  break    