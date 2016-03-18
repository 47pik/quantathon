import csv
import os
import numpy as np

N = 100
T = 1003

#access attribute i of stock s at column s * 6 + i
#Attributes:
#1: SO
#2: SH
#3: SL
#4: SC
#5: TVL
#6: IND



def get_data():
    '''Return data as numpy array and dictionary of numpy arrays.
    
    dat is numpy array with 602 columns and 1003 rows. Each row is a day of data.
    Column 0 is the date e.g. 20010601, column 601 is a number representing the date
    e.g. Jan 1, 2000 is 0, Dec 31 2003 is 1002.
    Other 600 columns are divided as follows:
    Columns 1-6 are relevant to stock 0, 7-12 are relevant to stock 1 ... 
    595-600 are relevant to stock 99. These numbers are, in this order:
    SO (opening price), intraday high (SH), intraday low (SL), 
    closing price (SC), trading volume (TVL), trade direction indicator (IND).
    
    stock_dict is a dictionary where the values are these 6 column tables
    described above. The keys are 's0', 's1'...'s99'. The final column is the
    date in int format (0,1,2, ... 1002).'''
    #os.chdir('C:\Users\47pik\Documents\GitHub\quantathon\')
    rdr = csv.reader(open(os.path.join('data', 'in_sample_data.csv'), 'r'))
    x=list(rdr)
    dat=np.array(x).astype('float')
    nums = np.zeros((T, 1))
    for i in range(T):
        nums[i,0] = i
    dat = np.append(dat, nums, axis=1)
    
    stock_dict = {}
    for i in range(N):
        stock_name = 's' + str(i)
        stock_table = dat[:,[-1] + range(i * 6 + 1, i * 6 + 6 + 1)].copy()
        stock_dict[stock_name] = stock_table
        
    return dat, stock_dict

