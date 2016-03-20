import numpy as np
import read_data as rd
import time
from collections import Counter
#from sklearn import linear_model as lm
import scipy.stats as ss
import sys

#Caches
SOd = {}; SHd = {}; SLd = {}; SCd = {}; TVLd = {}; AvrTVLd = {}; INDd = {}
W1d = {}; AvrRCCd = {}; RCCd = {}; RP1d = {};
W2d = {}; RCOd = {}; ROCd = {}; ROOd = {}; RVPd = {}; RP2d = {}
AvrRCOd = {}; AvrROCd= {}; AvrROOd = {}; AvrRVPd = {}
W3d = {}; FILL3d = {};  RP3d = {}
W4d = {}; FILL4d = {}; RP4d = {}
ret10d = {}; lowd = {}; highd = {}; ressupd = {}; movavgd = {}


#Part 1
def AvrRCC(t):
    '''Returns the equalweighted average close-to-close return across all stocks 
    on day t'''
    if t in AvrRCCd: return AvrRCCd[t]
    res = np.mean([RCC(t, j) for j in rd.stock_dict])
    AvrRCCd[t] = res
    return res

def RCC(t, j):
    '''Returns close-to-close return of stock j on day t'''
    if (t, j) in RCCd: return RCCd[(t,j)]
    res =(SC(t,j)/SC(t-1, j)) - 1
    RCCd[(t, j)] = res
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
    res = (SO(t, j) / SC(t - 1, j)) - 1
    RCOd[(t, j)] = res
    return res

def AvrRCO(t):
    '''Return average close-to-open return of all stocks on day t'''
    if t in AvrRCOd: return AvrRCOd[t]
    res = np.mean([RCO(t, j) for j in rd.stock_dict])
    AvrRCOd[t] = res
    return res    

def ROC(t, j):
    '''Return open-to-close return of stock j on day t'''
    if (t, j) in ROCd: return ROCd[(t, j)]
    res = (SC(t, j) / float(SO(t, j))) - 1
    ROCd[(t, j)] = res
    return res

def AvrROC(t):
    '''Return average open-to-close return of all stocks on day t'''
    if t in AvrROCd: return AvrROCd[t]
    res = np.mean([ROC(t, j) for j in rd.stock_dict])
    AvrROCd[t] = res
    return res  

def ROO(t, j):
    '''Return open-to-open return of stock j on day t'''
    if (t, j) in ROOd: return ROOd[(t, j)]
    res = (SO(t, j) / float(SO(t-1, j))) - 1
    ROOd[(t, j)] = res
    return res

def AvrROO(t):
    '''Return average open-to-open return of all stocks on day t'''
    if t in AvrROOd: return AvrROOd[t]
    res = np.mean([ROO(t, j) for j in rd.stock_dict])
    AvrROOd[t] = res
    return res

def RVP(t, j):
    '''Return range based proxy for variance of stock j on day t'''
    if (t, j) in RVPd: return RVPd[(t, j)]
    res = (1/(float(4*np.log(2))))*((np.log(SH(t, j)) - np.log(SL(t, j)))**2)
    RVPd[(t, j)] = res
    return res

def AvrRVP(t, j):
    '''Return average RVP for stock j for 200 days prior to day t'''
    if (t, j) in AvrRVPd: return AvrRVPd[(t, j)]
    res = np.mean([RVP(t, j) for t in range(max(1, t-200), t+1)])
    AvrRVPd[(t, j)] = res
    return res    

def W2(t, j):
    '''Returns weights for stock j on day t for Part 2'''
    if (t, j) in W2d: return W2d[(t, j)]

    n = float(rd.N)
    relative_tvl = TVL(t-1,j) / float(AvrTVL(t-1,j))
    relative_rvp = RVP(t-1,j) / float(AvrRVP(t-1,j))
    
    terms = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    terms[0] = (RCC(t-1,j) - AvrRCC(t-1))
    terms[1] = (ROO(t,j) - AvrROO(t))
    terms[2] = (ROC(t-1,j) - AvrROC(t-1))
    terms[3] = (RCO(t,j) - AvrRCO(t))
    terms[4] = relative_tvl * terms[0]
    terms[5] = relative_tvl * terms[1]
    terms[6] = relative_tvl * terms[2]
    terms[7] = relative_tvl * terms[3]
    terms[8] = relative_rvp * terms[0]
    terms[9] = relative_rvp * terms[1]
    terms[10] = relative_rvp * terms[2]
    terms[11] = relative_rvp * terms[3] 
    terms = np.array([x / n for x in terms])
    
    W2d[(t, j)] = terms
    return terms

