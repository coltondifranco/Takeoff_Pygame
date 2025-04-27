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
1. Download the Game
   * Download the application through this link: [DOWNLOAD HERE](https://drive.google.com/file/d/1XYVzbiBctyBcgi5mgo3z2qUt3NxfWsv6/view?usp=drive_link)
   * Click the download button at the top of the page (it will say that Google Drive cannot scan for viruses, select "Download anyway")
2. Extract the folder
   * Double-click the downloaded ZIP file to extract the folder containing the application
3. Run the Game
   * Navigate to the folder created from the zip
   * Double-click on the "VGW_Game" application to open the game
   ### IMPORTANT NOTE ABOUT MacOS SECURITY:
   Since I am not a verified developer, macOS may block the application from opening and display a message like: ""VGW_Game” is damaged 
   and can’t be opened. You should move it to the Trash". Do not move it to the trash. This is a standard security warning for apps from independent developers.
   #### Instead, follow these steps to safely open the app:
   * Right-click on the game folder (most likely titled "Takeoff_Pygame")
   * Select "New Terminal at Folder" to open the Mac terminal at the location of the game folder
   * In the Terminal window, type the following command and press enter. "xattr -cr ."
     - This will bypass Mac's security restriction for that folder ONLY. This will only affect that game folders contents and will NOT affect anything outside 
     of the folder
   * Now, the restriction is removed and you should be able to double click on the application titled "VGW_Game" to play the game

## Through Python in Command line on All Devices:
This game was not made on a Windows device, so there is no direct ".exe" application for Windows devices. To run the game on Windows, Mac, and Linux, you will need to have Python and Pygame installed and run the Python script through your system's command line.
1. Download the Game Files
   * Navigate to my "Takeoff-Pygame" repository
   * Click the green "Code" button at the top of the page
   * Click "Download ZIP" at the bottom of the dropdown menu
   * After downloading, extract (unzip) the folder so you can access the necessary game files, including the Python script and all assets (images and audio)
2. Installing Python
   * Go to https://www.python.org
   * Click Downloads -> click the big yellow button corresponding to latest Python version for your corresponding device
   * Important for Windows users:
     During Python installation, check the box that says "Add Python to PATH" before clicking "Install"
3. Install Pygame
   * Open your system's command line:
     - On Windows, open "Command Prompt" or search for it in the Start Menu
     - On MacOs, open "Terminal" or search for it in the Launchpad or Spotlight
   * Install Pygame by typing:
     - "pip install pygame" or
     - "pip3 install pygame" if you downloaded Python 3
4. Navigate to the Game Folder in the command line
   * Easy way (Recommended):
     - For MacOS users, you can easily right-click the game folder and select "New Terminal at Folder" to skip typing the path manually. This will open your terminal at the exact 
       location of that folder
     - For Windows users, you can right-click the folder and select "Open in Terminal" on newer Windows 11 versions or select "Open Command Prompt Here" on older Windows versions
   * Manual way (if you prefer typing manually in the command line):
     - Example for MacOS, type something like "cd ~/Downloads/Takeoff_Pygame-main" or whatever your specific path is to move to the game folder 
     - For Windows, it may look something like "cd C:\Users\YourUsername\Downloads\Takeoff-Pygame-main"
5. Run the Game
   * In the command line inside the game folder, type:
     - "python VGW_Game.py" or
     - "python3 VGW_Game.py" if you installed Python 3
   * The game window should open automatically and play will begin


# My high score is 1:47! I would love to know how long you survived and if you were able to beat my score!

