# import a library called 'pygame'
import pygame
import time
import random
import numpy as np

#define objects
class Coursework:
    """Base class for all coursework items"""
    courseworkCount = 0 #the variable courseworkCount is a class variable whose value is shared among all instances of this class. It can be accessed as Coursework.courseworkCount from inside or outside the class (NOT static)

    def __init__(self): #CourseworkNo):
        """initalises an instance of the coursework class, increments the instance counter"""
        Coursework.courseworkCount += 1 #keeps track of current no of coursework
        self.exists = 1  #set flag to say that coursework exists and has not been "popped"

    def SpawnCourseworkPosn(self, Screen_Width, Screen_Height): #sets a random spawn position for the coursework
        """Initialises a coursework instance, settings it's initial position as the top 
        middle of the screen and generating a random velocity"""
        offset = 50
        # self.x = random.randrange(0+offset,Screen_Width-offset)
        # self.y = random.randrange(-Screen_Height,-50) 
        self.x = Screen_Width/2.
        self.y = 0
        theta = np.random.normal(0, 0.7)
        vel = 10.
        self.velocity_x = vel*np.sin(theta)
        self.velocity_y = vel*np.cos(theta)

        noOfCourseworkTypes = len(CourseworkModelList)
        self.CourseworkSelect = random.randrange(0,noOfCourseworkTypes) #generates random int between 0 and noOfCourseworkTypes (not including noOfCourseworkTypes!)
        #print(self.CourseworkSelect)
        #print("Setting Coursework spawn position at:" , self.x, self.y)
    
    def returnPosn(self):
        """function to return the coursework's position"""
        return self.x, self.y 

    def courseworkPop(self):
        """sets exists flag to 0 so that the coursework instance
        no longer appears and decrements courseworkCount and increments score"""
        Coursework.courseworkCount -= 1
        self.exists = 0
        global GameScore
        GameScore+=1
        global WinScore

    def courseworkBurst(self):
        """sets exists flag to 0 so that the coursework instance
        no longer appears and decrements courseworkCount (does not increment score)"""
        Coursework.courseworkCount -= 1
        self.exists = 0

#define functions
def MakeCoursework(CourseworkList, Screen_Width, Screen_Height): 
    """function to create an instance of class coursework and run the 
    spawnCourseworkPosn function and increment the TotalCourseworkNo which 
    states how many courseworks have been created"""
    global TotalCourseworkNo
    #tempCourseworkIntance = Coursework()
    CourseworkList.append(Coursework())
    CourseworkList[TotalCourseworkNo].SpawnCourseworkPosn(Screen_Width, Screen_Height)
    #print("TotalCourseworkNo (in func): ", TotalCourseworkNo)
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

font001 = pygame.font.SysFont('Calibri', 25, True, False) #select font, size, bold, italics

# set the width and height of the screen
Screen_Width=1200
Screen_Height=700
ScreenSize=[Screen_Width,Screen_Height] #[width,height]
Screen1=pygame.display.set_mode(ScreenSize) #'Screen1' is the handle relating to this particular window

pygame.display.set_caption("Project176 - The Game") #sets game title

#initialise variables
pi = 3.141592653

GameScore = 0
WinScore = 10
FadeoutFlag = 0
Incr1 = 0
TimeSinceLastCoursework = 0
level = 0
playerNumber = 0
FrameRate=30

CourseworkList=[]  #list containing instances of coursework class
TotalCourseworkNo = 0 #initialises total no of courseworks which have existed to 0

x_speed = 0 #initialises player to be stationary
y_speed = 0

speedChange = 4 #sets speed of player movement

x_coord = Screen_Width/2 #start in middle of screen
y_coord = Screen_Height/2

horizFlag = 0 #flag for if player is moving left/right (-1/1)
vertFlag = 0  #flag for if player is moving up or not moving/down (0/-1)

CreditsX=Screen_Width+100

pygame.mouse.set_visible(0) #Hide mouse cursor

#import images & Sounds-------------------------------------------------------------------------------
Background = pygame.image.load('gameAssets/Board_rescaled.jpg').convert()

