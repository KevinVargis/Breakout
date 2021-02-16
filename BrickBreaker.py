from os import system
import sys
from Board import Board
from input import *
from Paddle import Paddle
import numpy as np
from Ball import Ball
from Brick import Bricks
import Lines

lett = ' '
no = 0

_ = system('clear')

while True:
    

    for i in range(Paddle.size*2 + 1):
        Board.grid[Paddle.oldy][Paddle.oldx-Paddle.size+i] = ' ' 
    for i in range(Paddle.size*2 + 1):
        Board.grid[Paddle.y][Paddle.x-Paddle.size+i] = '='
    Board.grid[Ball.oldy][Ball.oldx] = ' '
    Board.grid[Ball.y][Ball.x] = 'o'
    for boi in Bricks:
        if boi.lives == -2:
            continue
        elif boi.lives == 0:
            x = boi.x
            y = boi.y
            count = boi.cnt
            Lines.lines.remove({'x1':x-0.49, 'x2':x+1.49, 'y1':y-0.49, 'y2':y-0.49, 'd':'y', 'id':count, 'dir': 'd'})
            Lines.lines.remove({'x1':x-0.49, 'x2':x+1.49, 'y1':y+1.49, 'y2':y+1.49, 'd':'y', 'id':count, 'dir': 'u'})
            Lines.lines.remove({'x1':x+1.49, 'x2':x+1.49, 'y1':y-0.49, 'y2':y+1.49, 'd':'x', 'id':count, 'dir': 'r'})
            Lines.lines.remove({'x1':x-0.49, 'x2':x-0.49, 'y1':y-0.49, 'y2':y+1.49, 'd':'x', 'id':count, 'dir': 'l'})
        
            # Bricks.remove(boi)
            boi.lives = -2
            Board.grid[boi.y][boi.x] = ' '
            Board.grid[boi.y+1][boi.x] = ' '
            Board.grid[boi.y][boi.x+1] = ' '
            Board.grid[boi.y+1][boi.x+1] = ' '
        else:
            Board.grid[boi.y][boi.x] = str(boi.lives)
            Board.grid[boi.y+1][boi.x] = str(boi.lives)
            Board.grid[boi.y][boi.x+1] = str(boi.lives)
            Board.grid[boi.y+1][boi.x+1] = str(boi.lives)
    # _ = system('clear')
    # print(u'\u001b[{10}F')
    sys.stdout.write(u"\u001b[100F")
    if isinstance(lett, str):
        if ord(lett) == 3:
            sys.stdout.flush()
            _ = system('clear')
            break
        elif lett == 'p':
            if Lines.start == True:
                # print('hai')
                Ball.vy = 1
                Lines.start = False
                # Ball.y = 25
    # else:
    #     print(Paddle.x, type(lett))
    
    # print('\n'.join(''.join(map(str, Board.grid[i])) for i in range(np.shape(Board.grid)[0]-1, -1, -1)))
    for i in range(49, -1, -1):
        for j in range(100):
            if Board.grid[i][j] == '3':
                sys.stdout.write('\u001b[41m')
            elif Board.grid[i][j] == '2':
                sys.stdout.write('\u001b[43m')
            elif Board.grid[i][j] == '1':
                sys.stdout.write('\u001b[42m')
            sys.stdout.write(Board.grid[i][j])
            sys.stdout.write('\u001b[0m')
        print(' ')
    lett = input_to(Get())
    Paddle.move(lett)
    Ball.move()

# print(Board.grid)

