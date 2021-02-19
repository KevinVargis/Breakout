from Paddle import Paddle
import Ball
import Lines
from datetime import datetime

class powerup:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.oldx = x
        self.oldy = y

class expow(powerup):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = "exp"
        self.active = False
        self.time = datetime.now()

    def move(self):
        if self.active == True:
            cur = datetime.now()
            cur = (cur - self.time).total_seconds()
            if(cur > 30):
                Paddle.oldsize = Paddle.size
                Paddle.size = Paddle.size-2
                return -1
        else:
            cur = datetime.now()
            cur = (cur - self.time).total_seconds()
            if cur > 0.1:
                if self.y == 2:
                    if self.x >= (Paddle.x - Paddle.size) and self.x <= (Paddle.x + Paddle.size):
                        Paddle.oldsize = Paddle.size
                        Paddle.size = Paddle.size+2
                        self.active = True
                        self.time = datetime.now()
                    else:
                        return -1
                else:
                    self.oldy = self.y
                    self.y = self.y -1
        return 0

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
                if Ball.vx > 1 or Ball.vx < -1:
                   Ball.vx = Ball.vx - Ball.vx/abs(Ball.vx)
                if Ball.vy > 1 or Ball.vy < -1:
                   Ball.vy = Ball.vy - Ball.vy/abs(Ball.vy)
                return -1
        else:
            cur = datetime.now()
            cur = (cur - self.time).total_seconds()
            if cur > 0.1:
                if self.y == 2:
                    if self.x >= (Paddle.x - Paddle.size) and self.x <= (Paddle.x + Paddle.size):
                        if Ball.vx != 0:
                            Ball.vx = Ball.vx + Ball.vx/abs(Ball.vx)
                        if Ball.vy != 0:
                            Ball.vy = Ball.vy + Ball.vy/abs(Ball.vy)
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

