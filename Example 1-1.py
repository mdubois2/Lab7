# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 08:24:43 2024

@author: mdubo
"""

import matplotlib.pyplot as plt
import numpy as np

'''sets initial variables for graphing'''
t = np.linspace(1, 10, 101);
viral_load = [];
A = 12;
B = 0;
alpha = 0.42;
beta = 0.78;

'''Calculation of V(t) for different parameters'''
for i in range(3):
    viral_load.append(A*np.exp(alpha*t) + B*np.exp(-beta*t)); #Calculates V(T) for given parameters
    
    '''Changes set of parameters for V(t) calculation)'''
    A = A - 1.7;
    B = B + 2.3;
    alpha = alpha + 0.09;
    beta = beta - 0.12;
    
'''Graphs each V(t) for each parameter set'''
    
plt.subplots(1, 3, figsize=(30, 10))

plt.subplot(1,3,1)
plt.plot(t, viral_load[0])
plt.xlabel("Time (sec)")
plt.ylabel("Viral Load")
plt.title("The Viral Load of an HIV Patient over Time with Parameters A = 12, B = 0, alpha = 0.42, beta = 0.72")

plt.subplot(1,3,2)
plt.plot(t, viral_load[1])
plt.xlabel("Time (sec)")
plt.ylabel("Viral Load")
plt.title("The Viral Load of an HIV Patient over Time with Parameters A = 10.3, B = 2.3, alpha = 0.51, beta = 0.60")

plt.subplot(1,3, 3)
plt.plot(t, viral_load[2])
plt.xlabel("Time (sec)")
plt.ylabel("Viral Load")
plt.title("The Viral Load of an HIV Patient over Time with Parameters A = 8.6, B = 4.6, alpha = 0.60, beta = 0.48")
plt.tight_layout()
plt.show()
    