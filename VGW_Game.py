#!/usr/bin/env python
# coding: utf-8

# # Takeoff Pygame Project
# 
# In this notebook, we will be creating a game from scratch using the Pygame modules. This game will take the form of an endless runner or dodge game. In these types of games, a player continues on a single infinite level dodging obstacles until they hit one and end the game. Oftentimes, the player is moving to the right (background and obstacles move to the left) while avoiding obstacles. Rather in this game, our player will be moving up while dodging obstacles that are falling down. 
# 
# ### Mechanics
# 
# ##### Controls:
# The player will have 3 separate controls. The first control will be the spacebar which will move the character upward. The character will automatically want to fall downward, therefore holding the spacebar will allow you to move up and releasing the spacebar will make the character natually fall. The second and third controls will be the left and right arrow keys to move the character to the left and right respectively. Through these 3 controls, the player can move their character in all directions in the 2D plane of the screen.
# 
# ##### Boundaries:
# Boundary conditions will be set at the edges of the game window. The left and right boundaries along with the top boundary will serve as borders that the game will not allow you to pass. Therefore, your character will stop at any of these sides if the player attempts to move their character past them. The bottom boundary on the other hand will serve as a possible way of ending the game. If the player allows their character to fall too far to the point that they fall to the bottom boundary, the character will explode and the game will be over.
# 
# ##### Obstacles:
# Obstacles will continuously fall from the top of the screen towards the bottom. Their positions will be randomly generated and therefore unpredictable. This is done so that the player has to act on reaction to seeing the obstacle rather than knowledge of knowing where it will be. As the player advances through the game, the obstacles will become faster. This will make the game progressively more difficult as time advances. When the player allows the character to collide with an obstacle, the character will explode and the game will end.
# 
# ### Score
# The objective of the game is to obtain the highest possible score. The player is awarded a single point for every obstacle that is sucessfully dodged as it exists the bottom of the screen. This means that as the game progresses, points can be accumulated faster due to higher numbers of obstacles and their faster speeds.
# 
# ### Theme, Visuals, and Audio
# This game will have a space theme. The name takeoff comes from the character being a rocketship as it takes off and flies when the spacebar is held. The obstacles will be asteroids that fall from the top. A flame will come from the bottom of the rocket while the spacebar is held and a corresponding rocket booster noise will accompany. There will be a fun scifi space backround with fast paced game music in the background. When the player dies, the rocket will turn into an explotion and their will be an explosive noise to go along with this as well. The current score will appear at the top left of the screen throughout the game.

# ## Creating the Game

# We need to import all of the necessary modules needed to code the game.

# In[5]:


# Importing Pygame which has all of the game specific commands
import pygame

# Importing random which allows us to generate random values
import random

# Importing math package to easily call the distance formula for collisions
import math

# Importing mixer to allow for game sounds and music
from pygame import mixer


# Now we need to initialize the Pygame modules in order to be able to use all of its components. It basically sets up or turns on the neccessary components of Pygame. We will also add a clock to make sure the game runs the same on all devices.

# In[7]:


# Initializing Pygame modules
pygame.init()

# Adding clock
clock = pygame.time.Clock()


# Now that we have all of the modules successfully imported and initailized, we can start with the creation of the game. A very important first step to this is creating the game window. This is the screen in which the game will be played and where the game components will be displayed. We will also create a game over trigger that can be used to allow certain functions to happen either only when the game is active or only after the game has ended.

# In[9]:


# Creating a game window of width 800 and height 600
windowX = 800
windowY = 600
screen = pygame.display.set_mode((windowX, windowY))

# Setting over trigger to false meaning the game starts as being active
over_trigger = False


# Note that the window is generated down and right, starting from the top left corner. This means that a width value of 0 corresponds to the left border of the window and a width value of 800 corresponds to the right border of the window. Similarly, a height value of 0 corresponds to the top border of the window while a height value of 600 corresponds to the bottom of the window. This is very important to know as we will need to use this coordinate system to implement all of the aspects of our game to spefic locations on the window. 

# Now that we have our game window created, we want to add the title of the game to the top of the window as an identifyer. 

# In[12]:


# Setting window title
pygame.display.set_caption('Takeoff')


# Next, we need to create the background for the game to be played on. To do this, we will find and download and image from the internet into our folder, load it into pygame, and then scale the image to our desired size.

# In[14]:


# Loading our background image into pygame
background = pygame.image.load('assets/space.jpg')

# Scaling the background to desired size
background = pygame.transform.scale(background, (1200, 600))


# We now have a game window with a background and a title. Here, we will want to add background music that fits in with the game design. Withough background music, the game could be quite boring to play. We need to find music online, download it to the game folder, load it into the notebook, and finally allow it to loop so that it does not stop after one play through. We will allow this music to play only while the game is active as we will change the music after death.

# In[16]:


# Loading background music
mixer.music.load('assets/background.mp3')

