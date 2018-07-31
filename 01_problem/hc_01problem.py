import sys
import random
import time

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

def evalu(num):
    result = 0
    for i in range(len(num)):
        result += num[i]
    return result


#Main
length = int(input("Please enter the length of number:"))
iter_num = int(input("Please enter the iteration number:"))
num = init(length)
temp = []
t1 = time.time()
for i in range(iter_num):
    temp = trans(num)
    if evalu(temp) > evalu(num):
        num = temp[:]
t2 = time.time()
print("Final number:",num)
print("Final result:",evalu(num))
print('        Time: %.2f (second)'% (t2-t1))

