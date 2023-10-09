reset
set terminal postscript color enhanced dashed font ",14"
set output 'clover-7-0.eps'
#set xlabel 'Positive'
#set ylabel 'Negative'
set key outside center bottom horizontal

set style line 1 lc rgb 'black' pt 7 ps 1.5
set style line 2 lc rgb '#D3D3D3' pt 7 ps 1.5


plot 'clover-7-0P.dat' u 1:2 w p ls 1 notitle,\
'clover-7-0N.dat' u 1:2 w p ls 2 notitle
