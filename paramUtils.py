import numpy as np

def random2D(row = 1, col = 0, logical = True):
    """
    A simple generator for random 2d matrix 
    
    Attributes
    __________
    row :: int 
        number of rows, default = 1
    col :: int
        number of cols, default = 0
    Logical :: bool
        type of the output matrix, if True a binary matrix, default = True
        
    Values
    ______
    A row*col matrix
    Default output, single rv between (0,1)
    
    """
    if row == 0 or col == 0:
        dim = max(row,col)
        result = np.random.random(dim)
    else:
        result = np.random.random((row,col))
    if logical == True:
        result[result>0.5] = 1
        result[result<=0.5] = 0
        
    return(result)