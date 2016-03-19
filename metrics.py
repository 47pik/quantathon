import numpy as np
import read_data as rd

#Caches
SOd = {}; SHd = {}; SLd = {}; SCd = {}; TVLd = {}; INDd = {}
W1d = {}; AvrRCCd = {}; RCCd = {}; RP1d = {}
W2d = {}; RCOd = {}; ROCd = {}; ROOd = {}; RVP = {}; RP2d = {}
W3d = {}; FILL3d = {};  RP3d = {}
W4d = {}; FILL4d = {}; RP4d = {}


#Part 1
def AvrRCC(t):
    '''Returns the equal­weighted average close­-to­-close return across all stocks 
    on day t­'''
    if t in AvrRCCd: return AvrRCCd[t]
    res = np.mean([RCC(t, j) for j in rd.stock_dict])
    AvrRCCd[t] = res
    return res

def RCC(t, j):
    '''Returns close-to-close return of stock j on day t'''
    if (t, j) in RCCd: return RCCd[(t,j)]
    res =(SC(t,j)/SC(t-1, j)) - 1
    RCCd[t] = res
    return res

def W1(t,j):
    '''Returns weights for stock j on day t for Part 1'''
    if (t, j) in W1d: return W1d[(t,j)]
    res = - (1.0 / rd.N) * (RCC(t - 1, j) - AvrRCC(t - 1))
    W1d[(t,j)] = res
    return res

def RP1(t):
    '''Returns close-to-close portfolio for day t'''
    if t in RP1d: return RP1d[t]
    res = sum([W1(t, j) * RCC(t, j) for j in rd.stock_dict]) / \
        sum([abs(W1(t, j)) for j in rd.stock_dict])
    RP1d[t] = res
    return res


#Part 2
def RCO(t, j):
    '''Return close-to-open return of stock j on day t'''
    if (t, j) in RCOd: return RCOd[(t, j)]
    res = (SO(t, j) / float(SC(t, j))) - 1
    RCOd[(t, j)] = res
    return res

def ROC(t, j):
    '''Return open-to-close return of stock j on day t'''
    if (t, j) in ROCd: return ROCd[(t, j)]
    res = (SC(t, j) / float(SO(t, j))) - 1
    ROCd[(t, j)] = res
    return res

def ROO(t, j):
    '''Return open-to-open return of stock j on day t'''
    if (t, j) in ROOd: return ROOd[(t, j)]
    res = (SO(t, j) / float(SO(t, j))) - 1
    ROOd[(t, j)] = res
    return res

def RVP(t, j):
    '''Return range based proxy for variance of stock j on day t'''
    if (t, j) in RVPd: return RVPd[(t, j)]
    res (1/(float(4*np.log(2))))*((np.log(SH(t, j)) - np.log(SL(t, j)))**2)
    RVPd[(t, j)] = res
    return res

def W2(t, j):
    '''Returns weights for stock j on day t for Part 2'''
    pass

def RP2(t):
    '''Returns open-to-close portfolio for day t'''
    pass


#Part 3
def W3(t, j):
    '''Returns weights for stock j on day t for Part 3'''
    pass

def FILL3(t, j):
    '''Returns 1 if stock j on day t is able to be filled on according to W3, 0 otherwise'''
    pass

def RP3(t):
    '''Returns open-to-close portfolio for day t taking fill conditions into account'''
    pass


#Part 4
def W4(t, j):
    '''Returns weights for stock j on day t for Part 4'''
    pass
    
def FILL4(t, j):
    '''Returns 1 if stock j on day t is able to be filled on according to W4, 0 otherwise'''
    pass

def RP4(t, j):
    '''Returns open-to-close portfolio for day t taking fill conditions into account'''
    pass

    
#Utility
def SO(t, j):
    '''Returns opening price of stock j on day t'''
    if (t, j) in SOd: return SOd[(t, j)]
    stock_data = rd.stock_dict[j]
    opening = stock_data[t][1]
    SOd[(t, j)] = opening
    return opening

def SH(t, j):
    '''Returns intraday high of stock j on day t'''
    if (t, j) in SHd: return SHd[(t, j)]
    stock_data = rd.stock_dict[j]
    high = stock_data[t][2]
    SHd[(t, j)] = high
    return high

def SL(t, j):
    '''Returns intraday low of stock j on day t'''
    if (t, j) in SLd: return SLd[(t, j)]
    stock_data = rd.stock_dict[j]
    low = stock_data[t][3]
    SLd[(t, j)] = low
    return low

def SC(t, j):
    '''Returns closing price of stock j on day t'''
    if (t, j) in SCd: return SCd[(t, j)]
    stock_data = rd.stock_dict[j]
    closing = stock_data[t][4]
    SCd[(t, j)] = closing
    return closing

def TVL(t, j):
    '''Returns trading volume of stock j on day t'''
    if (t, j) in TVLd: return TVLd[(t, j)]
    stock_data = rd.stock_dict[j]
    volume = stock_data[t][5]
    TVLd[(t, j)] = volume
    return volume

def IND(t, j):
    '''Returns trade direction indicator of stock j on day t'''
    if (t, j) in INDd: return INDd[(t, j)]
    stock_data = rd.stock_dict[j]
    indicator = stock_data[t][6]
    INDd[(t, j)] = indicator
    return indicator