# Allowing the music to loop while the game is active
if over_trigger == False:
    mixer.music.play(-1)


# We are finally ready to start adding the visuals into the game. We will start with the main playable character. To do this, we will define the coordinates of the player, the initial movements of the player, and define a function which will put our player into the game window. We need to find a player icon online in which we want to use to be downloaded into the game as well. We will do the same thing for the flame that accompanies the rocket below when the player holds the spacebar. flame_on is initially defined as False and will eventually change change value to True so that the program knows when to display the flame and flame sound. We also create a function that places the flame in the correct position below the character. 

# In[18]:


# Player and Flame

# Defining player initial coordinates
playerX = 370
playerY = 520

# Defining players inital movement
playerX_change = 0
playerY_change = 0

# Loading player icon image
rocket = pygame.image.load('assets/rocket.png')
rotated_rocket = pygame.transform.rotate(rocket, 45)

# Define a function to create the player with an image and its coordinates
def player(x,y):
    screen.blit(rotated_rocket, (x, y))

# Loading rocket flame icon and its coordinates
flame = pygame.image.load('assets/flame.png')
flame = pygame.transform.rotate(flame, 180)
flameX = playerX
flameY = playerY
flame_on = False

# Firing flame
def fire_flame(x, y):
    screen.blit(flame, (x+29, y+65))


# The obstacles need to be created next. The image, x-coordinate, y-coordinate, and y change values are defined as empty arrays so that each individual obstacle can be appended to them as they respawn or are created. A for loop is used to cycle through the number of obstacles and define a random location in which they will spawn in our defined range of possibilites. Lastly, a function is made that will be used to put the obstacles on the screen in their random location.

# In[20]:


# Obstacles

# Defining obstacles and their initial coordinates
asteroid = pygame.image.load('assets/asteroid.png')
asteroid = pygame.transform.rotate(asteroid, 45)
asteroid = pygame.transform.scale(asteroid, (50, 50))
obsimg = []
obsX = []
obsY = []
obsY_change = []
num_of_obs = 12

for i in range(num_of_obs):
    obsimg.append(asteroid)

    # Coordinates of obstacles on window with randomization and movement
    obsX.append(random.randint(0, 734))
    obsY.append(random.randint(-1200, -10))
    obsY_change.append(3)

# Function to make obstacles
def obs(x, y, i):
    screen.blit(obsimg[i], (x, y))


# With all of the main visuals defined for the game, we must create and define a way for the game to end. This takes the form of a collision between the rocketship and an asteroid. Here, we define a collision as a specified distance between an asteroid and the rocketship.

# In[22]:


# Defining Collision Function

def collide(playerX, playerY, obsX, obsY):
    player = (playerX+20, playerY)
    obs = (obsX, obsY)
    distance = math.dist(player, obs)
    if distance < 30:
        return True
    else:
        return False


# Now we need a way to keep score and display it on the screen. Here, we will define what a score is and create a function to place it on the screen from everything to its location, color, and font.

# In[24]:


# Keeping score

start_time = pygame.time.get_ticks()
final_time = 0
font = pygame.font.Font('freesansbold.ttf', 40)
textX = 10
textY = 550

# Defining a function to show the elapsed time
def show_time(x, y):
    if over_trigger == False:
        elapsed_sec = (pygame.time.get_ticks() - start_time) / 1000
    else:
        elapsed_sec = final_time
    
    minutes = int(elapsed_sec) // 60
    seconds = int(elapsed_sec) % 60
    time_text = f'Time Survived: {minutes:02}:{seconds:02}'
    time = font.render(time_text, True, (255, 255, 255))
    screen.blit(time, (x, y))

# Changing the location of the score when the game ends
text_overX = 200
text_overY = 280


# Similar to score keeping, we need to define a function to display a game over text when the character dies. 

# In[26]:


# Game Over

game_over_text = pygame.font.Font('freesansbold.ttf', 70)
overX = 185
overY = 200

# Defining function to display game over
def game_over(x, y):
    over = game_over_text.render('GAME OVER', True, (255, 255, 255))
    screen.blit(over, (x, y))


# Along with the game over text, we want to add a button to play again so that the window need not be closed and this entire notebook reran in order to play another game after a death.

# In[28]:


# Play again button

# Defining colors for replay button and replay button while hovered
replay_color = (50, 50, 170)
replay_hover_color = (50, 100, 170)

# Defining the shape of the button (x, y, width, height)
replay_shape = pygame.Rect(250, 330, 300, 100)

# Defining function to create button
def replay():
    mouse_position = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # hover effect
    if replay_shape.collidepoint(mouse_position):
        pygame.draw.rect(screen, replay_hover_color, replay_shape)
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(screen, replay_color, replay_shape)

    # draw button text
    text = font.render('PLAY AGAIN', True, (255, 255, 255))
    text_rect = text.get_rect(center=replay_shape.center)
    screen.blit(text, text_rect)

    return False


