# import a library called 'pygame'
import pygame
import random

# initialisize the game engine
pygame.init()

# Define some colours # 0-255 (2**8 conbiations of 8 bits 0000 0000 - 0 & 1111 1111 - 255
# Use colorpicker.com to find RGB numbers for a specific colour
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255) 
turqoise = (0,170,170)

pi = 3.141592653

# set the width and height of the screen
Screen_Width=700
Screen_Height=500
ScreenSize=[Screen_Width,Screen_Height] #[width,height]
Screen1=pygame.display.set_mode(ScreenSize) #'Screen1' is the handle relating to this particular window

pygame.display.set_caption("Landmarks of the ocean")

starList=[]

for i in range(0,100):
        x = random.randrange(0,Screen_Width)
        y = random.randrange(0,Screen_Height)
        starList.append([x,y]) #list of lists (similar to a c++ vector)

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock_1 = pygame.time.Clock() 
 
# -------- Main Program Loop -----------
while not done: #while loop continues while true (i.e. while not false)
    # --- Main event loop (Handling inputs)
    for event in pygame.event.get(): #for event in list of events (i.e. list of user inputs) 
        if event.type == pygame.QUIT: #if one of these events is that the user clicked close 
            done = True #flag to exit while loop
 
    # --- Game logic should go here (game processing)
 
    # --- Drawing code should go here (drawing stuff)
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    Screen1.fill(white)
    
    # Drawing on white screen
        
    for item in starList:
        item[1] += 3
        if item[1] > Screen_Height:
            #item[1] = 0 #as soon as it dissapears off bottom of screen it appears at top 
            item[1] = random.randrange(-20,-5) #now the new circle appears at a random y position off the screen so that it doesn't pop into existance on screen or appear at top of the screen as soon as it dissapears
            item[0] = random.randrange(0,Screen_Width)
        pygame.draw.circle(Screen1, blue, item, 4)
            
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip() #command comes from flipbooks (updates screen with what we drew)
 
    # --- Limit to 30 frames per second
    clock_1.tick(30) #.tick() is a function of object Clock() clock_1 is an instance of object Clock() 
    #essentially a wait command for 1/30th of a second 

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
