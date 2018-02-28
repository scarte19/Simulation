import numpy as np
def Sim(n):
    init_age = np.random.randint(18, 60) 
    init_hui = round(np.random.uniform(.7 , .9), 2)
    init_hba1c = round(np.random.uniform(7,14), 2)
    age = init_age
    hui = init_hui
    hba1c = init_hba1c
    period = 0
    for patients in range(n):
        print('paitent no. = ' + str(n))
        while hui > 0.1 and period !=20:
            for i in range(20):
                starting_hba1c = hba1c
                if hba1c > 6.5 and hba1c < 20:
                    hba1c = hba1c + round(np.random.uniform(-1.1,1.1), 2)
                    #print('updated hba1c = ' + str(hba1c))
                if starting_hba1c - hba1c == 1:
                    hui = hui - 0.03
                    #print('hui -0.03')
                period+=1
                    
            print('after forloop updated hui =' + str(hui))
                
            

simulation = Sim(5)