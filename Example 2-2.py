# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 11:17:58 2024

@author: mdubo
"""

import matplotlib.pyplot as plt
import numpy as np

'''Imports data files'''
file_nameA = "C:/Users/mdubo/OneDrive/Desktop/WD/g149novickA.csv"
data_setA = np.loadtxt(file_nameA, delimiter = ',');

file_nameB = "C:/Users/mdubo/OneDrive/Desktop/WD/g149novickB.csv"
data_setB = np.loadtxt(file_nameB, delimiter = ',');

'''Extracts data from data file A'''
tA = np.array(data_setA[:, 0]);
galacA = np.array(data_setA[:, 1]);

'''Set parameters for approx. fit of data set A using V(t)'''
tau = 3.5;

V = 1 - np.exp(-tA/tau);

'''Plots data set A information with approx fit'''
plt.figure(figsize=(15, 10));
plt.plot(tA, galacA, 'r+')
plt.plot(tA, V);
plt.xlabel("Time (sec)")
plt.ylabel("Galactosidase Population According to the function V(t)")
plt.title("Production of Galactosidase in E.coli after introducing TMG over time with tau = 3.5, Overlayed with actual data")
plt.tight_layout()
plt.show()

'''Extracts and slices data from data file B'''
tB = np.array(data_setB[:, 0]);

tB = tB[:11];
galacB = np.array(data_setB[:11, 1]);

'''Sets parameters for W(t) fit using data file B'''
A = 0.014168;
tau = 1.36016;

W = A*(np.exp(-tB/tau)-1+(tB/tau));

'''Plots data file B information using W(t) fit'''
plt.figure(figsize=(15, 10));
plt.plot(tB, galacB, 'r+')
plt.plot(tB, W);
plt.xlabel("Time (sec)")
plt.ylabel("Galactosidase Population According to the function W(t)")
plt.title("Production of Galactosidase in E.coli after introducing TMG over time with A = 0.014168 tau = 1.36016, Overlayed with actual data")
plt.tight_layout()
plt.show()