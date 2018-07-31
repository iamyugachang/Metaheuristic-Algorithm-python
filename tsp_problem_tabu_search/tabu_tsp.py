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

def trans(seq,tabu):
    temp = seq[:]
    while 1:
        index = ran(len(seq))
        if index not in tabu:
            break
        
    t = temp[index[0]]
    temp[index[0]] = temp[index[1]]
    temp[index[1]] = t
    return temp,index

def distance(axis):
    return round(math.sqrt(axis[0]*axis[0]+axis[1]*axis[1]))

def evalu(seq,dic):
    dist = 0
    for i in range(len(seq)):
        delta_x = dic[seq[i]][0]-dic[seq[(i+1)%51]][0]
        delta_y = dic[seq[i]][1]-dic[seq[(i+1)%51]][1]
        
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

#initial        


    #dic={a:b}, a是點的編號(type[int]),b是點的座標(type[list]) (Ex:dic={1:[0,1]})
dic = {}
readfile(dic)
average_num = 30
iter_num = input('Please enter the iteration:')
iter_num = int(iter_num)
tabu_len = 10
#initial result
result = {}
for i in range(1,iter_num+1):
    result[i] = 0
    
#Execute
for j in range(average_num):
    seq = init(len(dic))
    tabu_list = []
    index = []
    temp = []
    for i in range(1,iter_num+1):
    
        
        (temp,index) = trans(seq,tabu_list)

    
        seq = determin(temp,seq,dic)
        if temp != seq:
            if len(tabu_list) == tabu_len:
                tabu_list.pop(0)
            
            tabu_list.append(index)
            #print(tabu_list)
        result[i] += evalu(seq,dic)
        

       

##Output
#print('Final sequence:',seq)
#print('Final distance:',evalu(seq,dic))
        
#Calculating average and output
with open('output_tabu.txt','r+') as f:
    f.truncate(0)
    f.close()
for i in range(1,iter_num+1):
    with open('output_tabu.txt','a') as f:
        f.write(str(i))
        f.write(' ')
        f.write(str(result[i]/average_num))
        f.write('\n')
        f.close()




