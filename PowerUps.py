from Paddle import Paddle
from Ball import Ball
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
        self.time = 0

    def move(self):
        if self.active == True:
            cur = datetime.now()
            cur = (cur - self.time).total_seconds()
            if(cur > 30):
                Paddle.oldsize = Paddle.size
                Paddle.size = Paddle.size-2
                return -1
        else:
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
        self.time = 0

    def move(self):
        if self.active == True:
            cur = datetime.now()
            cur = (cur - self.time).total_seconds()
            if(cur > 30):
                Paddle.oldsize = Paddle.size
                Paddle.size = Paddle.size+2
                return -1
        else:
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
        self.time = 0

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
            if self.y == 2:
                if self.x >= (Paddle.x - Paddle.size) and self.x <= (Paddle.x + Paddle.size):
                    if Ball.vx > 1 or Ball.vx < -1:
                        Ball.vx = Ball.vx + Ball.vx/abs(Ball.vx)
                    if Ball.vy > 1 or Ball.vy < -1:
                        Ball.vy = Ball.vy + Ball.vy/abs(Ball.vy)
                    self.active = True
                    self.time = datetime.now()
                else:
                    return -1
            else:
                self.oldy = self.y
                self.y = self.y -1
        return 0

