# Fly Swatter Game

This is a simple game where the player tries to swat as many flies as possible within a time limit. The game consists of a player-controlled swatter and several randomly moving flies on the screen. When the swatter collides with a fly, the fly dies and the player earns a point.

## How to Play

Launch the game by running the "fly_swatter2.py" file.
Click the "Start Game" button in the launcher window that appears.
The game screen will appear with flies moving around and a swatter at the bottom of the screen.
Move the swatter with the mouse to try and collide with the flies.
Click the left mouse button to swat a fly.
The game is over when the time limit runs out or the player reaches the maximum level of 5.
The player's score is displayed at the end of the game.

### Requirements

Python 3.x installed on your system.
Pygame module installed.
Tkinter module installed.
Files

"fly_swatter.py" - main game code.
"fly1.png" - image file of fly animation.
"fly2.png" - image file of fly animation.
"dead_fly.png" - image file of dead fly.
"swatter.png" - image file of swatter.
"buzz.mp3" - audio file for fly buzz sound.
"swat.wav" - audio file for swat sound.

### Game Features
Flies move randomly on the screen and bounce off the edges.
Flies are animated with two different images to create the illusion of flight.
Swatter is controlled by the mouse.
Sound effects are played when the player swats a fly or during the game.
The game has a time limit of 30 seconds.
The game has 5 levels, with the number of flies increasing by 5 for each level.
The game keeps track of the player's score.
The game is launched through a separate tkinter window.

### Known Issues

- Sometimes the flies stop moving randomly, which causes the game to freeze.
- The game crashes at a score of 13, for reasons that are currently unknown.

## Contributors
This game was created by kram254[Emmanuel Ndaliro] as a project to showcase my programming skills. It may be modified and redistributed under the terms of the MIT license.

## Launching the Game
Once you have cloned or downloaded the code repository, navigate to the Fly_Swatter directory and run the fly_swatter2.py file.

### Playing the Game
- When you launch the game, you will see a window with the title "Fly Swatter". The objective of the game is to swat as many flies as possible within the given time limit of 30 seconds. 
- Each fly swatted earns you one point. There are five levels in the game, and you must reach the point goal for each level to progress to the next level. The point goal is the level number multiplied by the initial number of flies.

- To swat a fly, click on the fly with your left mouse button. If you successfully swat a fly, you will hear a swatting sound, and the fly will disappear from the screen. If you miss a fly or the time limit expires, the game is over.

### Game Mechanics
- The game is programmed in Python using the Pygame library. The game window has a resolution of 800 x 600 pixels, and the game runs at 60 frames per second.

- The flies are programmed to move around randomly on the screen, bouncing off the edges of the screen when they reach them. The flies are also animated, with two different fly images used to create the illusion of movement.

- The game has two sound effects, a buzzing sound that plays continuously in the background and a swatting sound that plays when you successfully swat a fly.