# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 10:51:02 2018

@author: Abdulaziz Attas, Semion Carter
"""
import numpy as np 
import Patient as p

def Sim(num_patients, mHealth):
    #Each loop represents a new patient
    for i in range(num_patients):
        """
        Generating a new age, hui, and hba1c for every loop.
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
        while patient.hui > 0.1  and quarter < 400 and patient.age < 100:  
            q_hba1c = patient.hba1c + round(np.random.uniform(-0.5,1.0), 2) # random change in Hba1C 
            # 1% change during quarter visit and HbA1C increased
            if 0.9 <= abs(q_hba1c - patient.hba1c) <= 1.1 and q_hba1c - patient.hba1c > 0: 
                patient.hui+= -0.03
                print("decreased hui")
#            elif patient.hui < 1:
#                patient.hui+= 0.03
            if quarter % 4 == 0: #year has passed
                patient.age+= 1
            quarter+=1
            if 6.5 < q_hba1c < 20: #capping hba1c at 20
                patient.hba1c = q_hba1c
            
        print("patient age =" + str(patient.age))
        print("patient hui =" + str(patient.hui))
        print("patient hba1c =" + str(patient.hba1c))
        
Simulation = Sim(1,False) #call sim function
