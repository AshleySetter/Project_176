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
ScreenSize=[700,500] #[w,h]
Screen1=pygame.display.set_mode(ScreenSize) #'Screen1' is the handle relating to this particular window

pygame.display.set_caption("Landmarks of the ocean")


 
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
    
    #EXAMPLE SHAPES

#    pygame.draw.line(Screen1, blue, [10,20], [100,50], 5) #(screen, colour, startpoint, endpoint, thickness) # pygame library, draw package in that library, line function in that package

#    for X in range(0,300,50): #USE THIS TO DRAW REPEATING PATTERNS E.G FENCES, RAILWAY TRACKS
#        pygame.draw.line(Screen1, blue, [X,X], [X+100,X+50], 4)

    #pygame.draw.rect(Screen1, green, [20,20,250,90], 5) #[x,y,xlength,ylength], linewidth

    #pygame.draw.ellipse(Screen1, blue, [20,40,300,100], 7)
 
    #font001 = pygame.font.SysFont('Calibri', 25, True, False) #select font, size, bold, italics

    #text001 = font001.render("There are mermaids, evil crabs and walruses and diving people", True, red) #Render the text. "True" means anti-aliased text.

    #Screen1.blit(text001, [90, 250])

    #text002 = font001.render("Insert Imagination Here!", True, turqoise )

    #Screen1.blit(text002, [250,300])

    # This draws a triangle using the polygon command
    #pygame.draw.polygon(Screen1, black, [[300, 100], [210, 200], [400, 200]], 5)
    
    #pygame.draw.polygon(Screen1, turqoise, [[10,10],[10,80],[80,160],[160,190],[200,200]], 6)

    

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip() #command comes from flipbooks (updates screen with what we drew)
 
    # --- Limit to 30 frames per second
    clock_1.tick(30) #.tick() is a function of object Clock() clock_1 is an instance of object Clock() 
    #essentially a wait command for 1/30th of a second 

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
