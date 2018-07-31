import sys
import time
import math
import random
#transition
#evalutation
#determination
def ran(domain):
    first = 0
    second = 0
    while first == second:
        first   = random.randint(0,domain-1)
        second  = random.randint(0,domain-1)
        
    return [first,second]

def init(num):
    seq = []
    list_1_to_num = list(range(1,num+1))
    while len(list_1_to_num) > 0:
        index = random.randint(0,len(list_1_to_num)-1)
        seq.append(list_1_to_num.pop(index))
    return seq

def trans(seq):
    temp = seq[:]
    index = ran(len(seq))   
    t = temp[index[0]]
    temp[index[0]] = temp[index[1]]
    temp[index[1]] = t
    return temp

def neighbor_f(seq,num):
    neighbor = []
    index = random.randint(0,num-1)
    while len(neighbor) < num:
        tmp = trans(seq)
        if tmp not in neighbor:
            neighbor.append(tmp)
    
    return neighbor[index]
def distance(axis):
    return round(math.sqrt(axis[0]*axis[0]+axis[1]*axis[1]))

def evalu(seq,dic):
    dist = 0
    for i in range(len(seq)):
        delta_x = dic[seq[i]][0]-dic[seq[(i+1)%51]][0]
        delta_y = dic[seq[i]][1]-dic[seq[(i+1)%51]][1]
        
        dist += distance([delta_x,delta_y])
        
    return dist

def determin(neighbor,seq_current,dic,temperature,seq_best):  
    
    value = evalu(neighbor,dic) - evalu(seq_current,dic)
    #print('chosen neighbor distance',evalu(neighbor[index],dic))
    if value <= 0:
        seq_current = neighbor[:]
        seq_best = seq_current
        #print('changed !',evalu(seq_current,dic))
    else :
        r = random.random()
        if math.exp((-10)*value/temperature) > r:
            
            seq_current = neighbor
            
    return seq_current,seq_best        
            
            
        
            
def readfile(dic):
    with open('eil51.txt') as f:
        r = f.read()
        read_line = r.split('\n')               
        for i in range(len(read_line)):         
            read_element = read_line[i].split() 
            dic[int(read_element[0])] = [int(read_element[1])]
            dic[int(read_element[0])].append(int(read_element[2]))
        f.close()
def get_average(list):
    sum = 0
    for item in list:
        sum += item
    return sum/len(list)


#initial        

dic = {}
readfile(dic)
average_num = 30
average = []
iter_num = input('Please enter the iteration:')
iter_num = int(iter_num)
    #initial result
result = {}
for i in range(1,iter_num+1):
    result[i] = 0
#Execute
t1 = time.time()
#statistic = []
for j in range(average_num):
    seq_current = init(len(dic))
    neighbor = []
    count = 0
    t_max = 100
    t_min = 10
    seq_best = []
    for i in range(1,iter_num+1):
    
    
        best_value = evalu(seq_best,dic)
        neighbor = neighbor_f(seq_current,7)
        #print('current seq distance',evalu(seq_current,dic))
        (seq_current,seq_best) = determin(neighbor,seq_current,dic,t_max,seq_best)

        #降溫機制：
        if evalu(seq_current,dic) >= best_value:
            count += 1
        else:
            count = 0
            
            #print(best_value)
        if count == 10:
            t_max *= 0.99
            count = 0
            seq_current = seq_best[:]
        #print(evalu(seq_current,dic))
        result[i] += evalu(seq_current,dic)
   
    
    
    

    #Output
    #print('current seq distance',evalu(seq_current,dic))
    #statistic.append(evalu(seq_current,dic))
    
#Calculating average and output
with open('output_sa.txt','r+') as f:
    f.truncate(0)
    f.close()
for i in range(1,iter_num+1):
    with open('output_sa.txt','a') as f:
        f.write(str(i))
        f.write(' ')
        f.write(str(result[i]/average_num))
        f.write('\n')
        f.close()
#print('           Average:',get_average(statistic))

