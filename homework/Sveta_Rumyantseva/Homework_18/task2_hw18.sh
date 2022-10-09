#!/bin/bash

echo -n "Enter any word: "
read word
while [ "${word}" != . ]
do
length=${#word}
echo "${length}"
if [[ -z "${word}" ]]
then
echo "The string is empty."
elif [[ "${length}" -le 5 ]]
then
echo "Ok"
else
echo "The ${word} is too long."
fi 
echo -n "Enter any word: " 
read word
done
echo "The end."
