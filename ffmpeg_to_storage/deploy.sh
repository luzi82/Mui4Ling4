#!/bin/bash

gcloud functions deploy ffmpeg_to_storage \
    --runtime python37 \
    --timeout +P540s \
    --entry-point gcf_ffmpeg_to_storage \
    --trigger-topic ffmpeg_to_storage
