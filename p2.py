import numpy as np
from metrics import *
import random
import scipy.optimize

if __name__ == '__main__':
    f = sharpe
    r = scipy.optimize.minimize(f, np.array([0,-5,22,0,-5,0,-10,-5,0.03,-10,-50,-100]),\
                                options={'maxiter':100, 'disp':True})
    
    