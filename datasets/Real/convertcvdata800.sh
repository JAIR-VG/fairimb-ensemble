#!/bin/bash

folds=$1

dtst=( 03subcl5-800-7-0-bi 03subcl5-800-7-30-bi 03subcl5-800-7-50-bi 03subcl5-800-7-60-bi 03subcl5-800-7-70-bi 04clover5z-800-7-0-bi 04clover5z-800-7-30-bi 04clover5z-800-7-50-bi 04clover5z-800-7-60-bi 04clover5z-800-7-70-bi paw02a-800-7-0-bi paw02a-800-7-30-bi paw02a-800-7-50-bi paw02a-800-7-60-bi paw02a-800-7-70-bi )


for i in "${dtst[@]}"; do
    for (( j = 1; j <= $folds; j++))
    do
        ftra=$i"/"$i"-"$folds"-"$j"tra.dat"

	echo "Procesando $ftra"

	./keeltoprn.sh $ftra

        ftst=$i"/"$i"-"$folds"-"$j"tst.dat"
	echo "Procesando $ftst"
	./keeltoprn.sh $ftst
    done
done

