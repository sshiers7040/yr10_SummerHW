import pygame, sys #Import the pygame and sytem modules

pygame.init() #Allow pygame to initiate properly.

screen = pygame.display.set_mode([350, 400]) #The scrren object

b = pygame.Color("black") #Set the variable r to pygame's black colour
w = pygame.Color("white") #Set the variable w to pygame's white colour
y = pygame.Color("yellow") #Set the variable y to pygame's yellow colour

data = [
  [ w, w, w, w, b, b, b, b, b, b, w, w, w, w ],
  [ w, w, b, b, b, w, w, w, b, b, b, b, w, w ],
  [ w, b, b, w, w, y, y, y, y, y, b, b, w, w ],
  [ w, b, w, y, y, w, w, w, b, y, y, b, b, w ],
  [ b, b, w, y, y, w, y, y, b, y, y, b, b, w ],
  [ b, w, y, y, y, w, y, y, b, y, y, y, b, b ],
  [ b, w, y, y, y, w, y, y, b, y, y, y, b, b ],
  [ b, w, y, y, y, w, y, y, b, y, y, y, b, b ],
  [ b, w, y, y, y, w, y, y, b, y, y, y, b, b ],
  [ b, w, y, y, y, w, y, y, b, y, y, y, b, b ],
  [ b, w, y, y, y, w, y, y, b, y, y, y, b, b ],
  [ b, b, w, y, y, w, y, y, b, y, y, b, b, w ],
  [ w, b, w, y, y, b, b, b, b, y, y, b, b, w ],
  [ w, b, b, w, y, y, y, y, y, y, b, b, w, w ],
  [ w, w, b, b, b, w, w, w, b, b, b, b, w, w ],
  [ w, w, w, w, b, b, b, b, b, b, w, w, w, w ],
  ]

for y, row in enumerate(data): #For each row in data
    for x, colour in enumerate(row): #For each colour in the row
        rect = pygame.Rect(x*25, y*25, 25, 25) #Create the rect of colour for that item in the row
        screen.fill(colour, rect=rect) #Fill colour to the screen in the rect

pygame.display.update() #Update the screen

while True: #While the program is running
    for event in pygame.event.get(): #if any events are detected
        if event.type == pygame.QUIT: #If the event is to close the window
            pygame.quit() #Clear up pygame and stop it
            sys.exit() #Stop the system
