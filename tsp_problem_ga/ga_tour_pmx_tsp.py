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

def init(num,chromo_num):
    chromo_data = {'chromo':[],'distance':[]}
    
    for i in range(chromo_num):
        seq = []
        list_1_to_num = list(range(1,num+1))
        while len(list_1_to_num) > 0:
            index = random.randint(0,len(list_1_to_num)-1)
            seq.append(list_1_to_num.pop(index))
        chromo_data['chromo'].append(seq)
    return chromo_data

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
    new_data = {'chromo':[],'distance':[]}
    new_data['chromo'] = chromo_data['chromo'][:]
    
    #calculate distance of each chromosome
    for i in range(len(chromo_data['chromo'])):
        new_data['distance'].append(evalu(chromo_data['chromo'][i],dic))
    return new_data
def select(chromo_data,player):
    new_data = {'chromo':[],'distance':[]}
    while len(new_data['chromo']) < len(chromo_data['chromo']):
        tmp = []
        check = []
        ran_list = []
        while len(tmp) < player:
            ran = random.randint(0,len(chromo_data['chromo'])-1)
            if ran not in ran_list:
                check = chromo_data['chromo'][ran]
                tmp.append(check)
            
                
        best = tmp[0]
        for i in tmp:
            if evalu(i,dic) < evalu(best,dic):
                best = i
        new_data['chromo'].append(best)
                
    
    return new_data

def crossover(chromo_data,c_rate):
    new_chromo = {'chromo':[],'distance':[]}
    while 1:
        test1 = chromo_data['chromo'].pop(random.randint(0,len(chromo_data['chromo'])-1))
        test2 = chromo_data['chromo'].pop(random.randint(0,len(chromo_data['chromo'])-1))
        if random.random() > c_rate:
            new_chromo['chromo'].append(test1)
            new_chromo['chromo'].append(test2)
        else:
            #print('chosen list:',test1,test2)
            index1 = random.randint(0,len(test1)-1)
            index2 = random.randint(0,len(test2)-1)
            new2 = test1[index1:index2+1]
            new1 = test2[index1:index2+1]
            tmp1 = [x for x in test1 if x not in new2]
            tmp2 = [x for x in test2 if x not in new1]
            index1 = min(index1,index2)
            index2 = max(index1,index2)
            #print('break:',index1,index2)
            #find order of chromo
            for i in range(len(tmp1)):
                alter = tmp1[i]
                while 1:
                    if alter in new1:
                        alter = new2[new1.index(alter)]
                    else:
                        tmp1[i] = alter
                        break
            for i in range(len(tmp2)):
                alter = tmp2[i]
                while 1:
                    if alter in new2:
                        alter = new1[new2.index(alter)]
                    else:
                        tmp2[i] = alter
                        break        
            
            

            #paste back lookup to test
            new1 = tmp1[0:index1]+new1+tmp1[index1:]
            new2 = tmp2[0:index1]+new2+tmp2[index1:]
            new_chromo['chromo'].append(new1)
            new_chromo['chromo'].append(new2)
        if len(chromo_data['chromo']) < 2:
            if len(chromo_data['chromo']) == 1:
                new_chromo['chromo'].append(chromo_data['chromo'].pop())  
            break
    return new_chromo

def mutation(chromo_data,m_rate):
    new_data = {'chromo':[],'distance':[]}
    new_data['chromo'] = chromo_data['chromo'][:]
        
    
    if random.random() < m_rate:
        index = random.randint(0,len(new_data['chromo'])-1)
        tmp = trans(new_data['chromo'].pop(index))
        new_data['chromo'].append(tmp)
 
    return new_data
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
chromo_num = 100
iter_num = input('Please enter the iteration:')
iter_num = int(iter_num)
player = 25


t1 = time.time()
#Execute

chromo_data = init(len(dic),chromo_num)
chromo_data = fitness(chromo_data,dic)
for i in range(1,iter_num+1):  
    #print('iter',i)
    chromo_data = select(chromo_data,player)
    chromo_data = fitness(chromo_data,dic)
    #print('after select:',chromo_data['distance'])
    chromo_data = crossover(chromo_data,0.9)
    chromo_data = fitness(chromo_data,dic)
    #print('after crosso:',chromo_data['distance'])
    chromo_data = mutation(chromo_data,0.9)
    chromo_data = fitness(chromo_data,dic)
    #print('after mutati:',chromo_data['distance'])
    #print(get_stddev(chromo_data['distance']))
    #print(chromo_data['distance'])
    #result[i] += evalu(seq,dic)
    #print(' ')
    
   
   
t2 = time.time()        
print('Time: %.2f (second)(不包含I/O時間)'% (t2-t1))
print(chromo_data['distance'])       


#Calculating average and output





