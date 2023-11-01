#!/bin/bash


dtst=( 03subcl5-600-5-0-bi 03subcl5-600-5-30-bi 03subcl5-600-5-50-bi 03subcl5-600-5-60-bi 03subcl5-600-5-70-bi 04clover5z-600-5-0-bi 04clover5z-600-5-30-bi 04clover5z-600-5-50-bi 04clover5z-600-5-60-bi 04clover5z-600-5-70-bi paw02a-600-5-0-bi paw02a-600-5-30-bi paw02a-600-5-50-bi paw02a-600-5-60-bi paw02a-600-5-70-bi 03subcl5-800-7-0-bi 03subcl5-800-7-30-bi 03subcl5-800-7-50-bi 03subcl5-800-7-60-bi 03subcl5-800-7-70-bi 04clover5z-800-7-0-bi 04clover5z-800-7-30-bi 04clover5z-800-7-50-bi 04clover5z-800-7-60-bi 04clover5z-800-7-70-bi paw02a-800-7-0-bi paw02a-800-7-30-bi paw02a-800-7-50-bi paw02a-800-7-60-bi paw02a-800-7-70-bi )


for i in "${dtst[@]}"; do

   ftra=$i"/"$i".dat"

   echo "Procesando $ftra"

   ./keeltoprn.sh $ftra
done

