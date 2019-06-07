#!/bin/bash

set -e

TIMESTAMP=`date +%s`
TEST_DIR=/tmp/ZOJAOTSOOD-${TIMESTAMP}

mkdir -p ${TEST_DIR}

python3 ../ffmpeg_to_storage/main.py \
    --input=https://rthkaod3-vh.akamaihd.net/i/m4a/radio/archive/radio1/12oclocknews/m4a/20190525.m4a/master.m3u8 \
    --output=${TEST_DIR}/tmp.m4a \
    --ext=m4a

python3 main.py \
    --input=${TEST_DIR}/tmp.m4a \
    --output=${TEST_DIR}/output.json
