from Paddle import Paddle
import Ball
from math import sqrt
import Lines
from datetime import datetime
import time

def hits(x1, y1, x2, y2, x3, y3, x4, y4, d, id, dir):
    div = ((y4-y3) * (x2-x1)) - ((x4-x3) * (y2-y1))
    if (div != 0):
        ua = (((x4-x3) * (y1-y3)) - ((y4-y3) * (x1-x3))) / div
        if (ua >= 0) and (ua <= 1):
            ub = (((x2-x1) * (y1-y3)) - ((y2-y1) * (x1-x3))) / div
            if ((ub >= 0) and (ub <= 1)):
                x = x1 + (ua * (x2-x1))
                y = y1 + (ua * (y2-y1))
                if dir == 'l' and x1 > x3:
                    return
                elif dir == 'r' and x1 < x3:
                    return
                elif dir == 'u' and y1 < y3:
                    return
                elif dir == 'd' and y1 > y3:
                    return
                else:
                    return { 'x': x, 'y': y, 'd': d, 'dist': sqrt( (x - x1)**2 + (y - y1)**2 ), 'id': id}
    return

def moo(ting):
    cur = datetime.now()
    cur = (cur - ting.time).total_seconds()
    if cur > 0.1:
        ting.time = datetime.now()
        ting.oldx = ting.x
        ting.o = ting.oldy
        ting.oldy = ting.y
        ting.x = ting.x + ting.vx
        ting.y = ting.y + ting.vy
        for l in Lines.lines:
            # print(l['id'])
            if l['id'] == 'paddle':
                # print("bogalooooo")
                l['x1']=Paddle.x-Paddle.size 
                l['x2']=Paddle.x+Paddle.size
                l['y1']=Paddle.y 
                l['y2']=Paddle.y 
                
        ting.hit = [hits(ting.oldx, ting.oldy, ting.x, ting.y, l['x1'], l['y1'], l['x2'], l['y2'], l['d'], l['id'], l['dir']) for l in Lines.lines]
        # print('\u001b[0K', end=" ")
        # print(ting.hit)
        
        mini = 1000
        cou = 0
        pos = -1
        for i in ting.hit:
            if i != None and (i['id'] == 'wall' or i['id'] == 'paddle'):
                if i['dist'] < mini:
                    mini = i['dist']
                    pos = cou
            cou = cou + 1
        # print('hmm', pos)
        if pos != -1:
            if(ting.hit[pos]['d'] == 'r'):
                # ting.reset(ting.oldx, ting.oldy)
                return -1
            else:
                if ting.hit[pos]['id'] == 'wall':
                    if ting.vx != 0:
                        ting.x = int(ting.hit[pos]['x'] - ting.vx/abs(ting.vx))
                    if ting.vy != 0:
                        ting.y = int(ting.hit[pos]['y'] - ting.vy/abs(ting.vy))

                elif ting.hit[pos]['id'] == 'paddle':
                    ting.active = True
                    Paddle.oldsize = Paddle.size
                    Paddle.size = Paddle.size+2
                    ting.time = datetime.now()
                    # print("kachow")
                    # time.sleep(2)

                # print(ting.x)
                # print(ting.y)
                if ting.hit[pos]['d'] == 'y':
                    ting.vy = ting.vy * -1
                else:
                    ting.vx = ting.vx * -1
            if ting.y == ting.o:
                # if ting.y == 48:
                #     ting.y = ting.y -1
                # el
                if ting.y != 2:
                    ting.y = ting.y + 1
                # return
        if ting.y >= 49:
            ting.y = 48
            ting.vy = abs(ting.vy) * -1
        if ting.x >= 99:
            ting.x = 98
            ting.vx = abs(ting.vx) * -1
        if ting.y <= 0:
            ting.y = 1
            ting.vy = abs(ting.vy)
        if ting.x <= 0:
            ting.x = 1
            ting.vx = abs(ting.vx)
        # if Lines.grab == True and self.y == 2 and self.x >= (Paddle.x - Paddle.size) and self.x <= (Paddle.x + Paddle.size):
        #     self.start = True
        #     self.offset = Paddle.x - self.x
    return 0

class powerup:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.o = y
        self.vx = vx
        self.vy = vy
        self.oldx = x
        self.oldy = y

class expow(powerup):
    def __init__(self, x, y, vx, vy):
        super().__init__(x, y, vx, vy)
        self.type = "exp"
        self.active = False
        self.time = datetime.now()

    def move(self):
        # print(self)
        # time.sleep(2)
        if self.active == True:
            cur = datetime.now()
            cur = (cur - self.time).total_seconds()
            if(cur > 30):
                Paddle.oldsize = Paddle.size
                Paddle.size = Paddle.size-2
                return -1
        else:
            return moo(self)
            # cur = datetime.now()
            # cur = (cur - self.time).total_seconds()
            # if cur > 0.1:
            #     if self.y == 2:
            #         if self.x >= (Paddle.x - Paddle.size) and self.x <= (Paddle.x + Paddle.size):
            #             Paddle.oldsize = Paddle.size
            #             Paddle.size = Paddle.size+2
            #             self.active = True
            #             self.time = datetime.now()
            #         else:
            #             return -1
            #     else:
            #         self.oldy = self.y
            #         self.y = self.y -1
        # return 0

