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
num = []
t1 = time.time()
for i in range(length):
    temp1 = num[:]
    temp2 = num[:]
    temp1.append(0)
    temp2.append(1)
    if evalu(temp1) > evalu(temp2):
        num = temp1[:]
    else:
        num = temp2[:]

t2 = time.time()

print("Final number:",num)
print("Final result:",evalu(num))
print('        Time: %.5f (second)'% (t2-t1))
        

