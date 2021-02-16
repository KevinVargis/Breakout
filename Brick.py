from Lines import lines

count = 0

class brick():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        global count
        lines.append({'x1':x-0.49, 'x2':x+1.49, 'y1':y-0.49, 'y2':y-0.49, 'd':'y', 'id':count, 'dir': 'd'})
        lines.append({'x1':x-0.49, 'x2':x+1.49, 'y1':y+1.49, 'y2':y+1.49, 'd':'y', 'id':count, 'dir': 'u'})
        lines.append({'x1':x+1.49, 'x2':x+1.49, 'y1':y-0.49, 'y2':y+1.49, 'd':'x', 'id':count, 'dir': 'r'})
        lines.append({'x1':x-0.49, 'x2':x-0.49, 'y1':y-0.49, 'y2':y+1.49, 'd':'x', 'id':count, 'dir': 'l'})
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

# class brick3(brick):
#     def __init__(self, x, y):
#         super().__init__(x, y)
#         self.lives = 3

Bricks = [brick_reg(25, 25, 1), brick_reg(27, 25, 1), brick_reg(29, 25, 1), 
           brick_reg(31, 25, 1), brick_reg(33, 25, 1), brick_reg(35, 25, 1),
           brick_reg(37, 25, 2), brick_reg(39, 25, 2), brick_reg(41, 25, 2), 
           brick_reg(43, 25, 2), brick_reg(45, 25, 2), brick_reg(49, 25, 2)
           ]

# bricks.append(brick2(2,3))
# bricks.append(brick3(2,4))

# for ob in bricks:
    # print(ob.indest)