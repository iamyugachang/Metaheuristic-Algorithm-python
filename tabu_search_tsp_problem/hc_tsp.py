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
seq = init(51)
temp = []
#dic={a:b}, a是點的編號(type[int]),b是點的座標(type[list])
dic = {}
readfile(dic)
min_dist = 0
iter_num = input('Please enter the iteration:')
iter_num = int(iter_num)

#initial output file
with open('test.txt','r+') as f:
    f.truncate(0)
    f.close()

#Execute
for i in range(iter_num):
    temp = trans(seq)
    seq = determin(temp,seq,dic)
    
    with open('test.txt','a') as f:
        
        f.write(str(i+1))
        f.write(' ')
        f.write(str(evalu(seq,dic)))
        f.write('\n')
        f.close()

#Output
print('Final sequence:',seq)
print('Final distance:',evalu(seq,dic))

with open('eil51_optimal.txt') as f:
        a = []
        r = f.read()
        read_line = r.split()               
        for i in range(len(read_line)):
            a.append(int(read_line.pop(0)))
        f.close()
print('Optimal distance:',evalu(a,dic))



