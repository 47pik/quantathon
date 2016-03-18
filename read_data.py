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
    #os.chdir('C:\Users\47pik\Documents\GitHub\quantathon\data')
    rdr = csv.reader(open('data\in_sample_data.csv', 'r'))
    x=list(rdr)
    dat=np.array(x).astype('float')
    nums = np.zeros((1003, 1))
    for i in range(1003):
        nums[i,0] = i
    dat = np.append(dat, nums, axis=1)
    
    stock_dict = {}
    for i in range(N):
        stock_name = 's' + str(i)
        stock_table = dat[:,i * 6 + 1: i * 6 + 6 + 1].copy()
        stock_dict[stock_name] = stock_table
        
    return dat, stock_dict

