from Paddle import Paddle
from math import sqrt
from datetime import datetime
from Brick import Bricks
import Lines

# lines = [{'x1':0, 'x2':0, 'y1':0, 'y2':49, 'd':'x', 'id':'wall', 'dir': 'r'}, 
#             {'x1':99, 'x2':99, 'y1':0, 'y2':49, 'd':'x', 'id':'wall', 'dir': 'l'}, 
#             {'x1':0, 'x2':99, 'y1':49, 'y2':49, 'd':'y', 'id':'wall', 'dir': 'd'},
#             {'x1':Paddle.x-2, 'x2':Paddle.x+2, 'y1':Paddle.y, 'y2':Paddle.y, 'd':'y', 'id':'paddle', 'dir': 'u'},
#             {'x1':0, 'x2':99, 'y1':0, 'y2':0, 'd':'r', 'id':'wall', 'dir': 'u'}]


class ball:
    # lines = [{'x1':0, 'x2':0, 'y1':0, 'y2':49, 'd':'x'}, {'x1':99, 'x2':99, 'y1':0, 'y2':49, 'd':'x'}, {'x1':0, 'x2':99, 'y1':49, 'y2':49, 'd':'y'}]
    def __init__(self):
        self.x = 50
        self.o = 2
        self.y = 2
        self.oldx = 25
        self.oldy = 2
        self.vx = 0
        self.vy = 2
        self.time = datetime.now()
        
    def reset(self, x, y):
        self.x = 50
        self.y = 2
        self.o = y
        self.oldx = x
        self.oldy = y
        # self.vx = 0
        # self.vy = 0
        # global Lines.start
        Lines.start = True
    
    def hits(self, x1, y1, x2, y2, x3, y3, x4, y4, d, id, dir):
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


    def move(self):
        # global Lines.start
        # print(Lines.start)
        if Lines.start == True:
            self.oldx = self.x
            self.o = self.oldy
            self.oldy = self.y
            self.x = Paddle.x
        else:
            cur = datetime.now()
            cur = (cur - self.time).total_seconds()
            if cur > 0.1:
                self.time = datetime.now()
                self.oldx = self.x
                self.o = self.oldy
                self.oldy = self.y
                self.x = self.x + self.vx
                self.y = self.y + self.vy
                for l in Lines.lines:
                    # print(l['id'])
                    if l['id'] == 'paddle':
                        # print("bogalooooo")
                        l['x1']=Paddle.x-Paddle.size 
                        l['x2']=Paddle.x+Paddle.size
                        l['y1']=Paddle.y 
                        l['y2']=Paddle.y 
                        
                self.hit = [self.hits(self.oldx, self.oldy, self.x, self.y, l['x1'], l['y1'], l['x2'], l['y2'], l['d'], l['id'], l['dir']) for l in Lines.lines]
                # print('\u001b[0K', end=" ")
                # print(self.hit)
                print('\u001b[0K', end=" ")
                print(self.x, self.y)
                mini = 1000
                cou = 0
                pos = -1
                for i in self.hit:
                    if i != None:
                        if i['dist'] < mini:
                            mini = i['dist']
                            pos = cou
                    cou = cou + 1
                # print('hmm', pos)
                if pos != -1:
                    if(self.hit[pos]['d'] == 'r'):
                        self.reset(self.oldx, self.oldy)
                    else:
                        if self.hit[pos]['id'] == 'wall':
                            if self.vx != 0:
                                self.x = int(self.hit[pos]['x'] - self.vx/abs(self.vx))
                            if self.vy != 0:
                                self.y = int(self.hit[pos]['y'] - self.vy/abs(self.vy))

                        elif self.hit[pos]['id'] == 'paddle':
                            if self.vx != 0:
                                self.x = int(self.hit[pos]['x'] - self.vx/abs(self.vx))
                            if self.vy != 0:
                                self.y = int(self.hit[pos]['y'] - self.vy/abs(self.vy))
                            if self.x < Paddle.x:
                                if self.x - Paddle.x + Paddle.size < Paddle.size/2:
                                    self.vx = self.vx - 2
                                else:
                                    self.vx = self.vx -1
                            elif self.x > Paddle.x:
                                if Paddle.x + Paddle.size - self.x < Paddle.size/2:
                                    self.vx = self.vx + 2
                                else:
                                    self.vx = self.vx + 1
                        else:
                            self.x = int(self.hit[pos]['x'])
                            self.y = int(self.hit[pos]['y'])
                            if Bricks[self.hit[pos]['id']].lives != -1:
                                Bricks[self.hit[pos]['id']].lives = Bricks[self.hit[pos]['id']].lives - 1;
                        # print(self.x)
                        # print(self.y)
                        if self.hit[pos]['d'] == 'y':
                            self.vy = self.vy * -1
                        else:
                            self.vx = self.vx * -1
                    if self.y == self.o:
                        # if self.y == 48:
                        #     self.y = self.y -1
                        # el
                        if self.y != 2:
                            self.y = self.y + 1
                        # return

Ball = ball()