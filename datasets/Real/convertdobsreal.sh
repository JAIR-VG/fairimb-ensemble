#!/bin/bash

folds=$1
fichero=$2

dtst=( ecoli-0_vs_1 glass0 glass1 habermanImb iris0 pimaImb vehicle1 vehicle2 vehicle3 wisconsinImb yeast1 )


for i in "${dtst[@]}"; do
    for (( j = 1; j <= $folds; j++))
    do
        ftra=$fichero"/"$i"/"$i"-"$folds"dobscv-"$j"tra.dat"

	echo "Procesando $ftra"

	./keeltoprn.sh $ftra

        ftst=$fichero"/"$i"/"$i"-"$folds"dobscv-"$j"tst.dat"
	echo "Procesando $ftst"
	./keeltoprn.sh $ftst
    done
done

