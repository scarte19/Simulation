# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 10:51:02 2018

@author: Abdulaziz Attas, Semion Carter
"""
import numpy as np 
import Patient as p

def Sim(num_patients):
    #Each loop represents a new patient
    for i in range(num_patients):
        """
        Generating a new age, hui, and hba1c for every loop.
        """
        age = np.random.randint(18, 60) # random integer between 18 and 60
        hui = round(np.random.uniform(.7 , .9), 2) #random health utility index
        hba1c = round(np.random.uniform(6.5,14), 2) #random hba1c %
        patient = p.Patient(age,hui,hba1c) #patient instance
            
            
            

Simulation = Sim(5) #call sim function
