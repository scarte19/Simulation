# -*- coding: utf-8 -*-
import numpy as np

class Patient:
    #Patient class 
    def __init__(self,age,hui,hba1c):
        self.hba1c = hba1c
        self.age = age
        self.hui = hui
        
    """
    Method should take in self.hba1c as input and output the complication
    Method to update paitent diabetic complication
    Complications include:
        1. Blindness, HUI = -0.170, weight = 0.552
        2. Amputation, HUI = -0.105, weight = 0.102
        3. Neuropathy, HUI = -0.065, weight = 0.072
        4. Stroke,     HUI = -0.044, weight = 0.920
        5. 
    Complications will be determined by chance? and complication chance changes based on
    the yearly HbA1C level.
    """
    def det_complication(self,A1C):
        complication_dict = {"Blindness":-0.170,
                            "Amputation":-0.105,
                            "Neuropathy":-0.065,
                            "Stroke":-0.044,
                            "Nothing":0.00
                            }
        #complication_list = list(complication_dict.values)
        #prob_complications = np.random.choice(len(5),1)
        #print("complication is: " + str(prob_complications))
        #return prob_complications
        #return None
    """
    Patient complication will keep record on what complication patient is suffering from
    should keep a list.
    """
    def complications(self):
        pass
    """
    
    Input is patient's A1C,HUI and if mHealth is present , output is updated HUI
    Two methods to update patients attributes, quarterly update and yearly update
    - Quarterly update will update HbA1C, and HUI given that there was a ~ 1%change
    - Yearly Update will update HUI given that the patient developed a new complication
        - Increment patient age +1
        - Complications will be based on probability
        - Each complication decreases HUI, this will occur every year from the time he developed that complication
         until the patient dies or simulation reaches 100 years.
    """
    def q_update(self, A1C, hui, mHealth):
        self.hba1c = A1C
        self.hui = hui
        if mHealth == True: #IF mhealth is present A1C changes by given range
            q_hba1c = A1C + round(np.random.uniform(-1, 0.8),2)
        else: #if mhealth is not present A1C changes by given range
            q_hba1c = A1C + round(np.random.uniform(-0.5, 1.0), 2)
        return q_hba1c
    
    def y_update(self, A1C, hui, age, mHealth):
        self.hba1c = A1C
        self.hui = hui
        self.age = age + 1
        
        #return updated hui
        pass
    
    