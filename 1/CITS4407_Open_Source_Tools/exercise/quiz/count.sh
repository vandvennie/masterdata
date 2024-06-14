#!/usr/bin/env bash
set -x
if [[ $# -ne 1 ]]
then
    echo "Usage $0 <filename> <top N> "
    exit 1
fi

if [[ ! -s $1 ]]
then
    echo "File $1 does not exist or has zero length"
    exit 1
fi

name=$(basename .txt $1)
ontfile="${name}_count.txt"

# Perform word count and display the most frequent words
cat "$1" | tr -cs 'A-Za-z' '\n' | sort | uniq -c | sort -nr | head -n 10

tr -cs '[A-Za-z]' '\012' < $1 | sort | uniq -c | sort -k 1nr | head -n $2 > $outfile
