#!/bin/bash
echo "请输入一个星期几（英文）："
read day

case $day in
    Mon | Fri ) echo "${day}day";; 
    *) echo "Happy Weekends";;
esac

