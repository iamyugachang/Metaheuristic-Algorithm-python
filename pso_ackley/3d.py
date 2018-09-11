import sys
import time
import math
import random
import PyGnuplot as gp
'''
gp.c('set dgrid3d 30,30')
gp.c('set hidden3d')
gp.c('set xrange [-100:100]')
gp.c('set yrange [-100:100]')
gp.c('set xzeroaxis')
gp.c('set yzeroaxis')
gp.c('set ticslevel 0')
gp.c('splot "123.txt" u 1:2:3 with linespoints pt 1')
'''
gp.c('set dgrid3d 30,30')
gp.c('set xrange [-10:10]')
gp.c('set yrange [-10:10]')
gp.c('set ticslevel 0')
gp.c('splot "123.txt" u 1:2:3 with linespoints pt 1')
