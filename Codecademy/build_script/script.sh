#!/bin/zsh

echo "Hello! What is your name?"
read name
echo "Nice to meet you $name"

firstline=$(head -1 ./source/changelog.md)

echo $firstline

read -A splitfirstline <<< $firstline

version=${splitfirstline[2]}

echo $version

echo "Would you like to continue: Yes [1] or No [0]"

read versioncontinue

if [ $versioncontinue -eq 1 ]
then
    echo "OK"
    for file in ./source/*
    do
        if [ "$file" = "./source/secretinfo.md" ]
        then
            echo "$file was not copied"
        else
            echo "$file was copied"
            cp $file ./build/.
        fi
    done

    cd ./build
    echo "Build version $version contains:"
    ls 
    cd ../

else
    echo "Please come back when you are ready"
fi 

