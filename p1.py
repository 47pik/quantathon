import numpy as np
from metrics import *
import time
import sys
#import matplotlib.pyplot as plt


if __name__ == '__main__':
    ret_pf = [0, 0]
    st = time.time()
    for t in range(2, rd.T):
        rp = RP1(t)
        ret_pf.append(rp)
    
    #plt.plot(ret_pf)
    #plt.show()
    
    cumR = []
    rp2 = [x + 1 for x in ret_pf]
    for t in range(2, rd.T):    
        cumR.append(np.log(np.prod(rp2[2: t + 1])))
    
    eqLO = []
    rccs = [np.mean([RCC(t, j) for j in rd.stock_dict]) + 1 for t in range(rd.T)]
    for t in range(rd.T):
        eqLO.append(np.log(np.prod(rccs[2: t + 1])))
        
    #write csv
    #w = csv.writer('p1.csv')
        
        

