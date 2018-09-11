import sys
import time
import math
import random
#import PyGnuplot as gp
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
            table[i].append(0.000167)
            if i >= j:
                table[i][j] = -1
    return table

def find_path(ant_list,location_num,alpha,beta,table,dic):
    #find path for n ants only one step
    #num = len(ant_list)
    with open('data_test/log.txt','a') as f:
        f.write('current table:\n')
        for i in range(len(table)):
            for j in range(len(table[i])):
                f.write(str(table[i][j]))
                f.write('   ')
            f.write('\n')
        f.close()
    while len(ant_list[0]['path']) < location_num:
        
        for ant in ant_list:
            destination = prob(ant,location_num,alpha,beta,table,dic)
            ant['path'].append(destination)
            ant['tabu'].append(destination)
        with open('data_test/log.txt','a') as f:
            f.write('current ant_list'+str(ant_list)+'\n')
            f.close()
            
    
def prob(ant,num,alpha,beta,table,dic):
    start = ant['path'][-1]
    destin = [x for x in list(range(1,num+1)) if x not in ant['tabu']]
    with open('data_test/log.txt','a') as f:
        f.write('from '+str(start)+' to '+str(destin)+'\n')
        f.close()
        
    #print('start:',start)
    #print('destin:',destin)
    pher = []
    
    for i in destin:
        delta_x = dic[start][0] - dic[i][0]
        delta_y = dic[start][1] - dic[i][1]
        if start < i:
            add = math.pow(table[start-1][i-1],alpha)*math.pow(1/distance([delta_x,delta_y]),beta)
        else:
            add = math.pow(table[i-1][start-1],alpha)*math.pow(1/distance([delta_x,delta_y]),beta)
        pher.append(add)
        
    #print('pher:',pher)
    
    index = select(pher)
    with open('data_test/log.txt','a') as f:
        f.write('index chosen:'+str(index)+'\n')
        f.close()
    
    return destin[index]

def select(pher):
    #score setting
    score = []
    peak = []
    tmp = 0
    index = 0
    sum_pher = sum(pher)
    for i in pher:
        score.append(i/sum_pher)
        tmp += (i/sum_pher)
        peak.append(tmp)
    
    #print('peak:',peak)
    #process
    
    num = random.random()
    with open('data_test/log.txt','a') as f:
        f.write('pher: '+str(pher)+'\n')
        f.write('peak: '+str(peak)+'\n')
        f.write('random number: '+str(num)+'\n')
        f.close()
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
    test_table = []
    for i in seq:
        tmp_table.append([])
        test_table.append([])
        for j in seq:
            tmp_table[i].append(0)
            test_table[i].append(0)            
    #capture paths ants go through
    for ant in ant_list:
        path = ant['path']
        #analyze path
        #ex: [1,2,3,4,5]
        #print('path:',path)
        dist = evalu(path,dic)
        for i in range(len(path)):
            row = path[i]
            col = path[(i+1)%len(path)]
            #print('pre:',row)
            #print('nex:',col)
            delta_x = dic[row][0] - dic[col][0]
            delta_y = dic[row][1] - dic[col][1]
            #tmp_table[row-1][col-1] += (ant['pher']/pow(distance([delta_x,delta_y]),2))
            tmp_table[row-1][col-1] += (ant['pher']/dist)
            test_table[row-1][col-1]+= 1
            #print(tmp_table[row-1][col-1])
    #update pheromne table
    #print(tmp_table)
    
    for row in range(len(table)):
        for col in range(len(table[row])):
            if row < col:
                tmp = table[row][col]
                add = tmp_table[row][col] + tmp_table[col][row]
                table[row][col] = (1-d_rate)*tmp + add
    with open('data_test/log.txt','a') as f:
        f.write('test table:\n')
        for i in range(len(test_table)):
            for j in range(len(test_table[i])):
                f.write(str(test_table[i][j]))
                f.write('   ')
            f.write('\n')
        f.write('tmp table:\n')
        for i in range(len(tmp_table)):
            for j in range(len(tmp_table[i])):
                f.write(str(tmp_table[i][j]))
                f.write('   ')
            f.write('\n')
        f.write('table:\n')
        for i in range(len(table)):
            for j in range(len(table[i])):
                f.write(str(table[i][j]))
                f.write('   ')
            f.write('\n')
        f.close()
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
    
    best_distance = evalu(best_ant['path'],dic)
    for ant in ant_list:
        dist = evalu(ant['path'],dic)
        if  dist < best_distance:
            best_ant = ant
            best_distance = dist
    return best_ant 
            
