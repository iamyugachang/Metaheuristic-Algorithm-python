import sys
import random


#function definition
def init(length):
    num = []
    for i in range(length):
        num.append(random.randint(0,1))
    return num

def trans(num):
    temp = num[:]
    rand_index = random.randrange(len(num))
    temp[rand_index] = (temp[rand_index]+1)%2
    return temp    

def evalu(num,profit,weight,capacity):
    result = 0
    w = 0
    for i in range(len(num)):
        
        w += weight[i]*num[i]
        if w > capacity:
            return 0
        result += profit[i]*num[i]
    return result

def readfile(profit,weight):
    with open('p08_p.txt') as f:
        r = f.read()
        read_data = r.split()
        for i in range(len(read_data)):
            profit.append(int(read_data.pop()))
        profit.reverse()
        f.close()
    with open('p08_w.txt') as f:
        r = f.read()
        read_data = r.split()
        for i in range(len(read_data)):
            weight.append(int(read_data.pop()))
        weight.reverse()
        f.close()
#Main
for count in range(1):
    print('Count',count)
    iter_num = 100000
    profit = []
    weight = []
    optimal = []
    w = 0
    readfile(profit,weight)
    length = len(profit)
    capacity = 6404180
    num = init(length)
    store = []
    temp = []

    for i in range(iter_num):
        temp = trans(num)
        if evalu(temp,profit,weight,capacity) > evalu(num,profit,weight,capacity):
            print('iter',i,'發生取代')
            print('原num:',num)
            print('原profit:',evalu(num,profit,weight,capacity))
            num = temp[:]
            print('後num:',num)
            print('後profit:',evalu(num,profit,weight,capacity))
    print()
    print('My one max:',num)
    print('My profit:',evalu(num,profit,weight,capacity))
    for i in range(len(num)):
        w += weight[i]*num[i]
    print('My weight:',w,'/',capacity)



    with open('p08_s.txt') as f:
        r = f.read()
        read_data = r.split()
        for i in range(len(read_data)):
            optimal.append(int(read_data.pop()))
        optimal.reverse()
        f.close()
    
    print('Optimal profit:',evalu(optimal,profit,weight,capacity))
    print('Match rate',evalu(num,profit,weight,capacity)*100/evalu(optimal,profit,weight,capacity),'%')
