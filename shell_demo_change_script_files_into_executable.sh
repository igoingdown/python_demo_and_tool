#!/usr/bin/env bash

for file in `ls *py`
do
    chmod 744 $file
done

for file in `ls *sh`
do
    chmod 744 $file
done

for file in `ls *txt`
do
    chmod 644 $file
done

