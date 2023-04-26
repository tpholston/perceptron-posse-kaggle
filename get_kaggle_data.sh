#!/bin/bash

raw_data="data/raw_data"
clean_data="data/clean_data"

mkdir -p "$raw_data"
mkdir -p "$clean_data"

if [ "$1" != "-i" ]; then
    cd "$raw_data"

    export KAGGLE_USERNAME=$1
    export KAGGLE_KEY=$2

    kaggle competitions download -c ucsd-cse-151b-class-competition
fi 