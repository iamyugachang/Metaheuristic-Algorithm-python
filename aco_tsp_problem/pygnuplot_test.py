import PyGnuplot as gp
import numpy as np
def readfile(dic):
    with open('eil51.txt') as f:
        r = f.read()
        read_line = r.split('\n')               
        for i in range(len(read_line)):         
            read_element = read_line[i].split() 
            dic[int(read_element[0])] = [int(read_element[1])]
            dic[int(read_element[0])].append(int(read_element[2]))
        f.close()
dic = {}
readfile(dic)
with open('eil51_optimal.txt') as f:
        a = []
        r = f.read()
        read_line = r.split()               
        for i in range(len(read_line)):
            a.append(int(read_line.pop(0)))
        f.close()
#gp.s([X,Y,Z])
#gp.c('replot "tmp.dat" u 1:3')
#gp.p('myfigure.jpg')
filename = 'data/optimal.txt'
with open(filename,'w') as f:
    f.truncate(0)
    f.close()
for i in range(len(a)+1):
    with open(filename,'a') as f:
        
           
        f.write(str(dic[a[i%len(a)]][0]))
        f.write(' ')
        f.write(str(dic[a[i%len(a)]][1]))
        f.write('\n')
        f.close()
gp.c('plot "data/optimal.txt" u 1:2 with linespoints linewidth 2')
