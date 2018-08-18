import PyGnuplot as gp
gp.c('set dgrid3d 30,30')
gp.c('set hidden3d')
gp.c('splot "3Dtest.txt" u 1:2:3 with lines')
