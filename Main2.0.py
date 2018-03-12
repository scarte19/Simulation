# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 07:29:44 2018

@author: aziza
"""
import numpy as np 
import Patient as p

def Sim(num_patients, mHealth):
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
            q_init = patient.hba1c #HbA1c at the beggining of the quarter
            q_final = patient.q_update(patient.hba1c,patient.hui, mHealth) #HbA1c at the end of the quarter
            quarter+= 1
            #If the change in HbA1C is between 0.8 and 1.2 and +ive (means it increased), decrease HUI
            if 0.8 <= abs(q_final - q_init) <= 1.2 and q_final - q_init > 0:
                patient.hui+= -0.03
            if quarter % 4 == 0: #If a year has passed
                compl = patient.det_complication(patient.hba1c) #determine the complication penalty
                patient.hui+= compl  # add complication penalty to HUI
                #print("complication is : " + str(compl))
                patient.age+=1
            #While loop break conditions
            if quarter == 120 or patient.hui <= 0 or patient.age >= 90:
                break
            
        #print('quarter = ' + str(quarter))
        print("patient age =" + str(patient.age))
        print("patient hui =" + str(round(patient.hui,2)))
        print("patient hba1c =" + str(patient.hba1c))

Simulation = Sim(1,False)  