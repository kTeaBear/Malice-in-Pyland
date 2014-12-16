#collection of picture edits

def roseColoredGlasses():
  for pix in pixels:
    r = getRed(pix)
    g = getGreen(pix)
    b = getBlue(pix)
    setRed(pix, r * .93)
    setGreen(pix, g * .07)
    setBlue(pix, b * .54)
  repaint(pic)
  
def makeNegative():
  for pix in pixels:
    r= getRed(pix)
    g = getGreen(pix)
    b = getBlue(pix)
    invertColor = makeColor(255 - r, 255 - g, 255 - b)
    setColor(pix, invertColor)
  repaint(pic)

def betterBnW():
  for pix in pixels:
    r= getRed(pix)
    g = getGreen(pix)
    b = getBlue(pix)
    luminance = (r * 0.299 + g * 0.587 + b * 0.114)
    setColor(pix, makeColor(luminance))
  repaint(pic)
  
def vertMirror(picture):
  for x in range(0, getWidth(picture) / 2):
    for y in range(0, getHeight(picture)):
      leftpix = getPixel(picture, x, y)
      rightpix = getPixel(picture, getWidth(picture) - x - 1, y)
      reflect = getColor(leftpix)
      setColor(rightpix, reflect)
  repaint(picture)
  
def darkenUp():
  for pix in pixels:
    oldColor = getColor(pix)
    newColor = makeDarker(oldColor)
    setColor(pix, newColor)
    
def moreBlue(per):
  for pix in pixels:
    b = getBlue(pix)
    setBlue(pix, b + b * per * .01)
    
def moreRed(per):
  for pix in pixels:
    r = getRed(pix)
    setRed(pix, r + r * per * .01)
    
def morePurple(per):
  for pix in pixels:
    r = getRed(pix)
    b = getBlue(pix)
    setRed(pix, r + r * per *.01)
    setBlue(pix, b + b * per * .01)
    
def moreGreen(per):
  for pix in pixels:
    g = getGreen(pix)
    setGreen(pix, g + g * per * .01)
    
def makeSepia(picture):
  # Makes pictures look old,
  newPic = makeEmptyPicture(getWidth(picture), getHeight(picture))
  newPic = betterBnW(picture)
  # Set beginning and ending for X and Y ranges
  beginX = 0
  beginY = 0
  endX = getWidth(picture)
  endY = getHeight(picture)
  stepY = 1
  stepX = 1
 
  # Loop from left to right side
  for x in range(beginX, endX, stepX):
    for y in range(beginY, endY, stepY):
      # Get pixels and make faded
      # If/Else statements to determine fading and color
      picPix = getPixel(newPic, x, y)
      r = getRed(picPix)
      if (r < 63):
        redMult = 1.1
        blueMult = 0.9
      elif (r > 62 and r < 192):
        redMult = 1.15
        blueMult = 0.85
      else:
        redMult = 1.08
        blueMult = 0.93
      b = getBlue(picPix)
      g = getGreen(picPix)
      newRed = min((r * redMult), 255)
      newBlue = b * blueMult
      setColor(picPix,makeColor(newRed, g, newBlue))
  return newPic
  
  def doubleMirror(picture):
  for x in range(0, getWidth(picture) / 2):
    for y in range(0, getHeight(picture)):
      leftpix = getPixel(picture, x, y)
      rightpix = getPixel(picture, getWidth(picture) - x - 1, y)
      reflect = getColor(leftpix)
      setColor(rightpix, reflect)
  for x in range(0, getWidth(picture)):
    for y in range(0, getHeight(picture) / 2 ):
      pix = getPixel(picture, x, y)
      color = getColor(pix)
      reflect = getPixel(picture, x, getHeight(picture) - 1 - y)
      setColor(reflect, color)
  repaint(picture)