Background_Credits = pygame.image.load('gameAssets/Board_rescaled.jpg').convert()

Player_mid = pygame.image.load('gameAssets/character_model_scaled.png').convert()
#Player_mid.set_colorkey(white) 
Player_mid.set_colorkey(black) 
#Player_midx2 = pygame.transform.scale2x(Player_mid)
Player_midx2 = Player_mid

Player_Player = Player_midx2 #initialises Player_Player (i.e. the player character equal to upright player)

# Loading in images

Coursework_model1 = pygame.image.load('gameAssets/Coursework.jpg').convert()
Coursework_model1.set_colorkey(black)

Coursework_model2 = pygame.image.load('gameAssets/py2_icon.png').convert()
Coursework_model2.set_colorkey(black) 

CourseworkModelList = [Coursework_model1, Coursework_model2] # Adding an image to this list will add it to the possible coursework models

Ian = pygame.image.load('gameAssets/ian_icon.png').convert()
Ian.set_colorkey(black) 

alvaro = pygame.image.load('gameAssets/alvaroP_icon.png').convert()
ale = pygame.image.load('gameAssets/aleV_icon.png').convert()
ash = pygame.image.load('gameAssets/ashS_icon.png').convert()
craig = pygame.image.load('gameAssets/craigR_icon.jpg').convert()
david = pygame.image.load('gameAssets/davidL_icon.jpg').convert()
gabriele = pygame.image.load('gameAssets/gabrieleB_icon.jpg').convert()
hossam = pygame.image.load('gameAssets/hossamR_icon.jpg').convert()
kieran = pygame.image.load('gameAssets/kieranS_icon.jpg').convert()
lucy = pygame.image.load('gameAssets/lucyU_icon.jpg').convert()
manuele = pygame.image.load('gameAssets/manueleZ_icon.jpg').convert()
ryan = pygame.image.load('gameAssets/ryanP_icon.jpg').convert()
thorsten = pygame.image.load('gameAssets/thorstenW_icon.jpg').convert()

OriginalplayerList = [alvaro, ale, ash, craig, david, gabriele, hossam, kieran, lucy, manuele, ryan, thorsten]
playerFullSizeList = []
playerOffSetList = [[0, 10], [0, 10], [-40, 10], [-20, 20], [0, 10], [0, 15], [-4, 10], [-20, 10], [0, 10], [-24, 10], [-35, 10], [-135, 40]]
playerScaleList = [3, 2, 3, 3, 2, 3, 3, 2, 2, 2, 2, 2]
playerList = []
playerSizeList = []

for i, player in enumerate(OriginalplayerList):
    player.set_colorkey(black)
    playerFullSizeList.append([OriginalplayerList[i].get_rect()[2], OriginalplayerList[i].get_rect()[3]])
    playerList.append(pygame.transform.scale(OriginalplayerList[i], (OriginalplayerList[i].get_rect()[2]/playerScaleList[i], OriginalplayerList[i].get_rect()[3]/playerScaleList[i]))) # 1/3 image size
    playerSizeList.append([playerList[i].get_rect()[2], playerList[i].get_rect()[3]])

PlayerChoiceGapSize = 250
PlayerChoiceList_xPositions = np.arange(50+0, 50+PlayerChoiceGapSize*len(OriginalplayerList), PlayerChoiceGapSize)



