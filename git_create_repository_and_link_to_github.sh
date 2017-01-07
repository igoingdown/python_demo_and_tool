#!/usr/bin/env bash

# create a local git repository and link it to the github repository.
# to link a local git repository to the github, we need a github repository!

# give the online github repository whole path as the first arg!
# like "git@github.com:igoingdown/python_demo_and_tool.git"

git init
git config --global user.name "igoingdown"
git config --global user.email "fycjmingxing@126.com"
if [ $1 == "" ]; then
    echo -e "\n\nwe need a github repository as the first arg!\n\n"
    exit 1
else
    git remote add origin "$1"
fi
