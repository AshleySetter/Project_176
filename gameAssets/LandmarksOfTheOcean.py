# import a library called 'pygame'
import pygame
import random

#define objects
class Jewel:
    'Base class for all jewels'
    jewelCount = 0 #the variable jewelCount is a class variable whose value is shared among all instances of this class. It can be accessed as Jewel.jewelCount from inside or outside the class (NOT static)

    def __init__(self): #JewelNo):
        Jewel.jewelCount += 1 #keeps track of current no of jewel
        self.exists = 1  #set flag to say that jewel exists and has not been "popped"

    def SpawnJewelPosn(self, Screen_Width, Screen_Height): #sets a random spawn position for the jewel
        offset = 50
        self.x = random.randrange(0+offset,Screen_Width-offset)
        self.y = random.randrange(0+offset,Screen_Height-offset)  
        JewelSelect = random.randrange(0,1)
        noOfJewelTypes = 2
        self.JewelSelect = random.randrange(0,noOfJewelTypes) #generates random int between 0 and noOfJewelTypes (not including noOfJewelTypes!)
        #print self.JewelSelect
        #print "Setting Jewel spawn position at:" , self.x, self.y
    
    def returnPosn(self): #function to return the jewel's position
        return self.x, self.y 

    def jewelPop(self):
        #sets deleted flag and decrements jewelCount
        Jewel.jewelCount -= 1
        self.exists = 0
        global GameScore
        GameScore+=1
        global PopSound
        PopSound.play()

    

#define functions
def MakeJewel(JewelList, Screen_Width, Screen_Height): #function to create an instance of class jewel and run the spawnJewelPosn function and increment the TotalJewelNo which states how many jewels have been created
    global TotalJewelNo
    #tempJewelIntance = Jewel()
    JewelList.append(Jewel())
    JewelList[TotalJewelNo].SpawnJewelPosn(Screen_Width, Screen_Height)
    #print "TotalJewelNo (in func): ", TotalJewelNo
    TotalJewelNo += 1
    

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


# set the width and height of the screen
Screen_Width=1200
Screen_Height=700
ScreenSize=[Screen_Width,Screen_Height] #[width,height]
Screen1=pygame.display.set_mode(ScreenSize) #'Screen1' is the handle relating to this particular window

pygame.display.set_caption("Landmarks of the ocean") #sets game title

#initialise variables
pi = 3.141592653

GameScore = 0
FadeoutFlag = 0

JewelList=[]  #list containing instances of jewel class
TotalJewelNo = 0 #initialises total no of jewels which have existed to 0

x_speed = 0 #initialises mermaid to be stationary
y_speed = 0

speedChange = 4 #sets speed of mermaid movement

x_coord = Screen_Width/2 #start in middle of screen
y_coord = Screen_Height/2

horizFlag = 0 #flag for if mermaid is moving left/right (-1/1)
vertFlag = 0  #flag for if mermaid is moving up or not moving/down (0/-1)

CreditsX=Screen_Width+100

pygame.mouse.set_visible(0) #Hide mouse cursor

#import images & Sounds-------------------------------------------------------------------------------
Background = pygame.image.load('gameAssets/Background_Scaled.jpeg').convert()

Background_Ocean = pygame.image.load('gameAssets/OceanBackground_Scaled.jpg').convert()

EvilCrab_image = pygame.image.load('gameAssets/Evil_Crab5.png').convert()
EvilCrab_image.set_colorkey(white) #sets a particlar colour to be transparent!!!! 
EvilCrabx2 = pygame.transform.scale2x(EvilCrab_image) #scales crab up by factor of 2

#Mermaid_mid = pygame.image.load('gameAssets/Mermaid2_mid.png').convert()
Mermaid_mid = pygame.image.load('gameAssets/Mermaid_Summers.png').convert()
Mermaid_mid.set_colorkey(white) 
#Mermaid_midx2 = pygame.transform.scale2x(Mermaid_mid)
Mermaid_midx2 = Mermaid_mid

BlueJewel = pygame.image.load('gameAssets/BlueJewel3.png').convert()
BlueJewel.set_colorkey(black)

PinkJewel = pygame.image.load('gameAssets/PinkJewel.png').convert()
PinkJewel.set_colorkey(black) 


Mermaid_Player = Mermaid_midx2 #initialises Mermaid_Player (i.e. the player character equal to upright mermaid)

PopSound = pygame.mixer.Sound("gameAssets/66136__theta4__ding30603-spedup.wav")

