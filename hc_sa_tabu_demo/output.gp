#graph for hc
set title "Performance"
set xlabel "Iteration"
set ylabel "Distance"
set terminal png font " Times_New_Roman,12 "
set output "output_hc.png"
set key left 

plot 'output_hc.txt' using 1:2 with linespoints linewidth 1 title 'Hill Climbing'

#graph for sa
reset
set title "Performance"
set xlabel "Iteration"
set ylabel "Distance"
set terminal png font " Times_New_Roman,12 "
set output "output_sa.png"
set key left 

plot 'output_sa.txt' using 1:2 with linespoints linewidth 1 title 'Simulated annealing'

#graph for tabu
reset
set title "Performance"
set xlabel "Iteration"
set ylabel "Distance"
set terminal png font " Times_New_Roman,12 "
set output "output_tabu.png"
set key left 

plot 'output_tabu.txt' using 1:2 with linespoints linewidth 1 title 'Tabu Search'

#graph for all
reset
set title "Performance"
set xlabel "Iteration"
set ylabel "Distance"
set terminal png font " Times_New_Roman,12 "
set output "output_all.png"
set key left 

plot \
'output_tabu.txt' using 1:2 with linespoints linewidth 1 title 'Tabu Search',\
'output_hc.txt' using 1:2 with linespoints linewidth 1 title 'Hill Climbing',\
'output_sa.txt' using 1:2 with linespoints linewidth 1 title 'Simulated annealing'
