import output as op
import observations as ob
from metrics import *

if __name__ == '__main__':

    #generate time series
    ts_ret = ob.ts_return(RP4) 
    ts_cum_ret = ob.ts_cum_return(RP4)
    ts_mean_abs_w = ob.ts_mean_abs_weight(W4, fill_fn= FILL4)
    ts_port_dir = ob.ts_portfolio_dir(W4, fill_fn= FILL4)
    
    #generate deliverable results
    op.print_deliverables(ts_ret, ts_cum_ret, AvrROC)

    #plot data
    op.plot_portfolio_dynamics(2, rd.T, ts_ret, ts_cum_ret, ts_mean_abs_w, ts_port_dir)

    #generate data_matrix for output
    data_matrix = op.generate_data_matrix(rd.T, rd.N, rd.stock_dict, \
                rd.date_dict, ts_ret, ts_cum_ret, ts_mean_abs_w, ts_port_dir, W4)
        
    #output data to CSV
    op.generate_csv_data('data_part4.team_B.csv', data_matrix)