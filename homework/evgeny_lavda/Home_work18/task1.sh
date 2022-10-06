#!/bin/bash
printf 'Вы хотите установить python 1) Да 2) Нет:   '
read ANSWR
case $ANSWR in
        Да)
        echo "Вы выбрали установить python"
        ;;
        Нет)
        echo "Все-равно установим!"
        ;;
esac