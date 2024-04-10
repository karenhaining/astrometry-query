#!/bin/bash

APIKEY=$1

python3 client.py --apikey $APIKEY

for f in ./raw_data/*
do 
    filename=$(basename -- "$f")
    filename="${filename%.*}"
    
    resultsdir=./processed_data/$filename
    mkdir -p ./processed_data/$filename

    echo "Processing $f file..."
    python3 client.py --apikey $APIKEY                      \
                      --upload $f                           \
                      --newfits $resultsdir/newfits.fits    \
                      --corr    $resultsdir/corr.fits       \
                      --annotate $resultsdir/annotations.json \
                      --calibrate $resultsdir/calibrate.json \
                      --private

done