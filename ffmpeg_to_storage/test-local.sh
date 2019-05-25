#!/bin/bash

set -e

TIMESTAMP=`date +%s`
echo output to gs://mui4ling4-tmp/test-${TIMESTAMP}.m4a

python3 main.py \
    --input=https://rthkaod3-vh.akamaihd.net/i/m4a/radio/archive/radio1/12oclocknews/m4a/20190525.m4a/master.m3u8 \
    --output_bucket=mui4ling4-tmp \
    --output_blob_name=test-${TIMESTAMP}.m4a
