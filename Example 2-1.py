# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 11:00:58 2024

@author: mdubo
"""

import matplotlib.pyplot as plt
import numpy as np

'''Sets parameters for W(t) function'''
A = 1;
tau = 1;
t = np.linspace(0, 2, 51);

W = [];

'''Calculation of W(t) for different parameters'''
for i in range(4):
    W.append(A*(np.exp(-t/tau)-1+(t/tau)));
    
    '''changes parameters for new W(t) calculation'''
    A = A + 42.7;
    tau = tau + 4.8

'''Plots different W(t) models for different parameters'''
plt.figure(figsize=(15, 10));
plt.plot(t, W[0], color = 'red', label = 'A = 1, tau = 1');
plt.plot(t, W[1], color = 'green', linestyle = 'dashed', label = 'A = 43.7, tau = 5.8');
plt.plot(t, W[2], color = 'blue', linestyle = 'dashdot', label = 'A = 86.4, tau = 10.6');
plt.plot(t, W[3], color = 'purple', linestyle = 'dotted', label = 'A = 129.1, tau = 15.4');
plt.legend();
plt.xlabel("Time (sec)")
plt.ylabel("Galactosidase Population According to the function W(t)")
plt.title("Production of Galactosidase in E.coli after introducing TMG over time");