#!/bin/bash
printf "Начало работы скрипта"
while [ "$ANSWR" != "." ]
do
printf "Введите слово: "
read ANSWR
if [ "${#ANSWR}" -le "5" ]
then
echo "Ok"
else
echo "Слово слишком длинное"
fi
done
echo "Ok"