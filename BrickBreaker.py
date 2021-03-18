from os import system
import sys
from Board import Board
from input import *
from Paddle import Paddle
import numpy as np
import Ball
import Brick
import Lines
import PowerUps
from random import randint
from datetime import datetime
import time

def startup():
    Ball.Balls.append(Ball.ball())

lett = ' '
no = 0

Lives = 4
Score = 0
powactiv = True
timer = datetime.now()
levelstart = datetime.now()
lastr = datetime.now()
_ = system('clear')

level = 1
Brick.level1()

Lines.Pows.append(PowerUps.expow(58, 43, 1, -1))

def clearlevel():
    Brick.Bricks.clear()
    Lines.lines.clear()
    Lines.lines.append({'x1':0, 'x2':0, 'y1':0, 'y2':49, 'd':'x', 'id':'wall', 'dir': 'r'}) 
    Lines.lines.append({'x1':99, 'x2':99, 'y1':0, 'y2':49, 'd':'x', 'id':'wall', 'dir': 'l'})
    Lines.lines.append({'x1':0, 'x2':99, 'y1':49, 'y2':49, 'd':'y', 'id':'wall', 'dir': 'd'})
    Lines.lines.append({'x1':Paddle.x-Paddle.size, 'x2':Paddle.x+Paddle.size, 'y1':Paddle.y, 'y2':Paddle.y, 'd':'y', 'id':'paddle', 'dir': 'u'})
    Lines.lines.append({'x1':0, 'x2':99, 'y1':0, 'y2':0, 'd':'r', 'id':'wall', 'dir': 'u'})
    for i in range(np.shape(Board.grid)[0]):
        for j in range(np.shape(Board.grid)[1]):
            if i == 0:
                Board.grid[i][j] = '-'
            elif i == np.shape(Board.grid)[0]-1:
                Board.grid[i][j] = '_'
            elif i == np.shape(Board.grid)[0]-3:
                Board.grid[i][j] = '-'
            elif j == 0:
                Board.grid[i][j] = '|'
            elif j == np.shape(Board.grid)[1]-1:
                Board.grid[i][j] = '|'
            else:
                Board.grid[i][j] = ' '
    Lines.count = 0