#setting background music/sound
pygame.mixer.music.load('gameAssets/Keyboard_Typing_Sound_Effect.mp3')
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

            if event.type == pygame.constants.USEREVENT:
                pygame.mixer.music.play()
                if FadeoutFlag == 1:
                    pygame.mixer.music.load('gameAssets/51195__the-bizniss__flute-riff.wav')
                    pygame.mixer.music.play()

            if level == 0:
                if event.type == pygame.KEYDOWN: #user pressed down on a key
                    if event.key == pygame.K_LEFT:
                        playerNumber -= 1
                    elif event.key == pygame.K_RIGHT:
                        playerNumber += 1
                    if playerNumber < 0:
                        playerNumber = 0
                    elif playerNumber >= len(OriginalplayerList):
                        playerNumber = len(OriginalplayerList)-1
                    time.sleep(0.5)
                    #print(playerNumber)
                    if event.key == pygame.K_SPACE:
                        level += 1

            if level == 1:
                    #this whole if multiplexer facilitates movement of player character and sets orientation of player character
                if event.type == pygame.KEYDOWN: #user pressed down on a key
                    if event.key == pygame.K_LEFT:
                        x_speed = -speedChange
                        #horizFlag = -1
                        #Player_Player = pygame.transform.rotate(Player_midx2, 90)
                    elif event.key == pygame.K_RIGHT:
                        x_speed = speedChange
                        #horizFlag = 1
                        #Player_Player = pygame.transform.rotate(Player_midx2, -90)
                    elif event.key == pygame.K_UP:
                        y_speed = -speedChange
                    elif event.key == pygame.K_DOWN:
                        y_speed = speedChange
                        #if horizFlag == 0:
                        #    Player_Player = pygame.transform.rotate(Player_midx2, 180)
                        #vertFlag = -1
                        
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        x_speed = 0
                        #horizFlag = 0
                        #if vertFlag == -1:
                        #    Player_Player = pygame.transform.rotate(Player_midx2, 180)
                        #else:
                        #    Player_Player = Player_midx2
                    elif event.key == pygame.K_RIGHT:
                        x_speed = 0
                        #horizFlag = 0
                        #if vertFlag == -1:
                        #    Player_Player = pygame.transform.rotate(Player_midx2, 180)      
                        #else:
                        #    Player_Player = Player_midx2
                    elif event.key == pygame.K_UP:
                        y_speed = 0
                    elif event.key == pygame.K_DOWN:
                        y_speed = 0
                        #if vertFlag == -1 and horizFlag == 0:
                        #    Player_Player = Player_midx2   
                        #vertFlag = 0

    # --- Game logic should go here (game processing)
        
    #pos = pygame.mouse.get_pos()
    #mouseX = pos[0]
    #mouseY = pos[1]
    if level == 0: #level 0
        Screen1.fill(black)
        xPosPlayerChoice = -playerNumber*PlayerChoiceGapSize + Screen_Width/2 - 50
        for i, player in enumerate(OriginalplayerList):
            Screen1.blit(player, [(xPosPlayerChoice + PlayerChoiceList_xPositions[i] - playerFullSizeList[i][0]/2), (Screen_Height/2 - playerFullSizeList[i][1]/2)])

        PickCharText = font001.render("Use arrow keys to pick a player.            Press Space to Pick a player", True, white) #Render the text. "True" means anti-aliased text.
        Screen1.blit(PickCharText, [Screen_Width/2 - PickCharText.get_rect()[2]/2, Screen_Height/2 + 200])
        

    if level == 1:  #level 1    
     
    #These co-ords are used as hitbox for game mechanics
        x_coord = x_coord + x_speed
        y_coord = y_coord + y_speed
        Player_Size = Player_Player.get_rect().size
        x_rightcoord = x_coord + Player_Size[0]
        y_downcoord = y_coord + Player_Size[1] 
        
    #this if multiplexer constrains player to the screen
        if x_coord < 0:
            x_coord = 0
        elif x_rightcoord > Screen_Width-1:
            x_coord = Screen_Width-1-Player_Size[0]
        elif y_coord < 0:
            y_coord = 0
        elif y_downcoord > Screen_Height-1:
            y_coord = Screen_Height-1-Player_Size[1]
            
        TimeSinceLastCoursework += 1
        if(Coursework.courseworkCount < 10 and TimeSinceLastCoursework > 10): #sets max no of courseworks which can be onscreen at once
            MakeCoursework(CourseworkList, Screen_Width, Screen_Height) 
            TimeSinceLastCoursework = 0

        #if GameScore < WinScore :
        for coursework in CourseworkList: #loops through list of instances of Coursework class
            if coursework.exists == 1: #if coursework hasn't been 'popped'
                Courseworkx = coursework.returnPosn()[0]
                Courseworky = coursework.returnPosn()[1]

                for i, model in enumerate(CourseworkModelList):
                    if coursework.CourseworkSelect == i:
                        Coursework_model_Size = CourseworkModelList[i].get_rect().size
                        if Courseworkx+Coursework_model_Size[0]/2 > x_coord and Courseworkx+Coursework_model_Size[0]/2 < x_rightcoord and Courseworky+Coursework_model_Size[1]/2 > y_coord and Courseworky+Coursework_model_Size[1]/2 < y_downcoord: #checks if player hitbox is over coursework co-ords
                            coursework.courseworkPop() #pops coursework if collision is detected
                    #elif coursework.CourseworkSelect == 1:
                    #    Coursework_model2_Size = Coursework_model2.get_rect().size
                    #    if Courseworkx+Coursework_model2_Size[0]/2 > x_coord and Courseworkx+Coursework_model2_Size[0]/2 < x_rightcoord and Courseworky+PinkCoursework_model2_Size[1]/2 > y_coord and Courseworky+Coursework_model2_Size[1]/2 < y_downcoord: #checks if player hitbox is over coursework co-ords
                    #        coursework.courseworkPop() #pops coursework if collision is detected
                if Courseworky > Screen_Height:
                    coursework.courseworkBurst()

                coursework.y += coursework.velocity_y
                coursework.x += coursework.velocity_x

        #print(CourseworkList[0].courseworkCount)

        #if Xobject > x_coord and Xobject < x_rightcoord and Yobject > y_coord and Yobject < y_downcoord:
        #then object coord is inside player


        # --- Drawing code should go here (drawing stuff)
        # First, add the background. Don't put other drawing commands
        # above this, or they will be erased with this command.
    #    Screen1.fill(blue)
        # Drawing on screen

        Screen1.blit(Background,[0,0])

        for coursework in CourseworkList:
            if coursework.exists == 1: #checks if coursework has been 'popped'
                #pygame.draw.circle(Screen1, green, coursework.returnPosn(), 4, 0) #displays "un-popped" courseworks
                for i, courseworkmodel in enumerate(CourseworkModelList):
                    if coursework.CourseworkSelect == i:
                        Screen1.blit(courseworkmodel, coursework.returnPosn())
        Screen1.blit(Ian, [Screen_Width/2.-Ian.get_rect()[2]/2, 0])

        Screen1.blit(Player_Player, [x_coord, y_coord])
        Screen1.blit(playerList[playerNumber], [x_coord+playerSizeList[playerNumber][0]+playerOffSetList[playerNumber][0], y_coord-playerSizeList[playerNumber][1]+playerOffSetList[playerNumber][1]])

        GameScoreStr = str(GameScore)
        GameScoreTextStr = "Score: "
        ScoreText = GameScoreTextStr+GameScoreStr
        ScoreText = font001.render(ScoreText, True, white)    
        Screen1.blit(ScoreText, [Screen_Width-90, 20])

        if GameScore > WinScore:  #win condition
            level += 1
    elif level == 2:
        #Screen1.fill(white)
        Screen1.blit(Background_Credits,[0,0])
        #pygame.mixer.music.stop()
        if FadeoutFlag == 0:
            pygame.mixer.music.fadeout(2000)
            FadeoutFlag = 1
        CreditText = font001.render("Placeholder Credit Text...", True, black) #Render the text. "True" means anti-aliased text.
        Screen1.blit(CreditText, [CreditsX, Screen_Height/2])
        CreditsX -= 3
        Incr1+=1
        if Incr1 > FrameRate*15: #framerate * no of seconds for credits to run 
            pygame.quit()
     
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip() #command comes from flipbooks (updates screen with what we drew)

    #print("Score:", GameScore)


    # --- Limit to 30 frames per second
    clock_1.tick(FrameRate) #.tick() is a function of object Clock() clock_1 is an instance of object Clock() 
    #essentially a wait command for 1/30th of a second 

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
