import output as op
import observations as ob
from metrics import *

if __name__ == '__main__':

    #define params
    param_names = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12']
    param_vals = [-0.11812008, -3.05744312,  3.798748,   -2.05990281,  0.39163579,  3.8577401,\
              -4.32966829, -3.93373867, -0.46817134, -2.17563513,  2.48775916,  2.48504554]
    
    #generate time series
    ts_ret = ob.ts_return(RP2, coeffs=param_vals) 
    ts_cum_ret = ob.ts_cum_return(RP2, coeffs=param_vals)
    ts_mean_abs_w = ob.ts_mean_abs_weight(W2_wrapper, coeffs=param_vals)
    ts_port_dir = ob.ts_portfolio_dir(W2_wrapper, coeffs=param_vals)
    
    #generate deliverable results
    op.print_deliverables(ts_ret, ts_cum_ret, AvrROC)

    #plot data
    op.plot_portfolio_dynamics(2, rd.T, ts_ret, ts_cum_ret, ts_mean_abs_w, ts_port_dir)

    #generate data_matrix for output
    data_matrix = op.generate_data_matrix(rd.T, rd.N, rd.stock_dict, \
                rd.date_dict, ts_ret, ts_cum_ret, ts_mean_abs_w, ts_port_dir, W2_wrapper, coeffs=param_vals)
        
    #output data to CSV
    op.generate_csv_data('data_part2.team_B.csv', data_matrix)

    #output coefficients to CSV
    op.generate_csv_coeff('coeff_part2.team_B.csv', param_names, param_vals)
    
    ##performs at -0.064784872847161015 with IND
    ##three param version performs at -0.033414734359919554 with IND
    ##r = scipy.optimize.minimize(f, np.array(params),\
    ##                                        options={'maxiter':1000, 'disp':True})    
    