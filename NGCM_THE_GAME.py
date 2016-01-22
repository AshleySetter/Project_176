# import a library called 'pygame'
import pygame
import random
import numpy as np

#define objects
class Coursework:
    'Base class for all jewels'
    jewelCount = 0 #the variable jewelCount is a class variable whose value is shared among all instances of this class. It can be accessed as Coursework.jewelCount from inside or outside the class (NOT static)

    def __init__(self): #CourseworkNo):
        Coursework.jewelCount += 1 #keeps track of current no of jewel
        self.exists = 1  #set flag to say that jewel exists and has not been "popped"

    def SpawnCourseworkPosn(self, Screen_Width, Screen_Height): #sets a random spawn position for the jewel
        offset = 50
        # self.x = random.randrange(0+offset,Screen_Width-offset)
        # self.y = random.randrange(-Screen_Height,-50) 
        self.x = Screen_Width/2.
        self.y = 0
        self.vx = np.random.normal(0, 3)

        noOfCourseworkTypes = 1
        self.CourseworkSelect = random.randrange(0,noOfCourseworkTypes) #generates random int between 0 and noOfCourseworkTypes (not including noOfCourseworkTypes!)
        #print self.CourseworkSelect
        #print "Setting Coursework spawn position at:" , self.x, self.y
    
    def returnPosn(self): #function to return the jewel's position
        return self.x, self.y 

    def jewelPop(self):
        #sets deleted flag and decrements jewelCount
        Coursework.jewelCount -= 1
        self.exists = 0
        global GameScore
        GameScore+=1
        global PopSound
        global WinScore
        #if GameScore < WinScore:
        #    PopSound.play()

    def jewelBurst(self):
        #sets deleted flag and decrements jewelCount
        Coursework.jewelCount -= 1
        self.exists = 0

#define functions
def MakeCoursework(CourseworkList, Screen_Width, Screen_Height): #function to create an instance of class jewel and run the spawnCourseworkPosn function and increment the TotalCourseworkNo which states how many jewels have been created
    global TotalCourseworkNo
    #tempCourseworkIntance = Coursework()
    CourseworkList.append(Coursework())
    CourseworkList[TotalCourseworkNo].SpawnCourseworkPosn(Screen_Width, Screen_Height)
    #print "TotalCourseworkNo (in func): ", TotalCourseworkNo
    TotalCourseworkNo += 1
    

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

pygame.display.set_caption("NGCM Simulation and Modelling - The Game") #sets game title

#initialise variables
pi = 3.141592653

GameScore = 0
WinScore = 100
FadeoutFlag = 0
Incr1 = 0
Incr2 = 0
TimeSinceLastCoursework = 0
FrameRate=30

CourseworkList=[]  #list containing instances of jewel class
TotalCourseworkNo = 0 #initialises total no of jewels which have existed to 0

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
Background = pygame.image.load('gameAssets_NGCM/NGCM_Board_rescaled.jpg').convert()

Background_Ocean = pygame.image.load('gameAssets_NGCM/NGCM_Board.jpg').convert()

EvilCrab_image = pygame.image.load('gameAssets/Evil_Crab5.png').convert()
EvilCrab_image.set_colorkey(white) #sets a particlar colour to be transparent!!!! 
EvilCrabx2 = pygame.transform.scale2x(EvilCrab_image) #scales crab up by factor of 2

#Player_mid = pygame.image.load('gameAssets/Player2_mid.png').convert()
Player_mid = pygame.image.load('gameAssets_NGCM/player.jpeg').convert()
#Player_mid.set_colorkey(white) 
Player_mid.set_colorkey(black) 
#Player_midx2 = pygame.transform.scale2x(Player_mid)
Player_midx2 = Player_mid

BlueCoursework = pygame.image.load('gameAssets_NGCM/Coursework.jpeg').convert()
BlueCoursework.set_colorkey(black)

#PinkCoursework = pygame.image.load('gameAssets/PinkCoursework.png').convert()
#PinkCoursework.set_colorkey(black) 

Ian = pygame.image.load('gameAssets_NGCM/ian.jpg').convert()
Ian.set_colorkey(black) 

Player_Player = Player_midx2 #initialises Player_Player (i.e. the player character equal to upright mermaid)

PopSound = pygame.mixer.Sound("gameAssets/66136__theta4__ding30603-spedup.wav")

#setting background music/sound
pygame.mixer.music.load('gameAssets_NGCM/Keyboard_Typing_Sound_Effect.mp3')
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
                Player_Player = pygame.transform.rotate(Player_midx2, 90)
            elif event.key == pygame.K_RIGHT:
                x_speed = speedChange
                horizFlag = 1
                Player_Player = pygame.transform.rotate(Player_midx2, -90)
            elif event.key == pygame.K_UP:
                y_speed = -speedChange
                #Player_Player =  Player_midx2
            elif event.key == pygame.K_DOWN:
                y_speed = speedChange
                if horizFlag == 0:
                    Player_Player = pygame.transform.rotate(Player_midx2, 180)
                vertFlag = -1
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
                horizFlag = 0
                if vertFlag == -1:
                    Player_Player = pygame.transform.rotate(Player_midx2, 180)
                else:
                    Player_Player = Player_midx2
            elif event.key == pygame.K_RIGHT:
                x_speed = 0
                horizFlag = 0
                if vertFlag == -1:
                    Player_Player = pygame.transform.rotate(Player_midx2, 180)      
                else:
                    Player_Player = Player_midx2
            elif event.key == pygame.K_UP:
                y_speed = 0
            elif event.key == pygame.K_DOWN:
                y_speed = 0
                if vertFlag == -1 and horizFlag == 0:
                    Player_Player = Player_midx2   
                vertFlag = 0

        
    # --- Game logic should go here (game processing)
    
    #pos = pygame.mouse.get_pos()
    #mouseX = pos[0]
    #mouseY = pos[1]
 