# When the play again button is clicked, things need to happen. We need to create a function which resets the game to its beginning. This means returning the character and obstacles to their original positions, restarting the music, restarting the obstacles initial conditions, restarting the time, and turning over_trigger back to false.

# In[30]:


# Defining a restart function
def restart():
    global playerX, playerY, obsX, obsY, obsY_change, num_of_obs, start_time, final_time

    # Resetting the player
    playerX = 370
    playerY = 520

    # Resetting the obstacles
    obsX = []
    obsY = []
    obsY_change = []
    num_of_obs = 12

    for i in range(num_of_obs):
        obsX.append(random.randint(0, 734))
        obsY.append(random.randint(-1200, -100))
        obsY_change.append(3)

    # Reset the score and the time
    final_time = 0
    start_time = pygame.time.get_ticks()

    # Resetting the music
    mixer.music.load('assets/background.mp3')
    mixer.music.play(-1)


# With all preliminary game information defined, we are finally ready to get to the biggest chunk of the code. Here, we allow the game to run, allow for player inputs, game movements, screen interactions, and everything else that makes gameplay all while updating the screen with all of these at the same time. A while loop is created that allows everything inside to happen as long as the game window is open. That is, when the game is not running, nothing inside applies. 

# In[32]:


# Creating while loop in which all information will be valid while the window is running
running = True
while running:

    # Adding background image to screen so that it appears at all times while the game is running
    screen.blit(background, (0, 0))

    # Creating a for loop for game events. Here, all of the keystrokes are defined and mapped to a specific function
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        # Mapping downward keystrokes to functions
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playerY_change = -6
                # Rocket noise when holding space
                if over_trigger == False:
                    flame_sound = pygame.mixer.Sound('assets/engine.mp3')
                    flame_sound.play()
                # Rocket flame when holding space
                flame_on = True
            
            if event.key == pygame.K_LEFT:
                playerX_change = -6
            if event.key == pygame.K_RIGHT:
                playerX_change = 6

        # Mapping upward keystrokes to functions
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                playerY_change = 4
                # Rocket noise ending when lifting space
                flame_sound.stop()
                # Flame leaving when lifting space
                flame_on = False
            
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        
    # Allowing player to move with keystrokes
    playerX += playerX_change
    playerY += playerY_change

    # Setting X-boundaries for the player
    if playerX <= -20:
        playerX = -20
    elif playerX >= 730:
        playerX = 730

    # Setting Y-boundaries for player
    if playerY <= 0:
        playerY = 0
    # Game ends if player falls to far below the lower boundary of the game window
    if playerY >= 570:
        over_trigger = True
        mixer.music.stop()
        mixer.music.load('assets/over_music.mp3')
        mixer.music.play(-1)
        explosion_sound = pygame.mixer.Sound('assets/explosion.mp3')
        explosion_sound.play()
        final_time = (pygame.time.get_ticks() - start_time) / 1000
        for j in range(num_of_obs):
                obsX[j] = 900
                obsY[j] = 0
                obsY_change[j] = 0

    # Allowing obstacles to fall, respawn, and collide with character
    for i in range(num_of_obs):
        obsY[i] += obsY_change[i]

        if obsY[i] >= 700:
            obsX[i] = (random.randint(0, 734))
            obsY[i] = (random.randint(-120, -20))
            obsY_change[i] += 0.2

        # Game Over
        collision = collide(playerX, playerY, obsX[i], obsY[i])
        if collision:
            for j in range(num_of_obs):
                obsX[j] = 900
                obsY[j] = 0
                obsY_change[j] = 0
            over_trigger = True
            mixer.music.stop()
            mixer.music.load('assets/over_music.mp3')
            mixer.music.play(-1)
            explosion_sound = pygame.mixer.Sound('assets/explosion.mp3')
            explosion_sound.play()
            final_time = (pygame.time.get_ticks() - start_time) / 1000

        # Putting obstacles into the game
        obs(obsX[i], obsY[i], i)

    # Putting the player into the window and displaying the time elapsed
    if over_trigger == False:
        player(playerX, playerY)
        show_time(textX, textY)

    # Drawing the flame while space is held
    if flame_on:
        if over_trigger == False:
            flameX = playerX
            flameY = playerY
            fire_flame(flameX, flameY)

    # Game Over Text
    if over_trigger == True:
        game_over(overX, overY)
        show_time(text_overX, text_overY)
        playerX = 1000
        playerY = 0
        playerY_change = 0

    # Play Again
        if replay():
            over_trigger = False
            restart()
            

    # Updating the game window with any inputs
    pygame.display.update()

    # Setting uniform FPS so that the game runs the same speed on all devices
    clock.tick(60)

# Allowing for quitting of the window thus ending the while statement and everything inside
pygame.quit()


# In[ ]:




