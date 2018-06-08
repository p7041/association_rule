import numpy as np
import matplotlib.pyplot as plt

class customer():
    def __init__(self,num_of_ppl,s1=5,s2=5):
        self.nop = num_of_ppl
        self.res_p1 = np.random.normal(29.99,s1)
        self.res_p2 = np.random.normal(19.99,s2)
        
def simul(comboPrice,iter=10000,c1=12,c2=8,s1=5,s2=5):
    total_profit = 0
    for i in range(iter):
        cust=customer(2,s1,s2)
        if cust.res_p1 >= 29.99 and cust.res_p2 >= 19.99:
            profit = comboPrice -c1 -c2
        elif cust.res_p1 >= 29.99 and cust.res_p2 >= (comboPrice - 29.99):
            profit = comboPrice -c1 -c2
        elif cust.res_p1 >= (comboPrice - 19.99) and cust.res_p2 >= 19.99:
            profit = comboPrice - c1 -c2
        elif cust.res_p1 >= 29.99:
            profit = 29.99 - c1
        elif cust.res_p2 >= 19.99:
            profit = 19.99 - c2
        else:
            profit = 0
        total_profit += profit
    return round(total_profit,2)


pList = []
for cp in range(30,51):
    pList.append(simul(cp,iter=10000,c1=12,c2=8,s1=5,s2=5))
    
optimal_price = range(30,51)[pList.index(max(pList))]
print("\n Optimal Combo Price is $",optimal_price)

plt.style.use('ggplot')    
plt.plot(range(30,51),pList)
plt.title('Combo Price Simulation')
plt.xlabel('Combo Price')
plt.ylabel('Profit')
plt.show()  


###Simulation with different std values and costs
def param():    
    s1 = list(range(3,11))  
    s2 = list(range(3,11))         
    c1 = list(range(10,16)) 
    c2 = list(range(5,11))    
    param =[]
    for i in s1:
        for j in s2:
            for k in c1:
                for l in c2:
                    param.append([i,j,k,l])
    return param

def fullsimul():
    para = param()
    op_price_list = []
    for i in para:
        pList = []
        for cp in range(30,51):
            pList.append(simul(cp,iter=5000,c1=i[0],c2=i[1],s1=i[2],s2=i[3]))
        optimal_price = range(30,51)[pList.index(max(pList))]
        op_price_list.append(optimal_price)
    return op_price_list
        
        
