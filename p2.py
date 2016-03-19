import numpy as np
from metrics import *
import random
import scipy.optimize

if __name__ == '__main__':
    f = sharpe
    r = scipy.optimize.minimize(f, np.array([0.1, 0.05, -0.1]),\
                                options={'maxiter':100, 'disp':True})
    
    