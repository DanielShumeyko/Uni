# Daniel Shumeyko \\ Applied Statistics 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math

Lambdas = [[1, 4], [3, 7], [8, 12], [15, 19], [10, 20], [5, 22], [3, 24]] #Pairs of lambda values and ends of their time periods 


def simulate_period(previous_t, lam_t): # simulates homogenous poisson process with certain rate and up to a certain point of time. Rate and stop time are set using the lam_t argument which should be a list with 2 elements. Argument cumsum passes all the values during previous periods of time.
    cumsum = previous_t 
    while True:
        new_elmnt = np.random.exponential( 1/lam_t[0] )
        if cumsum[-1] + new_elmnt <= lam_t[1]:  # because we will almost certainly never get our exact end of time period value, we just take the closest one that is less or equal to it
            cumsum.append(cumsum[-1] + new_elmnt)
        else:
            cumsum.append(lam_t[1]) # then we add the desired end of time period manually
            return cumsum

def simulate(): # simulates inhomogenous poisson process for lambda and time period given above (Lambdas variable)
    t_sum = [0]
    for period in Lambdas:
        t_sum = simulate_period(t_sum, period)
    return t_sum

def plot_process(process):
    sns.set()
    x = process
    y = np.arange(0, len(process))
    plt.step(x,y, c='crimson')
    plt.xlabel('time')
    plt.ylabel('process')
    plt.suptitle('Nonhomogenous Pоisson Process', fontsize=25)
    plt.show()


if __name__ == "__main__":
    plot_process(simulate())  

