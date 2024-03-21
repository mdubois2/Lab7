# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 12:33:16 2024

@author: mdubo
"""

import matplotlib.pyplot as plt
import numpy as np

file_name = "C:/Users/mdubo/OneDrive/Desktop/WD/HIVseries.csv" #Imports file
data_set = np.loadtxt(file_name, delimiter = ',');

t_treatment = np.array(data_set[:, 0]); #Extracts data from file
virus_pop = np.array(data_set[:, 1]);


'''Sets parameters for fit'''
A = -6000;
B = 180000;
alpha = 0.000092;
beta = 0.63;
viral_load = (A*np.exp(alpha*t_treatment) + B*np.exp(-beta*t_treatment));

'''Plots data with approximated fit with V(t) function'''
plt.figure(figsize=(15, 10));
plt.plot(t_treatment, virus_pop, 'r+')
plt.plot(t_treatment, viral_load);
plt.xlabel("Time (days)")
plt.ylabel("HIV Population")
plt.title("Production of HIV Over A Week Period using the Viral Load model, using Parameters A = -6000, B = 180000, alpha = 0.000092, beta = 0.63, Overlayed with Data")
plt.tight_layout()
plt.show()


'''Part C:
    The model suggests that when HIV invades a healthy body, its initial infection rate is
    extremely high. However, as the amount of healthy cells decreases, the rate of infection
    also seems to decrease. This suggests that the latency period of HIV is long because 
    as there are less and less cells, it is harder for HIV to continue infecting new cells,
    leading to a latency period of 10 years.'''