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


    

def gen_ant(num):
    #template = {'id':0,'path':[],'tabu':[],'pher':100}
    ant_list = []
    for i in range(num):
        ant_list.append({'id':i,'path':[i+1],'tabu':[i+1],'pher':100})
    return ant_list
    

def gen_pher_table(num):
    seq = list(range(num))
    table = []
    for i in seq:
        table.append([])
        for j in seq:
            table[i].append(100)
            if i == j:
                table[i][j] = -1
    return table

def find_path():

def prob(ant,num,alpha,beta,table,dic):
    start = ant['path'][-1]
    destin = [x for x in list(range(1,num+1)) if x not in ant['tabu']]
    pher = []
    sum_pher = 0
    for i in destin:
        delta_x = dic[start][0] - dic[i][0]
        delta_y = dic[start][1] - dic[i][1]
        add = math.pow(table[start-1][i-1],alpha)*math.pow(distance([delta_x,delta_y])),beta)
        pher.append(add)
        sum_pher += add
    select(destin,pher,sum_pher)

def select(destin,pher,sum_pher):
    #score setting
    score = []
    peak = []
    tmp = 0
    for i in range(len(chromo_data['distance'])):
        score.append(1/chromo_data['distance'][i])
    for i in range(len(chromo_data['distance'])):
        tmp+= (score[i]/sum(score))
        peak.append(tmp)
   # print(score,peak)
    #process
    new_chromo = {'chromo':[],'distance':[]}
    
    for i in range(len(chromo_data['distance'])):
        num = random.random()
        #print(num)
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


    #dic={a:b}, a是點的編號(type[int]),b是點的座標(type[list]) (Ex:dic={1:[0,1]})
dic = {}
readfile(dic)
chromo_num = 5
iter_num = input('Please enter the iteration:')
iter_num = int(iter_num)



t1 = time.time()
#Execute


    
   
   
t2 = time.time()        
print('Time: %.2f (second)(不包含I/O時間)'% (t2-t1))
print(chromo_data['distance'])       


#Calculating average and output





