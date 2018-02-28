# -*- coding: utf-8 -*-


class Patient:
    #Patient class 
    def __init__(self,age,hui,hba1c):
        self.hba1c = hba1c
        self.age = age
        self.hui = hui
        
    """
    Method to update paitent diabetic complication
    Complications include:
        1. Blindness, HUI = -0.170, weight = 0.552
        2. Amputation, HUI = -0.105, weight = 0.102
        3. Neuropathy, HUI = -0.065, weight = 0.072
        4. Stroke,     HUI = -0.044, weight = 0.920
        5. 
    """
    def complication(self):
        pass