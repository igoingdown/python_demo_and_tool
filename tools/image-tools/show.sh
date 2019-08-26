#!/usr/bin/env bash

g++ show_pictures.cpp -std=c++11 `pkg-config --cflags --libs opencv`  -o test
./test
