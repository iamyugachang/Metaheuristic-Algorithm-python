# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 17:20:53 2018

@author: Yuga
"""

import random
import time
from itertools import combinations, permutations

def readfile(groupnum):
    data = []
    dimen = 0
    with open('iris.data','r') as f:
        r = f.read()
        readline = r.split('\n')
        for line in readline:
            if len(line) > 0:
                elements = line.split(',')
                new = []
                for e in elements:
                    if checknum(e):
                        new.append(checknum(e))
                        
                    else:
                        new.append(e)
                if dimen == 0:
                    for i in new:
                        if checknum(i):
                            dimen+=1
                new.append(-1)
                data.append(new)
        f.close()
    
    return data,dimen

def init(groupnum,data,dimen):
    #random choose k centers for classification
    #center = {0:[],1:[],2:[]}
    center = {}
    tmp = []
    count = 0
    while len(center) < groupnum:
        ran = random.randint(0,len(data)-1)
        if ran not in tmp:
            center[count] = data[ran][:dimen]
            count+=1
            tmp.append(ran)
    
    #print(center)
    #classify these data based on center list
    data = classify(data,center,dimen)
    return data,center

def checknum(self):
    try:
        val = float(self)
        return val
    except ValueError:
        #print("That's not a number!")
        return False
def findcenter(data,groupnum,dimen):
    #center = {0:[0,0,0,0,num],1:[0,0,0,0,num],2:[0,0,0,0,num]}
    center = {} 
    newcenter = {}
    for i in range(groupnum):
        center[i] = []
        newcenter[i] = []
        for j in range(dimen+1):
            center[i].append(0)
    
    for d in data:
        index = d[-1]
        for i in range(dimen): 
            center[index][i]+=d[i]
        center[index][-1]+=1
    for i in center:
        li = center[i][:dimen]
        amount = center[i][-1]
        for element in li:
            newcenter[i].append(element/amount)
            
    return newcenter

def classify(data,center,dimen):
    for d in data: #one of data
        distance = []
        for i in range(len(center)):
            distance.append(0)
        for num in range(dimen):
            for c in center:
                middle = center[c]
                distance[c]+=(d[num]-middle[num])**2
        mini = min(distance)
        index = distance.index(mini)
        d[-1] = index
    return data
    
def sse(data,center,dimen):
    distance = []
    for i in range(len(center)):
        distance.append(0)
            
    for d in data:
        cen = center[d[-1]]
        for k in range(len(cen)):
            distance[d[-1]] += (d[k]-cen[k])**2
    s = sum(distance)
    return s            
    
def accuracy(data,groupnum):
    #initial permutation list(Ex:[(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)] )
    permu_list = list(permutations([x for x in range(groupnum)], groupnum))  
    
    #initial name list
    name_list = []
    for d in data:
        if d[-2] not in name_list:
            name_list.append(d[-2])        
    result_list = {}
    ac_list = {}
    
    #check        
    for permu in permu_list:  
        #initial correct list
        correct_list = []
        total = []
        result = []
        c = 0
        t = 0
        for i in range(groupnum):    
            correct_list.append(0)
            total.append(0)
            result.append(0)
            
        #start distinguish    
        for d in data:
            classi = d[-1]
            if name_list[permu.index(classi)] == d[-2]:
                correct_list[permu.index(classi)]+=1
                c+=1
            total[permu.index(classi)]+=1
            t+=1        
        #calculate result
        for i in range(groupnum):
            result[i] = correct_list[i]/total[i]                    
        #store
        result_list[permu] = result
        ac_list[permu] = round((c/t)*100,2)    
        #print(correct_list)
    temp = 0   
        
    for permu in result_list:
        if sum(result_list[permu]) >= temp:
            temp = sum(result_list[permu])
            best_permu = permu  
    '''        
    #result
    print('accuracy rate for each classification:\n')
    for i in range(groupnum):
        print(str(name_list[best_permu[i]])+' : '+str(round(result_list[best_permu][best_permu[i]]*100,2))+'%'+'\n')
    print('total accuracy:',ac_list[best_permu],'%')
    '''
    return result_list,best_permu,ac_list[best_permu]
    
#initial
groupnum = 3
iteration = 50
data,dimen = readfile(groupnum)
data,center = init(groupnum,data,dimen)
aver_range = 30
ssum = 0
asum = 0
'''
#execute
for i in range(iteration):
    center = findcenter(data,groupnum,dimen)
    data = classify(data,center,dimen)
    
s = sse(data,center,dimen)
print('sse',s)
r,p = accuracy(data,groupnum)
'''
for _ in range(aver_range):
    data,dimen = readfile(groupnum)
    data,center = init(groupnum,data,dimen)
    
    for i in range(iteration):
        center = findcenter(data,groupnum,dimen)
        data = classify(data,center,dimen)
    
    s = sse(data,center,dimen)
    ssum+=s
    #print('sse',s)
    r,p,a = accuracy(data,groupnum)
    asum+=a
    #psum+=p
print('average sse:',ssum/aver_range)
print('average accuracy:',asum/aver_range)
