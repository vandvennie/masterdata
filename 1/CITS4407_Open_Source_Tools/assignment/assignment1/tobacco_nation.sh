#!/bin/bash
#This program is for tracking World-wide Tobacco Use
#This program is Assignment 1 for course 4407, submitted by student 24516605 at the UWA
#Usage: tobacco_nation <csv data file>  < year | country code >  < Male | Female >

#Check if the number of arguments is correct 
if  [[ $# -ne 3 ]]
then
	echo "Error: The number of arguments is incorrect" > /dev/stderr
    echo "Usage: tobacco_nation <csv data file>  < year | country code >  < Male | Female >"
    exit 1

#Check if the first argument is exist and has content
elif ! [[ -s "$1" ]]
then
    echo "Error: The named input file "$1" does not exist or has zero length" > /dev/stderr
    exit 1

#Check if the second argument is correct
elif ! [[ "$2" = [0-9][0-9][0-9][0-9] ]] && ! [[ "$2" = [A-Z][A-Z][A-Z] ]]
then
    echo "Error: The second argument must be a number of YEAR or three uppercase letters of a COUNTRY" > /dev/stderr
    exit 1

#Check if the third argument is correct
else 
    gender=$(echo $3 | tr '[:upper:]' '[:lower:]') 
    case "$gender" in
        "male")
            gender="Male"
            ;;
        "female")
            gender="Female"
            ;;
        *)
            echo "Error: The third argument must be Male or Female" > /dev/stderr
            exit 1
            ;;
    esac
    
fi


#find the maximum percentage in the table
#if the second argument is year

if [[ "$2" = [0-9][0-9][0-9][0-9] ]]
then
    year="$2"
    code=$(grep "$gender" "$1" | grep "$year" | sort -t ',' -k 7 -n -r | head -n 1 | cut -d ',' -f 3)
    country=$(grep "$gender" "$1" | grep "$year" | sort -t ',' -k 7 -n -r | head -n 1 | cut -d ',' -f 4)
    PC=$(grep "$gender" "$1" | grep "$year" |  sort -t ',' -k 7 -n -r | head -n 1 | cut -d ',' -f 7)
    
    #If the year is in the past, use "was" to describe the rate; if the year is in the future, use "is predicted to be".
    if [[ -n "$PC" ]] && [[ "$year" -lt 2024 ]]
    then
        echo "The global maximum percentage of "$gender" tobacco users in "$year" was in "$country" ("$code") at "$PC""
    elif [[ -n "$PC" ]] && [[ "$year" -ge 2024 ]]
    then
        echo "The global maximum percentage of "$gender" tobacco users in "$year" is predicted to be in "$country" ("$code") at "$PC""
    #If everything is correct but no result in the file.
    else
        echo "There is no result from those arguments in the file "$1""
    fi

#if the second argument is country code
else
    code="$2"
    country=$(grep "$gender" "$1" | grep "$code" | sort -t ',' -k 7 -n -r | head -n 1 | cut -d ',' -f 4)
    year=$(grep "$gender" "$1" | grep "$code" | sort -t ',' -k 7 -n -r | head -n 1 | cut -d ',' -f 5)
    PC=$(grep "$gender" "$1" | grep "$code" |  sort -t ',' -k 7 -n -r | head -n 1 | cut -d ',' -f 7)

    #If the year is in the past, use "was" to describe the rate; if the year is in the future, use "is predicted to be".
    if [[ -n "$PC" ]] && [[ "$year" -lt 2024 ]]
    then
        echo "The global maximum percentage of tobacco users for "$country" ("$code") was "$PC" in "$year""
    elif [[ -n "$PC" ]] && [[ "$year" -ge 2024 ]]
    then
        echo "The global maximum percentage of tobacco users for "$country" ("$code") is "$PC" in "$year""
    #If everything is correct but no result in the file.
    else
        echo "There is no result from those arguments in the file "$1""
    fi
    
    
fi

