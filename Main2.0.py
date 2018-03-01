# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 07:29:44 2018

@author: aziza
"""
import numpy as np 
import Patient as p

def Sim(num_patients):
    #Each loop represents a new patient
    for i in range(num_patients):
        """
        Random sampling a new age, hui, and hba1c for every loop.
        """
        age = np.random.randint(18, 40) # random integer between 18 and 60
        hui = round(np.random.uniform(.7 , .9), 2) #random health utility index
        hba1c = round(np.random.uniform(6.5,14), 2) #random hba1c %
        patient = p.Patient(age,hui,hba1c) #patient instance
        
        """
        1 quarter = 3months. 40 quarters = 10 years
        choose quarter because HbA1c levels change every 3 months
        """
        quarter = 0
        print("starting age= " + str(patient.age))
        while True:
            q_update = patient.q_update(patient.hba1c,patient.hui,mHealth)