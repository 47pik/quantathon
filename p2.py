import numpy as np
from metrics import *
import random
import scipy.optimize

if __name__ == '__main__':
    f = sharpe
    sh_dic = {}
    for pw in range(-5, 7):
        print(pw)
        #params = [random.uniform(-0.5, 0.5) for i in range(3)]
        a = -(2 ** pw)
        b = a * (-0.45/10)
        c = a * (-0.55/10)
        params = [a,a,a,a,b,b,b,b,c,c,c,c]
        r = scipy.optimize.minimize(f, np.array(params),
                                    options={'maxiter':100, 'disp':True})
        print(str(tuple(params)))
        print(r.x)
        print(r.fun)
        sh_dic[pw] = [tuple(params), r.x, r.fun]
    
    