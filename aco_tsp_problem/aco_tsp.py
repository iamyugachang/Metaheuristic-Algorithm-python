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

def find_path(ant_list,location_num,alpha,beta,table,dic):
    #find path for n ants
    num = len(ant_list)
    for ant in ant_list:
        destination = prob(ant,location_num,alpha,beta,table,dic)
        ant['path'].append(destination)
        ant['tabu'].append(destination)
    
def prob(ant,num,alpha,beta,table,dic):
    start = ant['path'][-1]
    destin = [x for x in list(range(1,num+1)) if x not in ant['tabu']]
    #print('start:',start)
    #print('destin:',destin)
    pher = []
    sum_pher = 0
    for i in destin:
        delta_x = dic[start][0] - dic[i][0]
        delta_y = dic[start][1] - dic[i][1]
        add = math.pow(table[start-1][i-1],alpha)*math.pow(distance([delta_x,delta_y]),beta)
        pher.append(add)
        sum_pher += add
    #print('pher:',pher)
    index = select(destin,pher,sum_pher)
    
    return destin[index]

def select(destin,pher,sum_pher):
    #score setting
    score = []
    peak = []
    tmp = 0
    for i in pher:
        score.append(i/sum_pher)
        tmp += (i/sum_pher)
        peak.append(tmp)
    
    #print('score,peak:',score,peak)
    #process
    
    num = random.random()
    #print('random:',num)
    mini = 1
    for i in range(len(peak)):
        minus = num-peak[i]
        if abs(minus) < mini:
            mini = abs(minus)

            if minus < 0:
                index = i
            else:
                index = i+1
    return index
def update_pher(ant_list,table,d_rate,dic):
    #generate temp table
    seq = list(range(len(ant_list)))
    tmp_table = []
    for i in seq:
        tmp_table.append([])
        for j in seq:
            tmp_table[i].append(0)
            
    #capture paths ants go through
    for ant in ant_list:
        path = ant['path']
        #analyze path
        #print('path:',path)
        for i in range(len(path)):
            row = path[i]
            col = path[(i+1)%len(path)]
            #print('pre:',row)
            #print('nex:',col)
            delta_x = dic[row][0] - dic[col][0]
            delta_y = dic[row][1] - dic[col][1]
            tmp_table[row-1][col-1] += (ant['pher']/pow(distance([delta_x,delta_y]),2))
            #print(tmp_table[row-1][col-1])
    #update pheromne table
    #print(tmp_table)
    for row in range(len(table)):
        for col in range(len(table[row])):
            if row != col:
                if row < col:
                    tmp = table[row][col]
                    add = tmp_table[row][col] + tmp_table[row][col]
                    table[row][col] = (1-d_rate)*tmp + add
    return table

def distance(axis):
    return round(math.sqrt(axis[0]*axis[0]+axis[1]*axis[1]))

def evalu(seq,dic):
    dist = 0
    for i in range(len(seq)):
        delta_x = dic[seq[i]][0]-dic[seq[(i+1)%len(seq)]][0]
        delta_y = dic[seq[i]][1]-dic[seq[(i+1)%len(seq)]][1]
        
        dist += distance([delta_x,delta_y])
        
    return dist

def determin(ant_list,dic,best_ant):
    #best_ant = ant_list[0]
    
    for ant in ant_list:
        if evalu(ant['path'],dic) < evalu(best_ant['path'],dic):
            best_ant = ant
    return best_ant   
            
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
alpha = 2
beta = 1
d_rate = 0.1
iter_num = input('Please enter the iteration:')
iter_num = int(iter_num)



t1 = time.time()
#Execute
table = gen_pher_table(len(dic))
ant_list = gen_ant(len(dic))
while len(ant_list[0]['path']) <len(dic):
        find_path(ant_list,len(dic),alpha,beta,table,dic)
best_ant = ant_list[0]
best_ant = determin(ant_list,dic,best_ant)    
for i in range(iter_num):
    ant_list = gen_ant(len(dic))
    
    while len(ant_list[0]['path']) <len(dic):
        find_path(ant_list,len(dic),alpha,beta,table,dic)
    
    better_ant = determin(ant_list,dic,best_ant)
    if evalu(better_ant['path'],dic) < evalu(best_ant['path'],dic):
        best_ant = better_ant
        
    print('distance:',evalu(best_ant['path'],dic))
    table = update_pher(ant_list,table,d_rate,dic)

    
   
   
t2 = time.time()        
print('Time: %.2f (second)(不包含I/O時間)'% (t2-t1))
#print('ant_list:',ant_list)
print('distance:',evalu(best_ant['path'],dic))  


#Calculating average and output





