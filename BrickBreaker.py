from os import system
import sys
from Board import Board
from input import *
from Paddle import Paddle
import numpy as np
from Ball import Ball
from Brick import Bricks
import Lines
import PowerUps
from random import randint

lett = ' '
no = 0

_ = system('clear')

while True:
    

    for i in range(Paddle.oldsize*2 + 1):
        Board.grid[Paddle.oldy][Paddle.oldx-Paddle.oldsize+i] = ' ' 
    Paddle.oldsize = Paddle.size
    for i in range(Paddle.size*2 + 1):
        Board.grid[Paddle.y][Paddle.x-Paddle.size+i] = '='

    Board.grid[int(Ball.oldy)][int(Ball.oldx)] = ' '
    print(Ball.x, Ball.y)
    Board.grid[int(Ball.y)][int(Ball.x)] = 'o'

    for boi in Bricks:
        if boi.lives == -2:
            continue
        elif boi.lives == 0:
            x = boi.x
            y = boi.y
            count = boi.cnt
            Lines.lines.remove({'x1':x-0.499, 'x2':x+1.499, 'y1':y-0.499, 'y2':y-0.499, 'd':'y', 'id':count, 'dir': 'd'})
            Lines.lines.remove({'x1':x-0.499, 'x2':x+1.499, 'y1':y+1.499, 'y2':y+1.499, 'd':'y', 'id':count, 'dir': 'u'})
            Lines.lines.remove({'x1':x+1.499, 'x2':x+1.499, 'y1':y-0.499, 'y2':y+1.499, 'd':'x', 'id':count, 'dir': 'r'})
            Lines.lines.remove({'x1':x-0.499, 'x2':x-0.499, 'y1':y-0.499, 'y2':y+1.499, 'd':'x', 'id':count, 'dir': 'l'})
            if no < 3:
                # pick = randint(1, 2)
                # if pick == 1:
                #     Lines.Pows.append(PowerUps.expow(x, y))
                # elif pick == 2:
                #     Lines.Pows.append(PowerUps.shpow(x, y))
                Lines.Pows.append(PowerUps.fspow(x, y))
                no = no+1
            # Bricks.remove(boi)
            boi.lives = -2
            Board.grid[boi.y][boi.x] = ' '
            Board.grid[boi.y+1][boi.x] = ' '
            Board.grid[boi.y][boi.x+1] = ' '
            Board.grid[boi.y+1][boi.x+1] = ' '
        elif boi.lives == -1:
            Board.grid[boi.y][boi.x] = 'B'
            Board.grid[boi.y+1][boi.x] = 'B'
            Board.grid[boi.y][boi.x+1] = 'B'
            Board.grid[boi.y+1][boi.x+1] = 'B'
        else:
            Board.grid[boi.y][boi.x] = str(boi.lives)
            Board.grid[boi.y+1][boi.x] = str(boi.lives)
            Board.grid[boi.y][boi.x+1] = str(boi.lives)
            Board.grid[boi.y+1][boi.x+1] = str(boi.lives)

    for boi in Lines.Pows:
        Board.grid[boi.oldy][boi.oldx] = ' '
        if boi.active == False:
            if boi.type == 'exp':
                Board.grid[boi.y][boi.x] = 'X'
            elif boi.type == 'shr':
                Board.grid[boi.y][boi.x] = 'S'
            elif boi.type == 'fst':
                Board.grid[boi.y][boi.x] = 'F'

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
                Ball.vx = 0
                Lines.start = False
                # Ball.y = 25
    # else:
    #     print(Paddle.x, type(lett))
    
    # print('\n'.join(''.join(map(str, Board.grid[i])) for i in range(np.shape(Board.grid)[0]-1, -1, -1)))
    for i in range(49, -1, -1):
        sys.stdout.write('\u001b[150D')
        for j in range(100):
            if Board.grid[i][j] == '3':
                sys.stdout.write('\u001b[41m')
                sys.stdout.write('\u001b[37m')
            elif Board.grid[i][j] == '2':
                sys.stdout.write('\u001b[43m')
                sys.stdout.write('\u001b[37m')
            elif Board.grid[i][j] == '1':
                sys.stdout.write('\u001b[42m')
                sys.stdout.write('\u001b[37m')
            elif Board.grid[i][j] == 'B':
                sys.stdout.write('\u001b[46m')
                sys.stdout.write('\u001b[37m')
            sys.stdout.write(Board.grid[i][j])
            sys.stdout.write('\u001b[0m')
        print(' ')
    lett = input_to(Get())
    Paddle.move(lett)
    Ball.move()
    for bois in Lines.Pows:
        Board.grid[bois.y][bois.x] = ' '
        if bois.move() == -1:
            Lines.Pows.remove(bois)

# print(Board.grid)

