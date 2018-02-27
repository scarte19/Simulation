# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 15:54:17 2018

@author: aziza
"""
import numpy as np
def sim(n):
    for simnum in range (n):
            age = np.random.randint(18, 60) 
            hui = round(np.random.uniform(.7 , .9), 2)
            hba1c = round(np.random.uniform(7,14), 2) 
            
        