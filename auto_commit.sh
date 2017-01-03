#!/usr/bin/env bash

git status >> /dev/null 2>&1
git add . >> /dev/null 2>&1
s_1=`date +%F`
s_2=`date +%T`
git commit -m "time is: $s_1 $s_2" >> /dev/null 2>&1
git push -u origin master >> /dev/null 2>&1
