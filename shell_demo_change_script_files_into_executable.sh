#!/usr/bin/env bash

for file in `ls *py`
do
    chmod u+x $file
done
