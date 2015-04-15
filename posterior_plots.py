# import necessary modules
import numpy as np
import triangle

# read in data and set true values
datafile = 'chains/analysis_n0100_n1200_n2100_seed4143_post_equal_weights.dat'
data = np.loadtxt(datafile, usecols=(0,1,2))
n0_true = 1.00
n1_true = 2.00
n2_true = -1.00
print data.shape

# plot it
figure = triangle.corner(data, labels=[r'$n_0$',r'$n_1$',r'$n_2$'],
                         truths=[n0_true, n1_true, n2_true],
                         quantiles=[0.16, 0.5, 0.84], show_titles=True,
                         title_args={"fontsize": 12},
                         bins=30)
figure.savefig("test_posterior.png")
