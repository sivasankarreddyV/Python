#!/usr/bin/bash
#to print max of three colors by using if else conditions
read -p "enter the first number:" num1
read -p "enter the second number:" num2
read -p "enter the third number :" num3
normal="\e[0m"
red="\e[31m"
green="\e[32"
yellow="\e[33m"

if [ $num1 -gt $num2 -a $num1 -gt $num3 ];
then
	echo -e "${red} the first number ${num1} is maximum ${normal}"
elif [ $num2 -gt $num3 ];
then
        echo -e "${green} the second number ${num2} is maximum ${normal}"
else
	echo -e "${yellow} the third number ${num3} is maximum ${normal}"
fi
