import matplotlib.pyplot as plt
import output as op
import observations as ob
from metrics import *

if __name__ == '__main__':

    #generate time series
    ts_ret = ob.ts_return(RP1) 
    ts_cum_ret = ob.ts_cum_return(RP1)
    ts_mean_abs_w = ob.ts_mean_abs_weight(W1)
    ts_port_dir = ob.ts_portfolio_dir(W1)
    
    f, axarr = plt.subplots(4, sharex=True)
    axarr[0].plot(range(2, rd.T), ts_ret[2:])
    axarr[0].set_title('Long-short return')
    axarr[1].plot(range(2, rd.T), ts_cum_ret[2:])
    axarr[1].set_title('Cumulative long-short return')
    axarr[2].plot(range(2, rd.T), ts_mean_abs_w[2:])
    axarr[2].set_title('Mean absolute weight')
    axarr[3].plot(range(2, rd.T), ts_port_dir[2:])
    axarr[3].set_title('Portfolio direction')
    plt.show()

    #generate data_matrix for output
    data_matrix = []
    for t in range(0, rd.T):
        row = []
        row.append(rd.date_dict[t])
        row.append(ts_ret[t])
        row.append(ts_cum_ret[t])
        row.append(ts_mean_abs_w[t])
        row.append(ts_port_dir[t])
        if t >= 2:
            row += [W1(t, 's' + str(i)) for i in range(0, rd.N)]
        else:
            row += [99 for j in rd.stock_dict]
        map(str, row)
        data_matrix.append(row)

    op.generate_csv('data_part1.team_B.csv', data_matrix)

