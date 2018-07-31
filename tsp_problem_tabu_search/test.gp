set title "Performance"
set xlabel "Iteration"
set ylabel "Score"
set terminal png font " Times_New_Roman,12 "
set output "test.png"

set key left 

plot 'test.txt' using 1:2 with linespoints linewidth 2 title 'test algo'
