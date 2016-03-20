import csv
import os
import deliverable_results as dr
import matplotlib.pyplot as plt

def print_deliverables(ts_ret, ts_cum_ret, avg_fn):
    print('Average Daily Log Returns: ' + str(dr.avg_daily_log_ret(ts_ret)))
    print('Std Dev of Daily Log Returns: ' + str(dr.std_daily_log_ret(ts_ret)))
    print('Annualized Sharpe Ratio: ' + str(dr.annualized_sr(ts_ret)))
    print('Skewness: ' + str(dr.skewness(ts_ret)))
    print('Excess Kurtosis: ' + str(dr.excess_kurtosis(ts_ret)))
    print('Max Drawdown Duration: ' + str(dr.max_drawdown(ts_cum_ret)[0]))
    print('Max Drawdown Loss: ' + str(dr.max_drawdown(ts_cum_ret)[1]))
    print('Equal Weight Correlation: ' + str(dr.equal_weight_corr(ts_ret, avg_fn)))    

def plot_portfolio_dynamics(r_low, r_high, ts_ret, ts_cum_ret, ts_mean_abs_w, ts_port_dir):
    f, axarr = plt.subplots(4, sharex=True)
    axarr[0].plot(range(r_low, r_high), ts_ret[r_low:])
    axarr[0].set_title('Long-short return')
    axarr[1].plot(range(r_low, r_high), ts_cum_ret[r_low:])
    axarr[1].set_title('Cumulative long-short return')
    axarr[2].plot(range(r_low, r_high), ts_mean_abs_w[r_low:])
    axarr[2].set_title('Mean absolute weight')
    axarr[3].plot(range(r_low, r_high), ts_port_dir[r_low:])
    axarr[3].set_title('Portfolio direction')
    plt.show()    

def generate_data_matrix(T, N, stock_dict, date_dict, ts_ret, ts_cum_ret, ts_mean_abs_w, ts_port_dir, W_fn):
    data_matrix = []
    for t in range(0, T):
        row = []
        row.append(date_dict[t])
        row.append(ts_ret[t])
        row.append(ts_cum_ret[t])
        row.append(ts_mean_abs_w[t])
        row.append(ts_port_dir[t])
        if t >= 2:
            row += [W_fn(t, 's' + str(i)) for i in range(0, N)]
        else:
            row += [99 for j in stock_dict]
        map(str, row)
        data_matrix.append(row)
    return data_matrix
    
def generate_csv_data(filename, data_matrix):
    with open(os.path.join('deliverables', filename), 'wb+') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        header = ['yyyymmdd', 'return', 'cumulative_return', 'mean_abs_weight', 'portfolio_direction']
        stocks = ['Stock_' + str(i) for i in range(0, 100)]
        writer.writerow(header + stocks)
        writer.writerows(data_matrix)
        