# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 03:20:23 2018

@author: stesn
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import solve

def f(x):
    return np.sin(x/5.)*np.exp(x/10.) + 5.*np.exp(-x/2.)

A= [[1., 1., 1., 1],
    [1., 15., 15*15, 15*15*15],
    [1., 4., 4*4, 4*4*4],
    [1., 10., 10*10, 10*10*10]]
B = [f(1), f(15), f(4), f(10)]
X = solve(A,B)

def f_1(x):
    return X[0] + X[1]*x + X[2]*x*x + X[3]*x*x*x

x = np.arange(1,15,0.1) 

plt.plot(x, f(x))
plt.plot(x, f_1(x))
file = open('ans2.txt', 'w')
file.write(str(X)[2:-1])
file.close()