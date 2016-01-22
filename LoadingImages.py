# import a library called 'pygame'
import pygame
import random

#define functions


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

#initialise variables
pi = 3.141592653


# set the width and height of the screen
Screen_Width=700
Screen_Height=500
ScreenSize=[Screen_Width,Screen_Height] #[width,height]
Screen1=pygame.display.set_mode(ScreenSize) #'Screen1' is the handle relating to this particular window

pygame.display.set_caption("Landmarks of the ocean")

#import images
test_image = pygame.image.load('gameAssets/Evil_Crab5.png').convert()
test_image.set_colorkey(white) #sets a particlar colour to be transparent!!!! 

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

    pos = pygame.mouse.get_pos()
    mouseX = pos[0]
    mouseY = pos[1]
 
    # --- Drawing code should go here (drawing stuff)
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    Screen1.fill(blue)



    Screen1.blit(test_image, [mouseX,mouseY])

    # Drawing on white screen
        
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip() #command comes from flipbooks (updates screen with what we drew)
 
    # --- Limit to 30 frames per second
    clock_1.tick(30) #.tick() is a function of object Clock() clock_1 is an instance of object Clock() 
    #essentially a wait command for 1/30th of a second 

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
