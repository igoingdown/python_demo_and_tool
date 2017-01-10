#!/usr/bin/env bash

working_dir=`pwd`
echo -e "\n\n\n\ntrying to commit modification in $working_dir\n"

git status
git add .
s_1=`date +%F`
s_2=`date +%T`
remoteOrigin=`git remote`
git commit -m "commit time: $s_1 $s_2"
git push -u "$remoteOrigin" master

echo -e "\nmodification in $working_dir commit over!\n\n\n\n"