class shpow(powerup):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = "shr"
        self.active = False
        self.time = datetime.now()

    def move(self):
        if self.active == True:
            cur = datetime.now()
            cur = (cur - self.time).total_seconds()
            if(cur > 30):
                Paddle.oldsize = Paddle.size
                Paddle.size = Paddle.size+2
                return -1
        else:
            cur = datetime.now()
            cur = (cur - self.time).total_seconds()
            if cur > 0.1:
                if self.y == 2:
                    if self.x >= (Paddle.x - Paddle.size) and self.x <= (Paddle.x + Paddle.size):
                        Paddle.oldsize = Paddle.size
                        if Paddle.size - 2 < 1:
                            return -1
                        Paddle.size = Paddle.size-2
                        self.active = True
                        self.time = datetime.now()
                    else:
                        return -1
                else:
                    self.oldy = self.y
                    self.y = self.y -1
        return 0

class fspow(powerup):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = "fst"
        self.active = False
        self.time = datetime.now()

    def move(self):
        if self.active == True:
            cur = datetime.now()
            cur = (cur - self.time).total_seconds()
            if(cur > 30):
                for bol in Ball.Balls:
                    if bol.vx > 1 or bol.vx < -1:
                        bol.vx = bol.vx - bol.vx/abs(bol.vx)
                    if bol.vy > 1 or bol.vy < -1:
                        bol.vy = bol.vy - bol.vy/abs(bol.vy)
                return -1
        else:
            cur = datetime.now()
            cur = (cur - self.time).total_seconds()
            if cur > 0.1:
                if self.y == 2:
                    if self.x >= (Paddle.x - Paddle.size) and self.x <= (Paddle.x + Paddle.size):
                        for bol in Ball.Balls:
                            if bol.vx != 0:
                                bol.vx = bol.vx + bol.vx/abs(bol.vx)
                            if bol.vy != 0:
                                bol.vy = bol.vy + bol.vy/abs(bol.vy)
                        self.active = True
                        self.time = datetime.now()
                    else:
                        return -1
                else:
                    self.oldy = self.y
                    self.y = self.y -1
        return 0

class grpow(powerup):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = "grb"
        self.active = False
        self.time = datetime.now()

    def move(self):
        if self.active == True:
            cur = datetime.now()
            cur = (cur - self.time).total_seconds()
            if(cur > 30):
                Lines.grab = False
                return -1
            Lines.grab = True
        else:
            cur = datetime.now()
            cur = (cur - self.time).total_seconds()
            if cur > 0.1:
                if self.y == 2:
                    if self.x >= (Paddle.x - Paddle.size) and self.x <= (Paddle.x + Paddle.size):
                        Lines.grab = True
                        self.active = True
                        self.time = datetime.now()
                    else:
                        return -1
                else:
                    self.oldy = self.y
                    self.y = self.y -1
        return 0

class trpow(powerup):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = "thr"
        self.active = False
        self.time = datetime.now()

    def move(self):
        if self.active == True:
            cur = datetime.now()
            cur = (cur - self.time).total_seconds()
            if(cur > 30):
                Lines.through = False
                return -1
            Lines.through = True
        else:
            cur = datetime.now()
            cur = (cur - self.time).total_seconds()
            if cur > 0.1:
                if self.y == 2:
                    if self.x >= (Paddle.x - Paddle.size) and self.x <= (Paddle.x + Paddle.size):
                        Lines.through = True
                        self.active = True
                        self.time = datetime.now()
                    else:
                        return -1
                else:
                    self.oldy = self.y
                    self.y = self.y -1
        return 0

class mlpow(powerup):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = "mlt"
        self.active = False
        self.time = datetime.now()

    def move(self):
        if self.active == True:
            cur = datetime.now()
            cur = (cur - self.time).total_seconds()
            if(cur > 30):
                num = len(Ball.Balls)
                if num > 1:
                    while len(Ball.Balls) > (num/2):
                        Ball.Balls.pop()
                return -1
        else:
            cur = datetime.now()
            cur = (cur - self.time).total_seconds()
            if cur > 0.1:
                if self.y == 2:
                    if self.x >= (Paddle.x - Paddle.size) and self.x <= (Paddle.x + Paddle.size):
                        num = len(Ball.Balls)
                        for i in range(num):
                            tem = Ball.ball()
                            tem.x = Ball.Balls[i].x
                            tem.y = Ball.Balls[i].y
                            tem.oldx = Ball.Balls[i].oldx
                            tem.oldy = Ball.Balls[i].oldy
                            tem.vx = Ball.Balls[i].vx *-1 + 1
                            tem.start = False
                            Ball.Balls.append(tem)
                            # tem.vx = Ball.Balls[i].x
                        self.active = True
                        self.time = datetime.now()
                    else:
                        return -1
                else:
                    self.oldy = self.y
                    self.y = self.y -1
        return 0

