'''
This was basically a file where I could test movement for pygame.
You move a yellow box that leaves a 'blur trail' of where it has been.
I was already used to using SDL with C++, and I followed another online tutorial to help me with
more pygame features than in the video tutorial'''

import random, pygame, sys
from pygame.locals import * #To make it easier to reference all the data from pygame.locals

fps = 30 #The frame rate
colourChangeSpeed = 30 #The frames before the background cplour will change
frameCounter = 0 #To keep track of the number of frames that have passed since the last background colour 
windowWidth = 500
windowHeight = 500
pixelMovement = 1 #The initial movement of the user controlled box
boxSize = 20 #The initial size of the usrer controlled box

#The box is a 2-D list, list for top-left x cooridnates and a list for top-left y coordiantes
#These are kept so that the box will elave a trail behind it of where it has been
#The first values in each list are set so that he box wil be centred
box = [windowWidth/2 - boxSize/2,10,10,10,10],[windowWidth/2 - boxSize/2,10,10,10,10]

#Colours with (R,G,B)
grey = (100,100,100)
navyBlue = (60,60,100)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
orange = (255,128,0)
purple = (255,0,255)
cyan = (0,255,255)

colours = [grey, navyBlue, white, black, green, blue, purple, cyan] #The colours that the background will use

pygame.init()
fpsClock = pygame.time.Clock() #To keep the frame rate
displaySurface = pygame.display.set_mode((windowWidth, windowHeight), 32)
pygame.display.set_caption("Movement Test.")

while True: #The main game loop  
    displaySurface.fill(colours[0])

    #While fewer frames have elapsed than the frames needed to switch the background colour
    if frameCounter < colourChangeSpeed:
        frameCounter += 1
    else: #If the background colour needs switching
        frameCounter = 0 #No frames will have elapsed since switching
        colours.append(colours.pop(0)) #Remove the current colour from the list, but then add it to the end of the list

    #Reset the change for the box's x and y coordinates
    xChange = 0
    yChange = 0

    for event in pygame.event.get(): #Event handling loop
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
    
    keysPressed = pygame.key.get_pressed() #Store all the keys pressed

    if keysPressed[K_LEFT]:
        xChange -= pixelMovement
    if keysPressed[K_RIGHT]:
        xChange += pixelMovement
    if keysPressed[K_UP]:
        yChange -= pixelMovement
    if keysPressed[K_DOWN]:
        yChange += pixelMovement

    #Add where the new box will have moved to to the start of the list of the box's previous coordinates
    #The first x and y coordinates represent the current positions of the box
    box[0].insert(0, box[0][0] + xChange)
    box[1].insert(0, box[1][0] + yChange)
    
    if box[0][0] >= windowWidth - 10: #If the box has touched the right of the window
        box[0][0] = windowWidth - 10 #Set it back
        pixelMovement = 1 #Set he movement back
        boxSize -= 1 #Reduce the box size
    elif box[0][0] <= 0: #If the box has touched the left of the window
        box[0][0] = 0
        pixelMovement = 1
        boxSize -= 1
    if box[1][0] >= windowHeight - 10: #If the box has touched the bottom of the window
        box[1][0] = windowHeight - 10
        pixelMovement = 1
        boxSize -= 1
    elif box[1][0] <= 0: #If the box has touched the top of the window
        box[1][0] = 0
        pixelMovement = 1
        boxSize -= 1

    if boxSize == 0: #If the box has bee ndepleted fully
        boxSize = 20 #Reset it
        
        #Centre the box by addign new coordiantes
        box[0].insert(0, windowWidth/2 - boxSize/2)
        box[1].insert(0, windowHeight/2 - boxSize/2)
        #Remove coordinates to accomadtae for the new coordiantes
        box[0].pop()
        box[1].pop()
        
        pygame.draw.rect(displaySurface, red, (box[0][0], box[1][0], boxSize, boxSize)) #Draw the box in red
        pygame.display.update()
        pygame.time.wait(1000) ##Wait a second before the user can ragain control

    if (xChange == 0) & (yChange == 0): #If the user hasn't moved the box (xChange & yChange are only assigned from 0 during movement)
        pixelMovement = 1 #Reset the velocity of the box
    else:
        pixelMovement += 1 #If the user has kept input, increase the velocity of the box
        

    if len(box[0]) > 1: #Delete the last items in the list to accomodate for the new cooridnates added, so that the trial doesn't go on forever
        box[0].pop()
        box[1].pop()

    #Draw the trail (of boxes with decreasing transparency from the actual box)
    for x in range(len(box[0]) - 1, 0, -1):
        rect = pygame.Surface((boxSize, boxSize), pygame.SRCALPHA, 32) #A surface with an alpha channel, so the trail can fade away
        rect.fill((255,255,0,255-(x*51))) #Base the alpha value after how previous the coordinates being used where the main coordiantes
        displaySurface.blit(rect, (box[0][x], box[1][x])) #Display the box for the trail

    pygame.draw.rect(displaySurface, yellow, (box[0][0], box[1][0], boxSize, boxSize)) #Draw the main box
    
    pygame.display.update() #Updte the screen
    fpsClock.tick(fps) #Handle the frame rate
