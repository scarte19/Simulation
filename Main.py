# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 10:51:02 2018

@author: Abdulaziz Attas, Semion Carter
"""
import numpy as np 
import Patient as p

def Sim(numruns):
    for i in range(numruns):
            age = np.random.randint(18, 60) #random age
            hui = round(np.random.uniform(.7 , .9), 2) #random health utility index
            hba1c = round(np.random.uniform(7,14), 2) #random hba1c level
            patient = p.Patient(age,hui,hba1c)
            print('age = ' + str(patient.age))
            print('num run = ' + str(i))

Simulation = Sim(5)
