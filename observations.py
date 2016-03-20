import numpy as np
from metrics import *

def ts_return(r_fn, coeffs=None):
    '''Return list representing the time-series of the long-short return'''
    ret_pf = [99, 99]
    for t in range(2, rd.T):
        if coeffs:
            rp = r_fn(t, coeffs)
        else:
            rp = r_fn(t)
        ret_pf.append(rp)
    return ret_pf

#check indicies
def ts_cum_return(r_fn, coeffs=None):
    '''Return list representing the time-series of cumulative long-short return'''
    cumR = [99, 99]
    ret_pf = ts_return(r_fn, coeffs)
    rp2 = [x + 1 for x in ret_pf]
    for t in range(2, rd.T):    
        cumR.append(np.log(np.prod(rp2[2: t + 1])))
    return cumR

def ts_mean_abs_weight(w_fn, coeffs=None, fill_fn=None):
    '''Return list representing the time series of mean absolute weight'''
    mean_abs_weight = [99, 99]
    if coeffs:
        extra_arg = [coeffs]
    else:
        extra_arg = []
    for t in range(2, rd.T):

        weights = np.array([w_fn(*([t, j] + extra_arg)) for j in rd.stock_dict])
        #apply fill fn if given
        if fill_fn:
            fills = np.array([fill_fn(*[t, j] + extra_arg) for j in rd.stock_dict])
            weights = weights * fills
        abs_weights = map(abs, weights)
        
        mean_abs_weight.append(sum(abs_weights) / float(rd.N))
    return mean_abs_weight
        
def ts_portfolio_dir(w_fn, coeffs=None, fill_fn=None):
    '''Return list representing the time series of portfolio direction'''
    port_dir = [99, 99]
    if coeffs:
        extra_arg = [coeffs]
    else:
        extra_arg = []    
    for t in range(2, rd.T):
        
        weights = np.array([w_fn(*([t, j] + extra_arg)) for j in rd.stock_dict])
        #apply fill fn if given
        if fill_fn:
            fills = np.array([fill_fn(*([t, j] + extra_arg)) for j in rd.stock_dict])
            weights = weights * fills
    
        abs_weights = map(abs, weights)
        denom = sum(abs_weights)
        if denom == 0:
            res = 0
        else:
            res = round(sum(weights), 15) / sum(abs_weights)
        port_dir.append(res)
        
    return port_dir
        
    ##???
    #eqLO = []
    #rccs = [np.mean([RCC(t, j) for j in rd.stock_dict]) + 1 for t in range(rd.T)]
    #for t in range(rd.T):
        #eqLO.append(np.log(np.prod(rccs[2: t + 1])))