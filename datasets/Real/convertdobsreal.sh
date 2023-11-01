#!/bin/bash

folds=$1

fichero=$2

#dtst=( ecoli-0_vs_1 glass0 glass1 habermanImb iris0 pimaImb vehicle1 vehicle2 vehicle3 wisconsinImb yeast1 )

dtst=( ecoli-0-1-3-7_vs_2-6 poker-8_vs_6 poker-8-9_vs_5 poker-8-9_vs_6 shuttle-2_vs_5 winequality-red-3_vs_5 winequality-red-8_vs_6 winequality-red-8_vs_6-7 winequality-white-3-9_vs_5 winequality-white-9_vs_4 yeast-1-2-8-9_vs_7 yeast4 yeast6 )


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

