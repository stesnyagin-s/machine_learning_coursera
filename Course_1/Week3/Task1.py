# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 15:56:19 2018

@author: stesn
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize
from scipy.optimize import differential_evolution

def f(x): #[1;30]
    return np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)
def h(x):
    return int(f(x))

x = np.arange(1,30,0.1) 

plt.plot(x, f(x))
file = open('ans1.txt', 'w')
result_1 = minimize(f,2, method='BFGS').fun
result_2 = minimize(f,30, method='BFGS').fun
file.write('{:.2f} '.format(result_1))
file.write('{:.2f}'.format(result_2))
file.close()

file = open('ans2.txt', 'w')
result = differential_evolution(f, [(1,30)]).fun[0]
file.write('{:.2f} '.format(result))
file.close()

vfunc = np.vectorize(h)
plt.plot(x, vfunc(x))
result_1 = minimize(h,30, method='BFGS').fun
result_2 = differential_evolution(h, [(1,30)]).fun
file = open('ans3.txt', 'w')
file.write('{:.2f} '.format(result_1))
file.write('{:.2f}'.format(result_2))
file.close()