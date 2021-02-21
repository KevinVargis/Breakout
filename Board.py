import numpy as np
class board:

    grid = np.zeros((52, 100), 'U1')
    # grid = [[' ']*10]*10
    # grid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
    #         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
    #         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
    #         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
    #         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
    #         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
    #         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
    #         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
    #         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
    #         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
    #         ]
    def __init__(self):
        for i in range(np.shape(self.grid)[0]):
            for j in range(np.shape(self.grid)[1]):
                if i == 0:
                    self.grid[i][j] = '-'
                elif i == np.shape(self.grid)[0]-1:
                    self.grid[i][j] = '_'
                elif i == np.shape(self.grid)[0]-3:
                    self.grid[i][j] = '-'
                elif j == 0:
                    self.grid[i][j] = '|'
                elif j == np.shape(self.grid)[1]-1:
                    self.grid[i][j] = '|'
                else:
                    self.grid[i][j] = ' '

Board = board()