#These co-ords are used as hitbox for game mechanics
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
    Player_Size = Player_Player.get_rect().size
    x_rightcoord = x_coord + Player_Size[0]
    y_downcoord = y_coord + Player_Size[1] 
    
#this if multiplexer constrains mermaid player to the screen
    if x_coord < 0:
        x_coord = 0
    elif x_rightcoord > Screen_Width-1:
        x_coord = Screen_Width-1-Player_Size[0]
    elif y_coord < 0:
        y_coord = 0
    elif y_downcoord > Screen_Height-1:
        y_coord = Screen_Height-1-Player_Size[1]
        
    TimeSinceLastCoursework += 1
    if(Coursework.jewelCount < 10 and TimeSinceLastCoursework > 10): #sets max no of jewels which can be onscreen at once
        MakeCoursework(CourseworkList, Screen_Width, Screen_Height) 
        TimeSinceLastCoursework = 0

    #if GameScore < WinScore :
    for jewel in CourseworkList: #loops through list of instances of Coursework class
        if jewel.exists == 1: #if jewel hasn't been 'popped'
            Courseworkx = jewel.returnPosn()[0]
            Courseworky = jewel.returnPosn()[1]
            if jewel.CourseworkSelect == 0:
                BlueCourseworkSize = BlueCoursework.get_rect().size
                if Courseworkx+BlueCourseworkSize[0]/2 > x_coord and Courseworkx+BlueCourseworkSize[0]/2 < x_rightcoord and Courseworky+BlueCourseworkSize[1]/2 > y_coord and Courseworky+BlueCourseworkSize[1]/2 < y_downcoord: #checks if mermaid hitbox is over jewel co-ords
                    jewel.jewelPop() #pops jewel if collision is detected
            elif jewel.CourseworkSelect == 1:
                PinkCourseworkSize = PinkCoursework.get_rect().size
                if Courseworkx+PinkCourseworkSize[0]/2 > x_coord and Courseworkx+PinkCourseworkSize[0]/2 < x_rightcoord and Courseworky+PinkCourseworkSize[1]/2 > y_coord and Courseworky+PinkCourseworkSize[1]/2 < y_downcoord: #checks if mermaid hitbox is over jewel co-ords
                    jewel.jewelPop() #pops jewel if collision is detected
            if Courseworky > Screen_Height:
                jewel.jewelBurst()

            jewel.y += 10-jewel.vx
            jewel.x += jewel.vx
            #if not Incr2 % 10:
            #    jewel.vx = random.randrange(-20, 20)
    Incr2 += 1

    #print CourseworkList[0].jewelCount

    #if Xobject > x_coord and Xobject < x_rightcoord and Yobject > y_coord and Yobject < y_downcoord:
    #then object coord is inside mermaid


    # --- Drawing code should go here (drawing stuff)
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
#    Screen1.fill(blue)
    # Drawing on screen

    Screen1.blit(Background,[0,0])

    for jewel in CourseworkList:
        if jewel.exists == 1: #checks if jewel has been 'popped'
            #pygame.draw.circle(Screen1, green, jewel.returnPosn(), 4, 0) #displays "un-popped" jewels
            if jewel.CourseworkSelect == 0:
                Screen1.blit(BlueCoursework,jewel.returnPosn())
            if jewel.CourseworkSelect == 1:
                Screen1.blit(PinkCoursework,jewel.returnPosn())
    #Screen1.blit(EvilCrabx2, [60,60])
    Screen1.blit(Ian, [Screen_Width/2.-Ian.get_rect()[2]/2, 0])

    Screen1.blit(Player_Player, [x_coord, y_coord])

    font001 = pygame.font.SysFont('Calibri', 25, True, False) #select font, size, bold, italics

    GameScoreStr = str(GameScore)
    GameScoreTextStr = "Score: "
    ScoreText = GameScoreTextStr+GameScoreStr
    ScoreText = font001.render(ScoreText, True, white)    
    Screen1.blit(ScoreText, [Screen_Width-90, 20])

    if GameScore > WinScore :  #win condition
        #Screen1.fill(white)
        Screen1.blit(Background_Ocean,[0,0])
        #pygame.mixer.music.stop()
        if FadeoutFlag == 0:
            pygame.mixer.music.fadeout(2000)
            FadeoutFlag = 1
        CreditText = font001.render("Placeholder Credit Text...", True, black) #Render the text. "True" means anti-aliased text.
        Screen1.blit(CreditText, [CreditsX, Screen_Height/2])
        CreditsX -= 3
        Incr1+=1
        if Incr1 > FrameRate*30: #framerate * no of seconds for credits to run 
            pygame.quit()
        
#could have lots of spaces between each person and scroll the credits across the screen
    

        
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip() #command comes from flipbooks (updates screen with what we drew)

    #print "Score:", GameScore


    # --- Limit to 30 frames per second
    clock_1.tick(FrameRate) #.tick() is a function of object Clock() clock_1 is an instance of object Clock() 
    #essentially a wait command for 1/30th of a second 

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
