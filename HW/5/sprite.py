import pygame, sys #Import the pygame and sytem modules

pygame.init() #Allow pygame to initiate properly.

screen = pygame.display.set_mode([225, 150]) #The scrren object

r = pygame.Color("red") #Set the variable r to pygame's red colour
w = pygame.Color("white") #Set the variable w to pygame's white colour

frameOne = [ #The colour grid for the first frame
  [ w, w, r, r, r, r, r, w, w ],
  [ w, w, r, w, r, w, r, w, w ],
  [ w, w, r, r, r, r, r, w, w ],
  [ w, r, r, r, w, r, r, r, w ],
  [ r, w, w, r, r, r, w, w, r ],
  [ r, r, w, w, w, w, w, r, r ]
  ]

frameTwo = [ #The colour grid for the second frame
  [ w, w, w, w, w, w, w, w, w ],
  [ w, w, r, r, r, r, r, w, w ],
  [ w, w, r, w, r, w, r, w, w ],
  [ r, w, r, r, r, r, r, w, r ],
  [ r, r, r, r, w, r, r, r, r ],
  [ w, w, w, r, r, r, w, w, w ]
  ]

def drawFrame(screen, frame):
    for y, row in enumerate(frame): #For each row in the frame
        for x, colour in enumerate(row): #For each colour in the row
            rect = pygame.Rect(x*25, y*25, 25, 25) #Create the rect of colour for that item in the row
            screen.fill(colour, rect=rect) #Fill colour to the screen in the rect

while True: #While the program is running
    for event in pygame.event.get(): #if any events are detected
        if event.type == pygame.QUIT: #If the event is to close the window
            pygame.quit() #Clear up pygame and stop it
            sys.exit() #Stop the system

    drawFrame(screen, frameOne) #Draw the first frame
    pygame.display.update() #Update the screen
    pygame.time.wait(1000) #Wait a second
    drawFrame(screen, frameTwo) #Draw the second frame
    pygame.display.update() #Update the screen
    pygame.time.wait(150) #Wait a 15% of a second