def W2p(t, j):
    '''Returns weights for stock j on day t for Part 2'''
    if (t, j) in W2d: return W2d[(t, j)]

    n = float(rd.N)
    relative_tvl = TVL(t-1,j) / float(AvrTVL(t-1,j))
    relative_rvp = RVP(t-1,j) / float(AvrRVP(t-1,j))
    
    terms = [0, 0, 0]
    rcc = (RCC(t-1,j) - AvrRCC(t-1))
    roo = (ROO(t,j) - AvrROO(t))
    roc = (ROC(t-1,j) - AvrROC(t-1))
    #rco = (RCO(t,j) - AvrRCO(t))
    r_avg = (rcc + roo + roc) / 3
    terms[0] = r_avg
    terms[1] = relative_tvl * r_avg
    terms[2] = relative_rvp * r_avg
    terms = np.array([x / n for x in terms])
    
    W2d[(t, j)] = terms
    return terms

def W2_wrapper(t,j, parameters):
    terms = W2(t, j)
    product = parameters * terms
    return np.sum(product)    

def W2p_wrapper(t,j, parameters):
    terms = W2p(t, j)
    product = parameters * terms
    return np.sum(product)  

def RP2(t, parameters):
    '''Returns open-to-close portfolio for day t'''
    if len(parameters) == 12:
        w = [W2_wrapper(t, j, parameters)  for j in rd.stock_dict]
    else:
        w = [W2p_wrapper(t, j, parameters)  for j in rd.stock_dict]
    rocs = [ROC(t, j) for j in rd.stock_dict]
    res = np.dot(w, rocs) / sum(map(abs, w))
    return res

def sharpe2(parameters):
    rfn = RP2
    rps = [rfn(t, parameters) for t in range(2, rd.T)]
    return -np.mean(rps) / np.std(rps)
    

#Part 3

def W3(t, j):
    '''Returns weights for stock j on day t for Part 3'''
    if (t, j) in W3d: return W3d[(t, j)]

    n = float(rd.N)
    relative_tvl = TVL(t-1,j) / float(AvrTVL(t-1,j))
    relative_rvp = RVP(t-1,j) / float(AvrRVP(t-1,j))
    
    terms = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    terms[0] = (RCC(t-1,j) - AvrRCC(t-1))
    terms[1] = (ROO(t,j) - AvrROO(t))
    terms[2] = (ROC(t-1,j) - AvrROC(t-1))
    terms[3] = (RCO(t,j) - AvrRCO(t))
    terms[4] = relative_tvl * terms[0]
    terms[5] = relative_tvl * terms[1]
    terms[6] = relative_tvl * terms[2]
    terms[7] = relative_tvl * terms[3]
    terms[8] = relative_rvp * terms[0]
    terms[9] = relative_rvp * terms[1]
    terms[10] = relative_rvp * terms[2]
    terms[11] = relative_rvp * terms[3] 
    terms = np.array([x / n for x in terms])
    
    W3d[(t, j)] = terms
    return terms

def W3p(t, j):
    '''Returns weights for stock j on day t for Part 3'''
    if (t, j) in W3d: return W3d[(t, j)]

    n = float(rd.N)
    relative_tvl = TVL(t-1,j) / float(AvrTVL(t-1,j))
    relative_rvp = RVP(t-1,j) / float(AvrRVP(t-1,j))
    
    terms = [0, 0, 0]
    rcc = (RCC(t-1,j) - AvrRCC(t-1))
    roo = (ROO(t,j) - AvrROO(t))
    roc = (ROC(t-1,j) - AvrROC(t-1))
    #rco = (RCO(t,j) - AvrRCO(t))
    r_avg = (rcc + roo + roc) / 3
    terms[0] = r_avg
    terms[1] = relative_tvl * r_avg
    terms[2] = relative_rvp * r_avg
    terms = np.array([x / n for x in terms])
    
    W3d[(t, j)] = terms
    return terms

