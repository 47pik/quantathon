import numpy as np
import scipy as sp

def avg_daily_log_ret(ts_ret):
    '''Returns average daily log returns'''
    log_rets = []
    for ts in ts_ret[2:]:
        log_rets.append(np.log(1 + ts))
    return np.mean(log_rets)

def std_daily_log_ret(ts_ret):
    '''Returns std dev of daily log returns'''
    log_rets = []
    for ts in ts_ret[2:]:
        log_rets.append(np.log(1 + ts))
    return np.std(log_rets, ddof=1)

def annualized_sr(ts_ret):
    '''Returns annualized sharpe ratio'''
    mean = np.mean(ts_ret[2:])
    std = np.std(ts_ret[2:], ddof=1)
    return (float(mean) / std) * np.sqrt(252)

def skewness(ts_ret):
    '''Return the skewness of returns on the strategy'''
    return sp.stats.skew(ts_ret[2:])

def excess_kurtosis(ts_ret):
    '''Return the excess kurtosis of returns on the strategy'''
    return sp.stats.kurtosis(ts_ret[2:])

def max_drawdown(ts_cum_ret):
    '''Return the maximum drawdown'''
    curr_peak = ts_cum_ret[2] + 1
    curr_peak_i = 2
    curr_valley = ts_cum_ret[2] + 1
    curr_valley_i = 2
    mdd_peak = curr_peak
    mdd_peak_i = 2
    mdd_valley = curr_valley
    mdd_valley_i = 2
    mdd_mag = 0
    #mdd_percent = 0
    
    for i in range(2, len(ts_cum_ret)):
        curr = ts_cum_ret[i] + 1
        
        if curr < curr_valley:
            curr_valley = curr
            curr_valley_i = i
            
            if (curr_peak - curr_valley) > mdd_mag:
            #if (curr_peak - curr_valley) / curr_peak > mdd_percent:
                mdd_peak = curr_peak
                mdd_peak_i = curr_peak_i
                mdd_valley = curr_valley
                mdd_valley_i = curr_valley_i
                
                #mdd_percent = (mdd_peak - mdd_valley) / mdd_peak
                mdd_mag = mdd_peak - mdd_valley
                
        elif curr > curr_peak:
            curr_peak = curr
            curr_peak_i = i
            curr_valley = curr
            curr_valley_i = i
    
    duration = mdd_valley_i - mdd_peak_i
    #return (duration, -mdd_percent)
    return(duration, -mdd_mag)
    
def equal_weight_corr(ts_ret, avg_fn):
    '''Return correlation between strategy and equal weight long portfolio'''
    
    eq_weight_ret = [avg_fn(t) for t in range(2, len(ts_ret))]
    return np.correlate(ts_ret[2:], eq_weight_ret)[0]