# (Directions to Download and Play are at the Bottom of README)

# Takeoff Pygame 
 Creating an infinite runner/dodge style game from scratch using Pygame modules
 
# Takeoff Pygame Project

In this notebook, I will be creating a game from scratch using the Pygame modules. This game will take the form of an endless runner or dodge game. In these types of games, a player continues on a single infinite level dodging obstacles until they hit one and end the game. Oftentimes, the player is moving to the right (background and obstacles move to the left) while avoiding obstacles. Rather, in this game, our player will be moving up while dodging obstacles that are falling down. 

### Mechanics

##### Controls:
The player will have 3 separate controls. The first control will be the spacebar which will move the character upward. The character will automatically want to fall downward, therefore holding the spacebar will allow you to move up and releasing the spacebar will make the character natually fall. The second and third controls will be the left and right arrow keys to move the character to the left and right respectively. Through these 3 controls, the player can move their character in all directions in the 2D plane of the screen.

##### Boundaries:
Boundary conditions will be set at the edges of the game window. The left and right boundaries along with the top boundary will serve as borders that the game will not allow you to pass. Therefore, your character will stop at any of these sides if the player attempts to move their character past them. The bottom boundary, on the other hand, will serve as a means of ending the game. If the player allows their character to fall too far to the point that they fall to the bottom boundary, the character will explode and the game will end.

##### Obstacles:
Obstacles will continuously fall from the top of the screen towards the bottom. Their positions will be randomly generated and therefore unpredictable. This is done so that the player has to act on reaction to seeing the obstacles rather than previous knowledge of where they will be. As the player advances through the game, the obstacles will become faster. This will make the game progressively more difficult as time advances. When the player allows the character to collide with an obstacle, the character will explode and the game will end.

### Score
The objective of the game is to survive as long as possible. At timer will begin at zero at the start of each game. It will increase in minutes and seconds as time elapses. Once the game ends, the timer will stop and your final survival time will be portrayed in the middle of the screen.

### Theme, Visuals, and Audio
This game will have a space theme. The name takeoff comes from the rocketship character icon which takes off and flies upward when the spacebar is held. The obstacles will be asteroids that fall from the top of the screen. The background is a unique, scifi space theme on some extraterrestrial planet. A flame will come from the bottom of the rocket while the spacebar is held and a corresponding rocket booster noise will accompany. There will be a fun scifi space backround with fast paced game music in the background. When the player dies, the rocket will turn into an explotion and there will be an explosive noise to go along with this as well. The background music will change to a much slower track until the replay button is pressed, a new game starts, and the original music replays. The current time will appear at the bottom left of the screen throughout the game to avoid interference with the asteroids falling from above.

# How to Download and Play Game!

## Through Application on MacOS Software:
This game was built using Pygame on MacOS and I created a downloadable app for MacOS users. Therefore, a direct visual interface application can be accessed on macOS devices
1. Navigate to my "Takeoff-Pygame" repository
2. Click the green "Code" button at the top of the screen
3. Click "download ZIP" at the bottom of the dropdown menu and then click on the download to extract the zip containing all of the necessary game files, including the application
4. Navigate to the folder created from the zip and double click on the "VGW_Game" application
### Note:
If this does not work and you get an error like "VGW_Game is damaged and can't be opened. You should move it to the trash", please don't. I'm not giving you a virus, I swear. You can try these to fix this:
  
   a. Navigate to System Preferences -> Security & Privacy -> General. At the bottom of the screen, you may see "VGW_Game was blocked from use because it was not from an identified 
      developer". Next to this, there is a button that says "Open Anyways" which should bypass this
      
   b. If that doesn't work, go to your command line app on Mac titled "Terminal" and type "xattr -cr /path/to/game/folder" where you would replace the end with your specific path the 
      the game folder created by the zip file download. The path for me took the form of "/Users/coltondifranco/downloads/Takeoff-Pygame-main" but will differ for everyone depending on 
      the user and location of the folder

## Through Python in Command line on Windows or Mac:
This game was not made on a Windows device, so I was not able to create a direct ".exe" application for Windows devices. To run the game on Windows, you will need to have Python and Pygame installed and run the Python game script on the Windows command line.
1. Navigate to my "Takeoff-Pygame" repository
2. Click the green "Code" button at the top of the screen
3. Click "download ZIP" at the bottom of the dropdown menu and then cick on the download itslef to extract the zip containing the necessary game files, including the audio, visuals, and Python script
4. Install Python at https://www.python.org -> Downloads -> download on your specific operating system and version
5. Install Pygame in the command line (app titled "Command Prompt" on windows or "Terminal" on macOS) by typing "pip install pygame"
6. In the command line, navigate the the folder created from the zip extraction by typing "cd path/to/game/folder" and replacing the path with your computer specific path
7. Run the Python file by typing "python VGW_Game.py"


# My high score is 1:44! I would love to know how long you survived and if you were able to beat my score.

