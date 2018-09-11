import sys
import time
import math
import random
#import PyGnuplot as gp
def init(num,xrange,yrange,vrange):
    #format: par_list = [part1, part2...]
    #format: part = {'id':0,'posi':[0,0],'velo':[0,0],'local_best':[]}
    part_list = []
    for i in range(num):
        x = random.uniform(xrange[0],xrange[1])
        y = random.uniform(yrange[0],yrange[1])
        vx = random.uniform(vrange[0],vrange[1])
        vy = random.uniform(vrange[0],vrange[1])
        part = {'id':i,'posi':[x,y],'velo':[vx,vy],'local_best':[x,y]}
        part_list.append(part)
    return part_list

def ackley(position):
    #position = [x,y]
    firstSum = 0.0
    secondSum = 0.0
    
    for c in position:
        #if len(str(c)) > 5:
        #    c = round(c,5)
        
        firstSum += c**2.0
        secondSum += math.cos(2.0*math.pi*c)
	
    n = float(len(position))
    return round(-20.0*math.exp(-0.2*math.sqrt(firstSum/n)) - math.exp(secondSum/n) + 20 + math.e,8)
    

def evalu(part_list,group_best):
    #check best position of each particle and group
    '''
    with open('log.txt','a') as f:
        f.write('current part_list: '+str(part_list))
        f.write('\n')
        f.write('\n')
        f.close()
    '''
    for part in part_list:
        ack = ackley(part['posi'])
        
        
        if ack < ackley(part['local_best']):
            part['local_best'] = part['posi']
            '''
            with open('log.txt','a') as f:
                f.write('local best found: '+str(part['local_best'])+' at '+str(part['id'])+'\n')
                f.close()
            '''
        if ack < ackley(group_best):
            group_best = part['posi']
            '''
            with open('log.txt','a') as f:
                f.write('group best found: '+str(group_best)+' at '+str(part['id'])+'\n')
                f.close()
            '''
        
                
    return (part_list,group_best)

def trans(part_list,crange,group_best,xrange,yrange,vrange,wrange,i,iteration):
    #update each property for particles
   
    w = wrange[0] - ((wrange[0]-wrange[1])/iteration)*i
    c_1 = crange[1] + ((crange[0]-crange[1])/iteration)*i
    c_2 = crange[0] + ((crange[1]-crange[0])/iteration)*i
    #print('w:',w,'c1:',c_1,'c2:',c_2)
    for part in part_list:
        r_1 = random.random()
        r_2 = random.random()
        '''
        with open('log.txt','a') as f:
            f.write('origin part:'+str(part)+'\n')
            f.close()
        '''
        
        vectori = [part['local_best'][0]-part['posi'][0],part['local_best'][1]-part['posi'][1]]
        vectorg = [group_best[0]-part['posi'][0],group_best[1]-part['posi'][1]]
        
        sumx = w*part['velo'][0] + c_1*r_1*vectori[0] + c_2*r_2*vectorg[0]
        sumy = w*part['velo'][1] + c_1*r_1*vectori[1] + c_2*r_2*vectorg[1]
        if sumx < vrange[0]:
            sumx = vrange[0]
        if sumx > vrange[1]:
            sumx = vrange[1]
        if sumy < vrange[0]:
            sumy = vrange[0]
        if sumy > vrange[1]:
            sumy = vrange[1]
        part['velo'] = [sumx,sumy]
        
        posix = part['posi'][0] + sumx
        posiy = part['posi'][1] + sumy
        if posix < xrange[0]:
            posix = xrange[0]
        if posix > xrange[1]:
            posix = xrange[1]
        if posiy < yrange[0]:
            posiy = yrange[0]
        if posiy > yrange[1]:
            posiy = yrange[1]
        
        part['posi'] = [posix,posiy]
        '''
        with open('log.txt','a') as f:
            
            f.write('r1: '+str(r_1)+' r2: '+str(r_2)+'\n')
            f.write('vectori: '+str(vectori)+', vectorg: '+str(vectorg)+'\n')
            f.write('part[velo]: '+str(part['velo'])+'\n')
            f.write('part[posi]: '+str(part['posi'])+'\n')
            f.close()
        '''    
    return part_list

def determin():
    #determin if the iteration is over 
    return 0

def output3d(part_list):
    with open('3d.txt','a') as f:
        for part in part_list:
            f.write(str(part['posi'][0])+' '+str(part['posi'][1])+' '+str(ackley(part['posi']))+'\n')
        f.close()
    
#initial
part_num = 100
xrange = [-100,100]
yrange = [-100,100]
vrange = [-4,4]
wrange = [0.9,0.4]
part_list = init(part_num,xrange,yrange,vrange)
iteration = 500
c_1 = 2
c_2 = 2
crange = [1,2.5]
group_best = part_list[random.randint(0,part_num-1)]['local_best']

'''
filename = 'log.txt'
with open(filename,'w') as f:
    f.truncate(0)
    f.close()
'''
with open('3d.txt','w') as f:
        f.truncate(0)
        f.close()
    
#execute
for i in range(iteration):
    
    (part_list,group_best) = evalu(part_list,group_best)
    #print(part_list)
    #print(group_best)
    part_list = trans(part_list,crange,group_best,xrange,yrange,vrange,wrange,i,iteration)
    output3d(part_list)
    '''
    gp.c('set dgrid3d 2,2')
    gp.c('set hidden3d')
    gp.c('set xrange [-100,100]')
    gp.c('set yrange [-100,100]')
    gp.c('splot "3d.txt" u 1:2:3 with linespoints pt 6')
    '''    
#output3d(part_list)
'''
gp.c('set dgrid3d 30,30')
gp.c('set hidden3d')
gp.c('set xrange [-100,100]')
gp.c('set yrange [-100,100]')
gp.c('set ticslevel 0')
gp.c('splot "3d.txt" u 1:2:3 with linespoints pt 1')
'''
print(group_best)
print(ackley(group_best))
    
