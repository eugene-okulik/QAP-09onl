#! /bin/bash

#Задание №2
#Напишите скрипт, который будет запрашивать слова на вход и затем если слово не длиннее 5 символов, то отвечает “ok”,
# а если длиннее, то отвечает “слово слишком длинное”.
#Реализуйте этот сценарий так, что бы он продолжал запрашивать слова и заканчивался, если передать ему “.” (точку)
#Подсказка: используйте while

#! /bin/bash

echo "Enter a dot '.' to stop the programm"
echo "Enter a word length less 5: "
read WORD
while [[ $WORD != '.' ]]
do
if [[ ${#WORD} -le 5 ]]
then
echo "OK"
else
echo "Length of your word is less than 5"
fi
read WORD
done
exit 0