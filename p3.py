import output as op
import observations as ob
from metrics import *

if __name__ == '__main__':

    #define params
    param_names = ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'b10', 'b11', 'b12']
    param_vals = [-1.25,-1.25,-1.25,-1.25,1.85,1.85,1.85,1.85,-0.11,-0.11,-0.11,-0.11]

    #generate time series      
    ts_ret = ob.ts_return(RP3, coeffs=param_vals) 
    ts_cum_ret = ob.ts_cum_return(RP3, coeffs=param_vals)
    ts_mean_abs_w = ob.ts_mean_abs_weight(W3_wrapper, coeffs=param_vals, fill_fn = FILL3)
    ts_port_dir = ob.ts_portfolio_dir(W3_wrapper, coeffs=param_vals, fill_fn= FILL3)
    
    #generate deliverable results
    op.print_deliverables(ts_ret, ts_cum_ret, AvrROC)

    #plot data
    op.plot_portfolio_dynamics(2, rd.T, ts_ret, ts_cum_ret, ts_mean_abs_w, ts_port_dir)

    #generate data_matrix for output
    data_matrix = op.generate_data_matrix(rd.T, rd.N, rd.stock_dict, \
                rd.date_dict, ts_ret, ts_cum_ret, ts_mean_abs_w, ts_port_dir, W3_wrapper, coeffs=param_vals)
        
    #output data to CSV
    op.generate_csv_data('data_part3.team_B.csv', data_matrix)

    #output coefficients to CSV
    op.generate_csv_coeff('coeff_part3.team_B.csv', param_names, param_vals)