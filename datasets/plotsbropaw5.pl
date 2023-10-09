reset
set terminal postscript color enhanced dashed font ",14"
set output 'paw-5-0.eps'
#set xlabel 'Positive'
#set ylabel 'Negative'
set key outside center bottom horizontal

set style line 1 lc rgb 'black' pt 7 ps 1.5
set style line 3 lc rgb 'green' pt 7 ps 1.5
set style line 4 lc rgb 'blue' pt 7 ps 1.5
set style line 5 lc rgb 'red' pt 7 ps 1.5
set style line 2 lc rgb '#D3D3D3' pt 7 ps 1.5


plot 'paw02a-600-5-0-bi-SP.txt' u 1:2 w p ls 3 title 'S',\
'paw02a-600-5-0-bi-BP.txt' u 1:2 w p ls 4 title 'B',\
'paw02a-600-5-0-bi-RP.txt' u 1:2 w p ls 5 title 'R',\
'paw02a-600-5-0-bi-OP.txt' u 1:2 w p ls 1 title 'O',\
'paw02a-600-5-0-bi-N.txt' u 1:2 w p ls 2 title 'N'
