#! /bin/bash
#Задание №1
#Напишите скрипт который будет спрашивать “Хотите установить Python?” и варианты ответа “1) Да 2) Нет”
#Если Да, то выдать сообщение “Вы выбрали установить python”
#Если Нет, то выдать сообщение “Все-равно установим”

echo 'Хотите установить Python?'
echo
select answer in 'Да' 'Нет'
do
if [[ $answer == 'Да' ]]
then
echo "Вы выбрали установить Python"
else
echo "Все-равно установим"
fi
break
done