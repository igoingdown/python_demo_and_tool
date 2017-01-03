#!/usr/bin/env bash

git status >> ../git.out 2>&1
git add . >> ../git.out 2>&1
s_1=`date +%F`
s_2=`date +%T`
git commit -m "time is: $s_1 $s_2" >> ../git.out 2>&1
git push -u origin master >> ../git.out 2>&1