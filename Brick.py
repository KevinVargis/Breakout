from Lines import lines

count = 0

class brick():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        global count
        lines.append({'x1':x-0.5, 'x2':x+1.5, 'y1':y-0.5, 'y2':y-0.5, 'd':'y', 'id':count, 'dir': 'd'})
        lines.append({'x1':x-0.5, 'x2':x+1.5, 'y1':y+1.5, 'y2':y+1.5, 'd':'y', 'id':count, 'dir': 'u'})
        lines.append({'x1':x+1.5, 'x2':x+1.5, 'y1':y-0.5, 'y2':y+1.5, 'd':'x', 'id':count, 'dir': 'r'})
        lines.append({'x1':x-0.5, 'x2':x-0.5, 'y1':y-0.5, 'y2':y+1.5, 'd':'x', 'id':count, 'dir': 'l'})
        # Ball.lines.append({'x1':x, 'x2':x+1, 'y1':y, 'y2':y, 'd':'y', 'id':count})
        # Ball.lines.append({'x1':x, 'x2':x+1, 'y1':y+1, 'y2':y+1, 'd':'y', 'id':count})
        # Ball.lines.append({'x1':x+1, 'x2':x+1, 'y1':y, 'y2':y+1, 'd':'x', 'id':count})
        # Ball.lines.append({'x1':x, 'x2':x, 'y1':y, 'y2':y+1, 'd':'x', 'id':count})
        self.cnt = count
        count = count+1

class brick_reg(brick):
    def __init__(self, x, y, lives):
        super().__init__(x, y)
        self.lives = lives
        self.boom = False

class brick_unbreak(brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lives = -1
        self.boom = False

class brick_exp(brick):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lives = 1
        self.boom = True

# class brick3(brick):
#     def __init__(self, x, y):
#         super().__init__(x, y)
#         self.lives = 3
Bricks = []
for i in range(8):
    Bricks.append(brick_reg(21+(i*2), 25, 1))

for i in range(8):
    Bricks.append(brick_reg(37+(i*2), 25, 2))

for i in range(8):
    Bricks.append(brick_reg(53+(i*2), 25, 3))

for i in range(6):
    Bricks.append(brick_exp(39+(i*2), 27))

for i in range(6):
    Bricks.append(brick_exp(39+(i*2), 33))

for i in range(13):
    Bricks.append(brick_unbreak(15+(i*5), 35))
# Bricks = [brick_reg(25, 25, 1), brick_reg(27, 25, 1), brick_reg(29, 25, 1), 
#            brick_reg(31, 25, 1), brick_reg(33, 25, 1), brick_reg(35, 25, 1),
#            brick_reg(37, 25, 2), brick_reg(39, 25, 2), brick_reg(41, 25, 2), 
#            brick_reg(43, 25, 2), brick_reg(45, 25, 2), brick_reg(49, 25, 2)
        #    ]

# bricks.append(brick2(2,3))
# bricks.append(brick3(2,4))

# for ob in bricks:
    # print(ob.indest)