def W3p_wrapper(t,j, parameters):
    terms = W3p(t, j)
    product = parameters * terms
    return np.sum(product)

def FILL3(t, j, w):
    '''Returns 1 if stock j on day t is able to be filled on according to W3, 0 otherwise'''
    sgn = np.sign(w)
    if (t, j, sgn) in FILL3d: return FILL3d[(t, j, sgn)]
    if (sgn * IND(t, j)) >= 0:
        res = 1
    else:
        res = 0
    FILL3d[(t, j, sgn)] = res
    return res

def W3_wrapper(t,j, parameters):
    terms = W3(t, j)
    product = parameters * terms
    return np.sum(product)  

def RP3(t, parameters):
    '''Returns open-to-close portfolio for day t taking fill conditions into account'''
    if len(parameters) == 12:
        w = [W3_wrapper(t, j, parameters) for j in rd.stock_dict]
    else:
        w = [W3p_wrapper(t, j, parameters) for j in rd.stock_dict]
        
    fills = []
    i = 0
    for j in rd.stock_dict:
        fills.append(FILL3(t, j, w[i]))
        i+= 1
    #fills = [FILL3(t, j, w) for j in rd.stock_dict]
    rocs = [ROC(t, j) for j in rd.stock_dict]
    
    term = np.array(w) * np.array(fills)
    denom = sum(map(abs, term))
    if denom == 0:
        res = 0
    else:
        res = sum(term * rocs) / sum(map(abs, term))
    return res

def sharpe3(parameters):
    rfn = RP3
    rps = [rfn(t, parameters) for t in range(2, rd.T)]
    return -np.mean(rps) / np.std(rps)
    
    
#Part 4
def W4(t, j):
    '''Returns weights for stock j on day t for Part 4'''
    if (t, j) in W4d: return W4d[(t,j)]
    #res =  ret10(t, j)
    #if TVL(t - 1, j) > AvrTVL(t - 1, j) * 1.5:
        #res = -ret10(t - 1, j)
    #else:
        #res = 0
    res = ressup(t, j)
    W4d[(t,j)] = res
    return res
    

def ret10(t, j):
    if (t, j) in ret10d: return ret10d[(t,j)]
    res = np.prod([1 + RCC(i, j) for i in range(t-1)])/ \
        np.prod([1 + AvrRCC(i) for i in range(t-1)])- 1
    ret10d[(t,j)] = res
    return res

def ressup(t, j):
    alpha_high = 0.01 #selling
    alpha_low = 0.0615 #buying
    beta = 1
    if (t, j) in ressupd: return ressupd[(t, j)]
    L = low(t, j); H = high(t, j)
    pr = SO(t, j)
    if pr < ((1 + alpha_low) * L):
        res = beta
    elif pr > ((1 - alpha_high) * H):
        res = -beta
    else:
        res = 0
    ressupd[(t, j)] = res
    return res
    
def low(t, j):
    if (t, j) in lowd: return lowd[(t, j)]
    L = min([SL(i, j) for i in range(max(1, t-20), t+1)]) #orig said t-200
    lowd[(t, j)] = L
    return L
    
def high(t, j):
    if (t, j) in highd: return highd[(t, j)]
    H = max([SH(i, j) for i in range(max(1, t-20), t+1)])
    highd[(t, j)] = H
    return H    

def movavg(t, j):
    '''Returns moving average for stock j for 200 days prior to day t'''
    if (t, j) in movavgd: return movavgd[(t, j)]
    longavg = np.mean([SC(i, j) for i in range(max(1, t-200), t+1)])
    if SC(t - 1, j) > longavg:
        res = SC(t - 1, j)
    else:
        res = -SC(t - 1, j)
    movavgd[(t, j)] = res
    return res    

