#!/bin/bash

ftra=$1

echo "Entrada = $ftra"

#numero de filas del archivo
rws=$(wc -l $ftra | awk '{print $1}')

Echo "filas archivo = $rws"

#Numero de fila donde aparece la palabra
rwsd=$(grep -ion "@data" $ftra | sed s/"\:@data"//g)

#Obtiene el total de lineas que ocupa la salida del clasificador en el fichero
let sbrws=$rws-$rwsd

Echo "total lineas = $sbrws"
		
#extrae todo lo que aparece a partir de @data
cat $ftra | grep -A$sbrws "@data" | sed -e '1d' > mytemporal.dat

nfile=`echo $ftra | sed s/"\.dat"//g`

echo "Nuevo archivo $nfile"

#sustituye comas por espacios
sed 's/,/ /g' mytemporal.dat>mytemporal.prn

./changelabel.sh mytemporal.prn

mv bothclasses.prn $nfile.prn

rm mytemporal*


echo " + + + + + + + + + + + + + + + + + + + + + + + + + +  "
echo " + +  Nuevo $nfile.prn + + "
echo " + + + + + + + + + + + + + + + + + + + + + + + + + +  "
