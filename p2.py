import numpy as np
import read_data

dat, stock_dict = read_data.get_data()


def RCO(t, j):
    '''Return close-to-open return of stock j on day t'''
    return (SO(t, j) / float(SC(t, j))) - 1

def ROC(t, j):
    '''Return open-to-close return of stock j on day t'''
    return (SC(t, j) / float(SO(t, j))) - 1

def ROO(t, j):
    '''Return open-to-open return of stock j on day t'''
    return (SO(t, j) / float(SO(t, j))) - 1

def SO(t, j):
    '''Returns opening price of stock j on day t'''
    stock_data = stock_dict[j]
    opening_price = stock_data[t][1]
    print stock_data[t]
    
    return opening_price
    
def SC(t, j):
    '''Returns closing price of stock j on day t'''
    stock_data = stock_dict[j]
    opening_price = stock_data[t][4]
    print stock_data[t]
    
    return opening_price


    