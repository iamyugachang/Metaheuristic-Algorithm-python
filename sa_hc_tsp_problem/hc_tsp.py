import sys
import time
import math
import random
#transition     任兩個互換
#evalutation    連線距離和 
#determination  距離短者獲勝
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

def distance(axis):
    return round(math.sqrt(axis[0]*axis[0]+axis[1]*axis[1]))

def evalu(seq,dic):
    dist = 0
    for i in range(len(seq)):
        d = [ dic[seq[i]][0]-dic[seq[(i+1)%51]][0],dic[seq[i]][1]-dic[seq[(i+1)%51]][1]]
        dist += distance(d)
        
    return dist

def determin(temp,seq,dic):
    if evalu(temp,dic) < evalu(seq,dic):
        seq = temp[:]
        
            
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
dic = {}
readfile(dic)
min_dist = 0
iter_num = input('Please enter the iteration:')
iter_num = int(iter_num)

#Execute
for i in range(iter_num):
    temp = trans(seq)
    determin(temp,seq,dic)

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

