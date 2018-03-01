# -*- coding: utf-8 -*-


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
        #return complication
        pass
    
    """
    Patient complication will keep record on what complication patient is suffering from
    should keep a list.
    """
    def complications(self):
        pass
    """
    
    Input is A1C and HUI , out put is updated HUI
    Two methods to update patients attributes, quarterly update and yearly update
    - Quarterly update will update HbA1C, and HUI given that there was a ~ 1%change
    - Yearly Update will update HUI given that the patient developed a new complication
        - Increment patient age +1
        - Complications will be based on probability
        - Each complication decreases HUI, this will occur every year from the time he developed that complication
         until the patient dies or simulation reaches 100 years.
    """
    def y_update(self,A1C, HUI):
        #return updated hui
        pass