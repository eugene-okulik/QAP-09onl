#!/bin/bash

echo -n "Do you want to install the Python?(Y/N): "
read answer
if [[ "${answer^^}" == "Y" ]]
then
echo "You have chose the Python install."
elif [[ "${answer^^}" == "N" ]]
then
echo "We’ll install the Python anyway."
else
echo "Your answer is wrong. You had to choose an answer: Y or N."
fi




