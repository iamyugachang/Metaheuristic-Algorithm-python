import sys
import time
import math
import random
#transition     任兩個互換
#evalutation    連線距離和 
#determination  距離短者獲勝
#note:
#random.randint(a,b) --> a <= x <= b
#range(a,b) --> a <= x < b
#senario: fitness(), select(), crossover(), mutation()
#Data structure: chromo_data = {'chromo':[],'distance':[]}

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

def distance(axis):
    return round(math.sqrt(axis[0]*axis[0]+axis[1]*axis[1]))

def evalu(seq,dic):
    dist = 0
    for i in range(len(seq)):
        delta_x = dic[seq[i]][0]-dic[seq[(i+1)%len(seq)]][0]
        delta_y = dic[seq[i]][1]-dic[seq[(i+1)%len(seq)]][1]
        
        dist += distance([delta_x,delta_y])
        
    return dist

def determin(temp,seq,dic):
    if evalu(temp,dic) < evalu(seq,dic):
        seq = temp[:]
    return seq    
            
def readfile(dic):
    with open('eil51.txt') as f:
        r = f.read()
        read_line = r.split('\n')               
        for i in range(len(read_line)):         
            read_element = read_line[i].split() 
            dic[int(read_element[0])] = [int(read_element[1])]
            dic[int(read_element[0])].append(int(read_element[2]))
        f.close()

def fitness(chromo_data,dic):
    #clear chromosome distance
    chromo_data['distance'] = []
    #calculate distance of each chromosome
    for i in range(len(chromo_data['chromo'])):
        chromo_data['distance'].append(evalu(chromo_data['chromo'][i],dic))
    
def select(chromo_data):
    #score setting
    score = []
    peak = []
    tmp = 0
    for i in range(len(chromo_data['distance'])):
        score.append(1/chromo_data['distance'][i])
    for i in range(len(chromo_data['distance'])):
        tmp+= (score[i]/sum(score))
        peak.append(tmp)
    print(score,peak)
    #process
    new_chromo = {'chromo':[],'distance':[]}
    
    for i in range(len(chromo_data['distance'])):
        num = random.random()
        print(num)
        mini = 1
        for i in range(len(chromo_data['distance'])):
            minus = num-peak[i]
            if abs(minus) < mini:
                mini = abs(minus)
                if minus < 0:
                    index = i
                else:
                    index = i+1
        new_chromo['chromo'].append(chromo_data['chromo'][index])
                
    
    return new_chromo

def crossover(chromo_data,c_rate):
    if random.random() > c_rate:
        return 0
    new_chromo = {'chromo':[],'distance':[]} 
    while 1:
        test1 = chromo_data['chromo'].pop(random.randint(0,len(chromo_data['chromo'])-1))
        test2 = chromo_data['chromo'].pop(random.randint(0,len(chromo_data['chromo'])-1))
        index1 = random.randint(0,len(tmp1)-1)
        index2 = random.randint(0,len(tmp2)-1)
        new1 = tmp1[index1:index2+1]
        new2 = tmp2[index1:index2+1]
        
    #do one of the methods in crossover
    #check crossover probability
    return final_result_of_all_chromosome
def mutation():
    #do one of the methods in mutation 
    #check mutation probability
    return final_result_all_chromosome
    

#initial        


    #dic={a:b}, a是點的編號(type[int]),b是點的座標(type[list]) (Ex:dic={1:[0,1]})
dic = {}
readfile(dic)

iter_num = input('Please enter the iteration:')
iter_num = int(iter_num)



t1 = time.time()
#Execute

seq = init(len(dic))
temp = []
for i in range(1,iter_num+1):  
    temp = trans(seq)
    seq = determin(temp,seq,dic)
    #result[i] += evalu(seq,dic)

t2 = time.time()        
print('Time: %.2f (second)(不包含I/O時間)'% (t2-t1))
       


#Calculating average and output





