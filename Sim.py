# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 14:15:28 2018

@author: aziza
"""
import numpy as np
import Patient

class Sim:
    def __init__(self, numruns):
        self.numruns = numruns
        for i in range(numruns):
            age = np.random.randint(18, 60) #random age
            hui = round(np.random.uniform(.7 , .9), 2) #random health utility index
            hba1c = round(np.random.uniform(7,14), 2) #random hba1c level
            patient = Patient.Patient(age,hui,hba1c)
            print('num run = ' + str(i))
    
    