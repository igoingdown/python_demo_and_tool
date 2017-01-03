#!/usr/bin/env bash

for file in `ls *py`
do
    chmod +x $file
done
