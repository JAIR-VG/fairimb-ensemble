#!/bin/sh

myfile=$1

awk '$NF ~ "positive" {$NF=0; print $0}' $myfile > positive.dat
awk '$NF ~ "negative" {$NF=1; print $0}' $myfile > negative.dat

cat positive.dat negative.dat > bothclasses.prn


