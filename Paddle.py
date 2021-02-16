class paddle:

    def __init__(self):
        self.x = 25
        self.y = 1
        self.oldx = 25
        self.oldy = 1
        self.size = 5
        self.speed = 2

    def move(self, dir):
        # print(dir)
        self.oldx = self.x
        self.oldy = self.y
        if dir == 'a' or dir == 'A':
            if self.x-self.size-self.speed > 0:
                self.x = self.x - self.speed
        if dir == 'd' or dir == 'D':
            if self.x+self.size+self.speed+1 < 100:
                self.x = self.x + self.speed

Paddle = paddle()