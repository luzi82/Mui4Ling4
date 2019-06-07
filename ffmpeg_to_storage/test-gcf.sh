#!/bin/bash

set -e

TIMESTAMP=`date +%s`
echo output to gs://mui4ling4-tmp/test-ffmpeg_to_storage-${TIMESTAMP}.m4a

gcloud pubsub topics publish ffmpeg_to_storage \
    --attribute input=https://rthkaod3-vh.akamaihd.net/i/m4a/radio/archive/radio1/12oclocknews/m4a/20190525.m4a/master.m3u8,output=gs://mui4ling4-tmp/test-ffmpeg_to_storage-${TIMESTAMP}.m4a,ext=m4a
