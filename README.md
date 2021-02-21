# DASS Assignment 2
Brick Breaker game

## Startup
- Naviagate to folder and run `python3 BrickBreaker.py`

## Main Objects
- Board - Instance of `board` class contains a 2D char grid which is repeatedly updated and printed to function as game screen
- Paddle - Instance of `paddle` class, contains parameters of the game paddle
    - `move()` - calculates the next positon of the object
- Balls - Array containing the instance(s) of balls currently in play, objects of `ball` class
    - `move()` - calculates the next positon of the object
    - `hits()` - given two lines, returns the location of any intersections, identity of the object collided with and distance of intercept from current position. The primary collision logic
- Pows - Array containing all active/onscreen powerups objects of parent class `powerup`
    - `move()` - calculates the next positon of the catchable powerup and handles status effects
- Bricks - Array of all the bricks in the game, instances deriving from `brick` class
- `BrickBreaker.py` - Uses results of all the given functions to update the game state and print the display. Keeps track of lives lost and score. Handles cleanup of destroyed bricks