#setting background music/sound
pygame.mixer.music.load('gameAssets/213703__taira-komori__sea-magma.mp3')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()

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

        elif event.type == pygame.constants.USEREVENT:
            pygame.mixer.music.play()
            if FadeoutFlag == 1:
                pygame.mixer.music.load('gameAssets/51195__the-bizniss__flute-riff.wav')
                pygame.mixer.music.play()

            #this whole if multiplexer facilitates movement of player character and sets orientation of player character
        elif event.type == pygame.KEYDOWN: #user pressed down on a key
            if event.key == pygame.K_LEFT:
                x_speed = -speedChange
                horizFlag = -1
                Mermaid_Player = pygame.transform.rotate(Mermaid_midx2, 90)
            elif event.key == pygame.K_RIGHT:
                x_speed = speedChange
                horizFlag = 1
                Mermaid_Player = pygame.transform.rotate(Mermaid_midx2, -90)
            elif event.key == pygame.K_UP:
                y_speed = -speedChange
                #Mermaid_Player =  Mermaid_midx2
            elif event.key == pygame.K_DOWN:
                y_speed = speedChange
                if horizFlag == 0:
                    Mermaid_Player = pygame.transform.rotate(Mermaid_midx2, 180)
                vertFlag = -1
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
                horizFlag = 0
                if vertFlag == -1:
                    Mermaid_Player = pygame.transform.rotate(Mermaid_midx2, 180)
                else:
                    Mermaid_Player = Mermaid_midx2
            elif event.key == pygame.K_RIGHT:
                x_speed = 0
                horizFlag = 0
                if vertFlag == -1:
                    Mermaid_Player = pygame.transform.rotate(Mermaid_midx2, 180)      
                else:
                    Mermaid_Player = Mermaid_midx2
            elif event.key == pygame.K_UP:
                y_speed = 0
            elif event.key == pygame.K_DOWN:
                y_speed = 0
                if vertFlag == -1 and horizFlag == 0:
                    Mermaid_Player = Mermaid_midx2   
                vertFlag = 0

        
    # --- Game logic should go here (game processing)
    
    #pos = pygame.mouse.get_pos()
    #mouseX = pos[0]
    #mouseY = pos[1]
 
#These co-ords are used as hitbox for game mechanics
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
    Mermaid_Size = Mermaid_Player.get_rect().size
    x_rightcoord = x_coord + Mermaid_Size[0]
    y_downcoord = y_coord + Mermaid_Size[1] 
    
#this if multiplexer constrains mermaid player to the screen
    if x_coord < 0:
        x_coord = 0
    elif x_rightcoord > Screen_Width-1:
        x_coord = Screen_Width-1-Mermaid_Size[0]
    elif y_coord < 0:
        y_coord = 0
    elif y_downcoord > Screen_Height-1:
        y_coord = Screen_Height-1-Mermaid_Size[1]
        

    while Jewel.jewelCount < 1: #sets max no of jewels which can be onscreen at once
        MakeJewel(JewelList, Screen_Width, Screen_Height) 

    for jewel in JewelList: #loops through list of instances of Jewel class
        if jewel.exists == 1: #if jewel hasn't been 'popped'
            Jewelx = jewel.returnPosn()[0]
            Jewely = jewel.returnPosn()[1]
            if jewel.JewelSelect == 0:
                BlueJewelSize = BlueJewel.get_rect().size
                if Jewelx+BlueJewelSize[0]/2 > x_coord and Jewelx+BlueJewelSize[0]/2 < x_rightcoord and Jewely+BlueJewelSize[1]/2 > y_coord and Jewely+BlueJewelSize[1]/2 < y_downcoord: #checks if mermaid hitbox is over jewel co-ords
                    jewel.jewelPop() #pops jewel if collision is detected
            if jewel.JewelSelect == 1:
                PinkJewelSize = PinkJewel.get_rect().size
                if Jewelx+PinkJewelSize[0]/2 > x_coord and Jewelx+PinkJewelSize[0]/2 < x_rightcoord and Jewely+PinkJewelSize[1]/2 > y_coord and Jewely+PinkJewelSize[1]/2 < y_downcoord: #checks if mermaid hitbox is over jewel co-ords
                    jewel.jewelPop() #pops jewel if collision is detected


    #print JewelList[0].jewelCount

    #if Xobject > x_coord and Xobject < x_rightcoord and Yobject > y_coord and Yobject < y_downcoord:
    #then object coord is inside mermaid


    # --- Drawing code should go here (drawing stuff)
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
#    Screen1.fill(blue)
    # Drawing on screen

    Screen1.blit(Background,[0,0])

    for jewel in JewelList:
        if jewel.exists == 1: #checks if jewel has been 'popped'
            #pygame.draw.circle(Screen1, green, jewel.returnPosn(), 4, 0) #displays "un-popped" jewels
            if jewel.JewelSelect == 0:
                Screen1.blit(BlueJewel,jewel.returnPosn())
            if jewel.JewelSelect == 1:
                Screen1.blit(PinkJewel,jewel.returnPosn())
    #Screen1.blit(EvilCrabx2, [60,60])

    Screen1.blit(Mermaid_Player, [x_coord, y_coord])

    font001 = pygame.font.SysFont('Calibri', 25, True, False) #select font, size, bold, italics

    GameScoreStr = str(GameScore)
    GameScoreTextStr = "Score: "
    ScoreText = GameScoreTextStr+GameScoreStr
    ScoreText = font001.render(ScoreText, True, white)

    Screen1.blit(ScoreText, [Screen_Width-90, 20])

    if GameScore > 20:  #win condition
        #Screen1.fill(white)
        Screen1.blit(Background_Ocean,[0,0])
        #pygame.mixer.music.stop()
        if FadeoutFlag == 0:
            pygame.mixer.music.fadeout(2000)
            FadeoutFlag = 1
        CreditText = font001.render("Coding and Game Design: Ashley Setter                              Art Design: Heather Riddle                              Story Design: Summer Oliver                              Sound and Music Courtesy of http://www.freesound.org", True, black) #Render the text. "True" means anti-aliased text.
        Screen1.blit(CreditText, [CreditsX, Screen_Height/2])
        CreditsX -= 3
        
#could have lots of spaces between each person and scroll the credits across the screen
    

        
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip() #command comes from flipbooks (updates screen with what we drew)

    #print "Score:", GameScore


    # --- Limit to 30 frames per second
    clock_1.tick(30) #.tick() is a function of object Clock() clock_1 is an instance of object Clock() 
    #essentially a wait command for 1/30th of a second 

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