while Lives > 0:
    # sys.exit()
    Board.grid[50][2] = 'S'
    Board.grid[50][3] = 'c'
    Board.grid[50][4] = 'o'
    Board.grid[50][5] = 'r'
    Board.grid[50][6] = 'e'
    Board.grid[50][8] = '-'
    sk = Score
    for i in range(3):
        Board.grid[50][12-i] = str(sk%10)
        sk = sk/10

    Board.grid[50][44] = 'T'
    Board.grid[50][45] = 'i'
    Board.grid[50][46] = 'm'
    Board.grid[50][47] = 'e'
    Board.grid[50][49] = '-'
    Board.grid[50][53] = ':'

    cur = datetime.now()
    cur = (cur - timer).total_seconds()
    sec = cur %60
    minu = cur/60
    for i in range(2):
        Board.grid[50][52-i] = str(minu%10)
        minu = minu/10
    for i in range(2):
        Board.grid[50][55-i] = str(sec%10)
        sec = sec/10
    Board.grid[50][89] = 'L'
    Board.grid[50][90] = 'i'
    Board.grid[50][91] = 'v'
    Board.grid[50][92] = 'e'
    Board.grid[50][93] = 's'
    Board.grid[50][95] = '-'
    Board.grid[50][97] = str(Lives)

    if not Ball.Balls:
        Ball.Balls.append(Ball.ball())
        # Lines.start = True
        # Lines.Pows = []
        # Lines.grab = False
        Lines.through = False
        Paddle.oldsize = Paddle.size
        Paddle.size = 5
        Lives = Lives - 1

    if Paddle.size+Paddle.x >= 99:
        Paddle.x = 98 - Paddle.size
    if Paddle.x-Paddle.size <= 0:
        Paddle.x = 1 + Paddle.size
    for i in range(Paddle.oldsize*2 + 1):
        Board.grid[Paddle.oldy][Paddle.oldx-Paddle.oldsize+i] = ' ' 
    Paddle.oldsize = Paddle.size
    for i in range(Paddle.size*2 + 1):
        Board.grid[Paddle.y][Paddle.x-Paddle.size+i] = '='
    for boi in Ball.Balls:
        Board.grid[int(boi.oldy)][int(boi.oldx)] = ' '
        # print(boi.x, boi.y)
        Board.grid[int(boi.y)][int(boi.x)] = 'o'

    for boi in Brick.Bricks:
        if boi.peacock == True:
            boi.lives = 1 #randint(1, 3)
        if boi.lives == -2:
            continue
        elif boi.lives == 0:
            x = boi.x
            y = boi.y
            coun = boi.cnt
            Lines.lines.remove({'x1':x-0.5, 'x2':x+1.5, 'y1':y-0.5, 'y2':y-0.5, 'd':'y', 'id':coun, 'dir': 'd'})
            Lines.lines.remove({'x1':x-0.5, 'x2':x+1.5, 'y1':y+1.5, 'y2':y+1.5, 'd':'y', 'id':coun, 'dir': 'u'})
            Lines.lines.remove({'x1':x+1.5, 'x2':x+1.5, 'y1':y-0.5, 'y2':y+1.5, 'd':'x', 'id':coun, 'dir': 'r'})
            Lines.lines.remove({'x1':x-0.5, 'x2':x-0.5, 'y1':y-0.5, 'y2':y+1.5, 'd':'x', 'id':coun, 'dir': 'l'})
            # if no < 3:
            #     Lines.Pows.append(PowerUps.mlpow(x, y))
            #     no = no+1
            Score = Score+10


            pick = 1
            # pick = randint(1, 25)
            # if powactiv == True:
            if pick == 1:
                Lines.Pows.append(PowerUps.expow(x, y, boi.vx, boi.vy))
            # elif pick == 2:
            #     Lines.Pows.append(PowerUps.shpow(x, y))
            # elif pick == 3:
            #     Lines.Pows.append(PowerUps.mlpow(x, y))
            # elif pick == 4:
            #     Lines.Pows.append(PowerUps.fspow(x, y))
            # elif pick == 5:
            #     Lines.Pows.append(PowerUps.trpow(x, y))
            # elif pick == 6:
            #     Lines.Pows.append(PowerUps.grpow(x, y))

            # Brick.Bricks.remove(boi)
            boi.lives = -2
            Board.grid[boi.y][boi.x] = ' '
            Board.grid[boi.y+1][boi.x] = ' '
            Board.grid[boi.y][boi.x+1] = ' '
            Board.grid[boi.y+1][boi.x+1] = ' '
            if boi.boom == True:
                Score = Score + 10
                for boi2 in Brick.Bricks:
                    if boi2.x >= x-2 and boi2.x <= x+2:
                        if boi2.y >= y-2 and boi2.y <= y+2:
                            if boi2.lives != -2:
                                boi2.peacock = False
                                boi2.lives = 0
        elif boi.boom == True:
            Board.grid[boi.y][boi.x] = 'X'
            Board.grid[boi.y+1][boi.x] = 'X'
            Board.grid[boi.y][boi.x+1] = 'X'
            Board.grid[boi.y+1][boi.x+1] = 'X'
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

    # if powactiv == False:
    #     if level == 2:
    #         Brick.level2()
    #         Score = 510

    powactiv = True
    for boi in Lines.Pows:
        Board.grid[boi.oldy][boi.oldx] = ' '
        if boi.active == False:
            if boi.type == 'exp':
                Board.grid[boi.y][boi.x] = 'E'
            elif boi.type == 'shr':
                Board.grid[boi.y][boi.x] = 'S'
            elif boi.type == 'fst':
                Board.grid[boi.y][boi.x] = 'F'
            elif boi.type == 'grb':
                Board.grid[boi.y][boi.x] = 'G'
            elif boi.type == 'thr':
                Board.grid[boi.y][boi.x] = 'T'
            elif boi.type == 'mlt':
                Board.grid[boi.y][boi.x] = 'M'

    # _ = system('clear')
    # print(u'\u001b[{10}F')
    sys.stdout.write(u"\u001b[100F")
    if isinstance(lett, str):
        if ord(lett) == 3:
            sys.stdout.flush()
            _ = system('clear')
            break
        elif lett == 'p':
            for boi in Ball.Balls:
                if boi.start == True:
                    boi.start = False
        elif lett == 'n':
            level+=1
            if level == 2:
                # Brick.Bricks.clear()
                clearlevel()
                Brick.level2()
                levelstart = datetime.now()
                score = 510
                # time.sleep(5)
                # for x in Brick.Bricks:
                #     if x.lives != -2:
                #         x.lives = 0
                # powactiv = False
            elif level == 3:
                Lives = -1
                # Ball.y = 25
    # else:
    #     print(Paddle.x, type(lett))
    
    # print('\n'.join(''.join(map(str, Board.grid[i])) for i in range(np.shape(Board.grid)[0]-1, -1, -1)))
    for i in range(51, -1, -1):
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
            elif Board.grid[i][j] == 'X':
                sys.stdout.write('\u001b[47m')
                sys.stdout.write('\u001b[30m')
            if i == 50:
                sys.stdout.write('\u001b[0m')
                
            sys.stdout.write(Board.grid[i][j])
            sys.stdout.write('\u001b[0m')
        print(' ')
    lett = input_to(Get())
    cur = datetime.now()
    cur = (cur - levelstart).total_seconds()
    if(cur > 5):
        cur = datetime.now()
        cur = (cur - lastr).total_seconds()
        if(cur > 2):
            lastr = datetime.now()
            clearlevel()
            for boi in temp_Brick:
                # print(boi)
                # time.sleep(10)
                if boi.y-1 == 0:
                    if boi.lives != -2:
                        Lives = -2
                        break
                if boi.lives == -2:
                    Brick.Bricks.append(Brick.brick_reg(200, 200, -2))
                elif boi.boom == True:
                    Brick.Bricks.append(Brick.brick_exp(boi.x, boi.y-1))
                elif boi.peacock == True:
                    Brick.Bricks.append(Brick.brick_rbow(boi.x, boi.y-1))
                else:
                    Brick.Bricks.append(Brick.brick_reg(boi.x, boi.y-1, boi.lives))
    if Score == 510:
        level+=1
        Brick.level2()
        levelstart = datetime.now()
        print("You have cleared all the bricks!")
        # sys.exit()
    Paddle.move(lett)
    # print(Ball)
    for boi in Ball.Balls:
        Board.grid[int(boi.y)][int(boi.x)] = ' '
        if boi.move() == -1:
            Ball.Balls.remove(boi)
    for bois in Lines.Pows:
        Board.grid[int(bois.y)][int(bois.x)] = ' '
        if bois.move() == -1:
            Lines.Pows.remove(bois)
    temp_Brick = list(Brick.Bricks)
    # print(temp_Brick)
    # time.sleep(5)
    # time.sleep(1)


if Lives == 0:
    print("Out of lives")
elif Lives == -1:
    print("You have completed the game")
elif Lives == -2:
    print("Game Over")
print("Thanks for playing!")

# print(Board.grid)

