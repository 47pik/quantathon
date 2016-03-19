import csv
import os

def generate_csv(filename, data_matrix):
    with open(os.path.join('deliverables', filename), 'wb+') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        header = ['yyyymmdd', 'return', 'cumulative_return', 'mean_abs_weight', 'portfolio_direction']
        stocks = ['Stock_' + str(i) for i in range(0, 100)]
        writer.writerow(header + stocks)
        writer.writerows(data_matrix)
        