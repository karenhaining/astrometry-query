#!/bin/bash

APIKEY=$1

python3 client.py --apikey $APIKEY

for f in ./raw_data/*
do 
    filename=$(basename -- "$f")
    
    resultsdir=./processed_data/$filename
    mkdir -p ./processed_data/$filename

    echo "Processing $f file..."
    python3 client.py --apikey $APIKEY                      \
                      --upload $f                           \
                      --annotate $resultsdir/annotations.json \
                      --calibrate $resultsdir/calibrate.json \
                      --private

done