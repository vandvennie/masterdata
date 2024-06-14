#!/usr/bin/bash

if [[ $# -ne 1 ]]
then

	echo "Please input correct arguments." >>/dev/stderr
	exit 1
fi




text=$1

num=$(wc -l $1)

if [[ $num > 1 ]]

then

	pr=$(head -n 1 $text)

	text=$(tail -n +3 > text.txt)

	num=$(($num-2))

	echo " The nuber of $num line is $pr "

fi
