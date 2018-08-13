import sys
import random
import time


#function definition
def init(length):
    num = []
    for i in range(length):
        num.append(random.randint(0,1))
    return num

def trans(num):
    temp = num[:]
    rand_index = random.randrange(len(num))
    temp[rand_index] = (temp[rand_index]+1)%2
    return temp    

def evalu(num,profit,weight,capacity):
    result = 0
    w = 0
    for i in range(len(num)):
        
        w += weight[i]*num[i]
        if w > capacity:
            return 0
        result += profit[i]*num[i]
    return result

def readfile(profit,weight):
    with open('p08_p.txt') as f:
        r = f.read()
        read_data = r.split()
        for i in range(len(read_data)):
            profit.append(int(read_data.pop(0)))
        
        f.close()
    with open('p08_w.txt') as f:
        r = f.read()
        read_data = r.split()
        for i in range(len(read_data)):
            weight.append(int(read_data.pop(0)))
       
        f.close()
#Main

iter_num = 10000

profit = []
weight = []
optimal = []
w =0
readfile(profit,weight)
length = len(profit)
capacity = 6404180
store_max_length = 10
store = []
num = init(length)
#num是現在最大的解
temp = []
store.append(num)
t1 = time.time()
for i in range(iter_num):
    temp = trans(store[-1])
    if evalu(temp,profit,weight,capacity) > evalu(num,profit,weight,capacity):
        
        num = temp[:]
        store = [num]
        
    else:
        if len(store) > store_max_length:
            store = [num]
        else:
            store.append(temp)
t2 = time.time()    
print('  Final profit:',evalu(num,profit,weight,capacity))
with open('p08_s.txt') as f:
        r = f.read()
        read_data = r.split()
        for i in range(len(read_data)):
            optimal.append(int(read_data.pop()))
        optimal.reverse()
        f.close()
    
print('Optimal profit:',evalu(optimal,profit,weight,capacity))        
print('    Match rate: %.2f %%' % (evalu(num,profit,weight,capacity)*100/evalu(optimal,profit,weight,capacity)))
print('          Time: %.2f (second)'% (t2-t1))
print(num)






