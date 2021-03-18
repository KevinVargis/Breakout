# from Lines import lines
import Lines

# count = 0

class brick():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = -1
        # global count
        Lines.lines.append({'x1':x-0.5, 'x2':x+1.5, 'y1':y-0.5, 'y2':y-0.5, 'd':'y', 'id':Lines.count, 'dir': 'd'})
        Lines.lines.append({'x1':x-0.5, 'x2':x+1.5, 'y1':y+1.5, 'y2':y+1.5, 'd':'y', 'id':Lines.count, 'dir': 'u'})
        Lines.lines.append({'x1':x+1.5, 'x2':x+1.5, 'y1':y-0.5, 'y2':y+1.5, 'd':'x', 'id':Lines.count, 'dir': 'r'})
        Lines.lines.append({'x1':x-0.5, 'x2':x-0.5, 'y1':y-0.5, 'y2':y+1.5, 'd':'x', 'id':Lines.count, 'dir': 'l'})
        # Ball.lines.append({'x1':x, 'x2':x+1, 'y1':y, 'y2':y, 'd':'y', 'id':count})
        # Ball.lines.append({'x1':x, 'x2':x+1, 'y1':y+1, 'y2':y+1, 'd':'y', 'id':count})
        # Ball.lines.append({'x1':x+1, 'x2':x+1, 'y1':y, 'y2':y+1, 'd':'x', 'id':count})
        # Ball.lines.append({'x1':x, 'x2':x, 'y1':y, 'y2':y+1, 'd':'x', 'id':count})
        self.cnt = Lines.count
        Lines.count = Lines.count+1
        # print(Lines.count)

class brick_reg(brick):
    def __init__(self, x, y, lives):
        super().__init__(x, y)
        self.lives = lives
        self.boom = False
        self.peacock = False

class brick_rbow(brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lives = 3
        self.boom = False
        self.peacock = True

class brick_unbreak(brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lives = -1
        self.boom = False
        self.peacock = False

class brick_exp(brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lives = 1
        self.boom = True
        self.peacock = False

# class brick3(brick):
#     def __init__(self, x, y):
#         super().__init__(x, y)
#         self.lives = 3
Bricks = []

def level1():
    for i in range(8):
        if i%2 == 0:
            Bricks.append(brick_rbow(21+(i*2), 25))
        else:
            Bricks.append(brick_reg(21+(i*2), 25, 1))

    for i in range(8):
        if i%2 == 0:
            Bricks.append(brick_rbow(37+(i*2), 25))
        else:
            Bricks.append(brick_reg(37+(i*2), 25, 2))

    for i in range(8):
        if i%2 == 0:
            Bricks.append(brick_rbow(53+(i*2), 25))
        else:
            Bricks.append(brick_reg(53+(i*2), 25, 3))

    for i in range(6):
        Bricks.append(brick_exp(39+(i*2), 27))

    for i in range(6):
        Bricks.append(brick_exp(39+(i*2), 33))

    for i in range(13):
        Bricks.append(brick_unbreak(15+(i*5), 35))
    

def level2():
    for i in range (1, 11):
        Bricks.append(brick_reg(50-2*i, 15+2*i, 2))
        Bricks.append(brick_reg(50+2*i, 15+2*i, 2))
    for i in range (0, 5):
        Bricks.append(brick_reg(40+2*i, 35+2*i, 2))
        Bricks.append(brick_reg(60-2*i, 35+2*i, 2))
    for i in range(15):
        Bricks.append(brick_exp(50, 17+2*i))

    Bricks.append(brick_reg(50, 15, 2))
    Bricks.append(brick_reg(50, 45, 2))
    
# Bricks = [brick_reg(25, 25, 1), brick_reg(27, 25, 1), brick_reg(29, 25, 1), 
#            brick_reg(31, 25, 1), brick_reg(33, 25, 1), brick_reg(35, 25, 1),
#            brick_reg(37, 25, 2), brick_reg(39, 25, 2), brick_reg(41, 25, 2), 
#            brick_reg(43, 25, 2), brick_reg(45, 25, 2), brick_reg(49, 25, 2)
        #    ]

# bricks.append(brick2(2,3))
# bricks.append(brick3(2,4))

# for ob in bricks:
    # print(ob.indest)