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



profit = []
weight = []
optimal = []
w =0
readfile(profit,weight)
length = len(profit)
capacity = 6404180

#num是現在最大的解
temp = []
t1 = time.time()
num = [[1],[0]]
max_num = []
while 1:
    if len(num[-1]) > len(weight):
        break;
    for i in range(len(num)):
        
        num.append(num[0]+[1])
        num.append(num[0]+[0])
        num.remove(num[0])
        
        
        
for i in range(len(num)):
    if evalu(num[i],profit,weight,capacity) > evalu(max_num,profit,weight,capacity):
        max_num = num[i][:]

            
t2 = time.time()    
print('  Final profit:',evalu(max_num,profit,weight,capacity))
with open('p08_s.txt') as f:
        r = f.read()
        read_data = r.split()
        for i in range(len(read_data)):
            optimal.append(int(read_data.pop()))
        optimal.reverse()
        f.close()
    
print('Optimal profit:',evalu(optimal,profit,weight,capacity))        
print('    Match rate: %.2f %%' % (evalu(max_num,profit,weight,capacity)*100/evalu(optimal,profit,weight,capacity)))
print('          Time: %.2f (second)'% (t2-t1))
print(max_num)






