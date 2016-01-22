# import a library called 'pygame'
import pygame

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


 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock_1 = pygame.time.Clock() 
 
#initial rectangle positions
rect_x = 50
rect_y = 50
rect_Width = 80
rect_Height = 50

#velocity of rectangle
rect_Vx = 3.
rect_Vy = 2.

# -------- Main Program Loop -----------
while not done: #while loop continues while true (i.e. while not false)
    # --- Main event loop (Handling inputs)
    for event in pygame.event.get(): #for event in list of events (i.e. list of user inputs) 
        if event.type == pygame.QUIT: #if one of these events is that the user clicked close 
            done = True #flag to exit while loop
 
    # --- Game logic should go here (game processing)
    rect_Vy += 1.05
    rect_x += rect_Vx
    rect_y += rect_Vy

    if rect_x+rect_Width > Screen_Width-1 or rect_x < 0: #screen measures 0-699 => need to -1 from Screen_Width & take into account the width of the rectangle (since rect_x is the top left corner of the square)
        rect_Vx *= -1
        
    if rect_y+rect_Height > Screen_Height-1 or rect_y < 0:
        rect_Vy *= -1

    #rect_Vy += 0.5 #acceleration :o

    # --- Drawing code should go here (drawing stuff)
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    Screen1.fill(white)
    
    # Drawing on white screen
    pygame.draw.rect(Screen1, black, [rect_x,rect_y,rect_Width,rect_Height])

    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip() #command comes from flipbooks (updates screen with what we drew)
 
    # --- Limit to 30 frames per second
    clock_1.tick(30) #.tick() is a function of object Clock() clock_1 is an instance of object Clock() 
    #essentially a wait command for 1/30th of a second 

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
