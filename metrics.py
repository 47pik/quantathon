import numpy as np
import read_data as rd

#Part 2
def RCO(t, j):
    '''Return close-to-open return of stock j on day t'''
    return (SO(t, j) / float(SC(t, j))) - 1

def ROC(t, j):
    '''Return open-to-close return of stock j on day t'''
    return (SC(t, j) / float(SO(t, j))) - 1

def ROO(t, j):
    '''Return open-to-open return of stock j on day t'''
    return (SO(t, j) / float(SO(t, j))) - 1

def RVP(t, j):
    '''Return range based proxy for variance of stock j on day t'''
    return (1/(float(4*np.log(2))))*((np.log(SH(t, j)) - np.log(SL(t, j)))**2)
    

def SO(t, j):
    '''Returns opening price of stock j on day t'''
    stock_data = rd.stock_dict[j]
    opening = stock_data[t][1]
    return opening

def SH(t, j):
    '''Returns intraday high of stock j on day t'''
    stock_data = rd.stock_dict[j]
    high = stock_data[t][2]
    return high

def SL(t, j):
    '''Returns intraday low of stock j on day t'''
    stock_data = rd.stock_dict[j]
    low = stock_data[t][3]
    return low

def SC(t, j):
    '''Returns closing price of stock j on day t'''
    stock_data = rd.stock_dict[j]
    closing = stock_data[t][4]
    return closing

def TVL(t, j):
    '''Returns trading volume of stock j on day t'''
    stock_data = rd.stock_dict[j]
    volume = stock_data[t][5]
    return volume

def IND(t, j):
    '''Returns trade direction indicator of stock j on day t'''
    stock_data = rd.stock_dict[j]
    indicator = stock_data[t][6]
    return indicator