def readfile(dic):
    #with open('eil51.txt') as f:
    with open('test.txt') as f:
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
def output_table(table):
    
        
    return 0
#initial        


#dic={a:b}, a是點的編號(type[int]),b是點的座標(type[list]) (Ex:dic={1:[0,1]})
dic = {}
readfile(dic)
alpha = 1
beta = 2
d_rate = 0.15
iter_num = input('Please enter the iteration:')
iter_num = int(iter_num)



t1 = time.time()
#Executtion

'''
#generate ant path file
for ant in ant_list:
    filename = 'data/'+str(ant['id'])+'.txt'
    with open(filename,'w') as f:
        f.truncate(0)
        f.close()

while len(ant_list[0]['path']) <len(dic):
        find_path(ant_list,len(dic),alpha,beta,table,dic)

write ant path into file
for ant in ant_list:
    filename = 'data/'+str(ant['id'])+'.txt'
    for i in range(len(ant['path'])):
        with open(filename,'a') as f:
            
            f.write(str(dic[ant['path'][i]][0]))
            f.write(' ')
            f.write(str(dic[ant['path'][i]][1]))
            f.write('\n')
            f.close()
'''

best_ant = {'path':list(range(1,len(dic)+1))}
table = gen_pher_table(len(dic))
filename = 'data_test/log.txt'
with open(filename,'w') as f:
    f.truncate(0)
    f.close()
    
for k in range(iter_num):
    '''
    with open(filename,'w') as f:
        f.truncate(0)
        f.close()
        '''
    '''
    filename = 'data/best.txt'
    with open(filename,'w') as f:
           f.truncate(0)
           f.close()
    '''
    ant_list = gen_ant(len(dic))
    
    
    find_path(ant_list,len(dic),alpha,beta,table,dic)
    best_ant = determin(ant_list,dic,best_ant)
    
    
    '''    
    #write best ant path
    filename = 'data/best.txt'
    for i in range(len(best_ant['path'])+1):
        with open(filename,'a') as f:
            
            f.write(str(dic[best_ant['path'][i%len(best_ant['path'])]][0]))
            f.write(' ')
            f.write(str(dic[best_ant['path'][i%len(best_ant['path'])]][1]))
            f.write('\n')
            f.close()
    gp.c('set terminal qt 0')
    gp.c('plot "data/best.txt" u 1:2 with linespoints linewidth 2')    
'''
    if k%100 ==0:
        print('distance:',evalu(best_ant['path'],dic))
    
    table = update_pher(ant_list,table,d_rate,dic)
    '''
    with open(filename,'a') as f:
        for i in range(len(table)):
            for j in range(len(table[i])):
                f.write(str(table[i][j]))
                f.write(' ')
            f.write('\n')
    f.close()
    '''
    
'''
    #Draw 3D pheromone graph
    filename = 'data/pher_table.txt'
    with open(filename,'w') as f:
        f.truncate(0)
        f.close()
    for row in range(len(table)):
        for col in range(len(table[row])):
            with open(filename,'a') as f:
                f.write(str(col+1))
                f.write(' ')
                f.write(str(row+1))
                f.write(' ')
                f.write(str(table[row][col]))
                f.write('\n')
                f.close()
    gp.c('set terminal qt '+str(k))
    gp.c('set xrange [1:51]')
    gp.c('set yrange [1:51]')
    gp.c('set dgrid3d 30,30')
    gp.c('set hidden3d')
    gp.c('splot "data/pher_table.txt" u 1:2:3 with lines')
    #gp.c('set output "123.png"')
'''    

    
   
   
t2 = time.time()        
print('Time: %.2f (second)(不包含I/O時間)'% (t2-t1))
#print('ant_list:',ant_list)
print('distance:',evalu(best_ant['path'],dic))  


#Calculating average and output





