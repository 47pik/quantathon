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
    
    #performs at -0.064784872847161015 with IND
    #three param version performs at -0.033414734359919554 with IND
    r = scipy.optimize.minimize(f, np.array(params),\
                                            options={'maxiter':1000, 'disp':True})    
    print(r.x)
    print(r.fun)
    print(str(tuple(params)))
    
    #results:
    #Warning: Desired error not necessarily achieved due to precision loss.
             #Current function value: -0.442797
             #Iterations: 106
             #Function evaluations: 1719
             #Gradient evaluations: 122
    #[ -0.14017089 -10.7714376   11.30675988   7.50040931   0.25822643
       #2.58069292  -2.88504362  -2.57650906  -0.30956843  -0.06588881
       #0.26922478   0.20417341]
    #-0.44279693753
    #(-0.11812008, -3.05744312, 3.798748, -2.05990281, 0.39163579, 3.8577401, -4.32966829, -3.93373867, -0.46817134, -2.17563513, 2.48775916, 2.48504554)    
    