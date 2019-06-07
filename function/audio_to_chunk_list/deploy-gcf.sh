#!/bin/bash

gcloud functions deploy audio_to_chunk_list \
    --runtime python37 \
    --entry-point gcf_trigger_sample_np_to_chunk_list \
    --trigger-topic audio_to_chunk_list
