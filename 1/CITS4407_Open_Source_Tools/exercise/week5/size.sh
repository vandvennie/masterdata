#!/usr/bin/env bash
if [[ $# -ne 1 ]]
then
    echo "Usage $0 <directory>" > /dev/null
    exit 1
fi

count=$(ls $1 | wc -l)
size=$(du -h | tail -1)
echo Number of files $count Total size of files in $1 is $size
