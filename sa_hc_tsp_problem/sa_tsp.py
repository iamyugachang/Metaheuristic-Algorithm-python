import sys
import time
import math
import random
#transition
#evalutation
#determination
def ran(domain):
    num = []
    num.append(random.randint(1,domain))
    num.append(random.randint(1,domain))
    return num

def init(num):
    seq = []
    while len(seq) < num:
        
        temp = random.randint(1,num)
        if temp not in seq:
            seq.append(temp)
    return seq

 def trans(seq):
    temp = seq[:]
    index = ran(len(seq))
    t = temp[index[0]-1]
    temp[index[0]-1] = temp[index[1]-1]
    temp[index[1]-1] = t
    return temp

def neighbor_f(seq,num):
    neighbor = []
    for i in range(num):
        tmp = trans(seq)
        if tmp not in neighbor:
            neighbor.append(tmp)
    return neighbor
def distance(axis):
    return round(math.sqrt(axis[0]*axis[0]+axis[1]*axis[1]))

def evalu(seq,dic):
    dist = 0
    for i in range(len(seq)):
        d = [ dic[seq[i]][0]-dic[seq[(i+1)%51]][0],dic[seq[i]][1]-dic[seq[(i+1)%51]][1]]
        dist += distance(d)
        
    return dist

def determin(neighbor,seq_current,dic,temperature,seq_best):  
    index = random.randint(0,len(neighbor)-1)
    value = evalu(neighbor[index],dic) - evalu(seq_current,dic)
    #print('chosen neighbor distance',evalu(neighbor[index],dic))
    if value <= 0:
        seq_current = neighbor[index]
        seq_best = seq_current[:]
        #print('changed !',evalu(seq_current,dic))
    else :
        r = random.random()
        if math.exp((-10)*value/temperature) >= r:
            
            seq_current = neighbor[index]
            
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
def get_stddev(list):
    average = get_average(list)
    sdsq = sum([(i - average) ** 2 for i in list])
    stdev = (sdsq / (len(list) - 1)) ** .5
    return stdev

#initial        

dic = {}
readfile(dic)

#Execute
t1 = time.time()
statistic = []
for i in range(10):
    seq_current = init(51)
    neighbor = []
    count = 0
    t_max = 100
    t_min = 10
    seq_best = []
    while t_max > t_min:
    
    
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
            t_max *= 0.999
            count = 0
            #print(t_max)
        #if time.time() > t1+50:
        #    break
   
    
    
    

    #Output
    print('current seq distance',evalu(seq_current,dic))
    statistic.append(evalu(seq_current,dic))
    

print('           Average:',get_average(statistic))
print('Standard deviation:',get_stddev(statistic))
