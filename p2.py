import numpy as np
from metrics import *
import random
import scipy.optimize

if __name__ == '__main__':
    f = sharpe2
    sh_dic = {}
    #for pw in range(-5, 7):
        #print(pw)
        ##params = [random.uniform(-0.5, 0.5) for i in range(3)]
        #a = -(2 ** pw)
        #b = a * (-0.45/10)
        #c = a * (-0.55/10)
        #params = [a,a,a,a,b,b,b,b,c,c,c,c]
        #r = scipy.optimize.minimize(f, np.array(params),
                                    #options={'maxiter':100, 'disp':True})
        #print(str(tuple(params)))
        #print(r.x)
        #print(r.fun)
        #sh_dic[pw] = [tuple(params), r.x, r.fun]
        #with starting -0.125
    params = [-0.11812008, -3.05744312,  3.798748,   -2.05990281,  0.39163579,  3.8577401,\
              -4.32966829, -3.93373867, -0.46817134, -2.17563513,  2.48775916,  2.48504554]
    r = scipy.optimize.minimize(f, np.array(params),\
                                            options={'maxiter':1000, 'disp':True})    
    print(r.x)
    print(r.fun)
    print(str(tuple(params)))
    