def FILL4(t, j, weights=None):
    '''Returns 1 if stock j on day t is able to be filled on according to W4, 0 otherwise'''
    if (t, j) in FILL4d: return FILL4d[(t, j)]
    if (W4(t, j) * IND(t, j)) >= 0:
        res = 1
    else:
        res = 0
    FILL4d[(t,j)] = res
    return res

def RP4(t):
    '''Returns open-to-close portfolio for day t taking fill conditions into account'''
    w = [W4(t, j) for j in rd.stock_dict]
    fills = [FILL4(t, j) for j in rd.stock_dict]
    rocs = [ROC(t, j) for j in rd.stock_dict]
    
    term = np.array(w) * np.array(fills)
    denom = sum(map(abs, term))
    if denom == 0:
        res = 0
    else:
        res = sum(term * rocs) / sum(map(abs, term))
    return res
    
def sharpe_fast(rps):
    return -np.mean(rps) / np.std(rps)
    
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

def AvrTVL(t, j):
    '''Returns average trading volume for stock j for 200 days prior to day t'''
    if (t, j) in AvrTVLd: return AvrTVLd[(t, j)]
    res = np.mean([TVL(t, j) for t in range(max(1, t-200), t+1)])
    AvrTVLd[(t, j)] = res
    return res

def IND(t, j):
    '''Returns trade direction indicator of stock j on day t'''
    if (t, j) in INDd: return INDd[(t, j)]
    stock_data = rd.stock_dict[j]
    indicator = stock_data[t][6]
    INDd[(t, j)] = indicator
    return indicator

if __name__ == '__main__':
    pass
    ##parameters = [10,2,3,4,5,6,7,8,1,2,3,4]
    #params = [-0.11812008, -3.05744312,  3.798748,   -2.05990281,  0.39163579,  3.8577401,\
              #-4.32966829, -3.93373867, -0.46817134, -2.17563513,  2.48775916,  2.48504554]   

    #st = time.time(); s = sharpe3(params); end = time.time(); print(end - st)
    ##mnROO = [np.mean([ROO(t,j) for j in rd.stock_dict]) for t in range(rd.T)]
    ##mnRCC = [np.mean([RCC(t,j) for j in rd.stock_dict]) for t in range(rd.T)]
    ##mnROC = [np.mean([ROC(t,j) for j in rd.stock_dict]) for t in range(rd.T)]
    ##mnRCO = [np.mean([RCO(t,j) for j in rd.stock_dict]) for t in range(rd.T)]
    #sys.exit()
    #rp4s = [RP4(t) for t in range(11, rd.T)]
    
    #i10 = {}
    #cd = {}
    #j = 's6'
    #for j in rd.stock_dict:
        ##r10 = [ret10(t, j) for t in range(11, rd.T)]
        #ind = np.reshape(rd.stock_dict[j][:,6], (1003, 1))
        ##ind10 = ind[11:,:]
        ##pos10i = filter(lambda i: r10[i] > 0, range(rd.T - 11))
        ##pos10 = [int(ind10[i]) for i in pos10i]
        ###print(Counter(pos10))
        ##neg10i = filter(lambda i: r10[i] < 0, range(rd.T - 11))
        ##neg10 = [int(ind10[i]) for i in neg10i]
        ###print(Counter(neg10))  
        ##i10[j] = (Counter(pos10), Counter(neg10))
        #roc = np.reshape(np.array([ROC(t, j) for t in range(rd.T)]), (1003, 1))
        ##l = lm.LinearRegression()
        ##l.fit(roc, ind)
        #x = ss.linregress(np.transpose(roc)[0], np.transpose(ind)[0])
              
        #cd[j] = x
        
        #coefs = [cd[j].slope for j in cd]
        #errs = [cd[j].stderr for j in cd]
        #np.median(coefs)
        #np.median(errs)
        #pv = [cd[j].pvalue for j in cd]
        #np.median(pv)        
        #pvi = [(i, pv[i]) for i in range(100)]
        #spvi = sorted(pvi, key=lambda x:x[1]) 
        #sigcoefs = [[x[0], x[1], coefs[x[0]]] for x in spvi[:23]]
