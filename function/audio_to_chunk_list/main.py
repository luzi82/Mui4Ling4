import argparse
import ffmpeg
import numpy
import os
import tempfile
import futsu.json
import futsu.gcp
import futsu.storage

def sample_np_to_chunk_list(sample_np):
    sample_np_len = sample_np.shape[0]
    
    chunk_start_np = numpy.arange(start=0,stop=sample_np_len-800+1,step=400).reshape(-1,1)
    chunk_len = chunk_start_np.shape[0]
    idx_np   = numpy.arange(800).reshape(1,-1)
    chunk_idx_np = chunk_start_np + idx_np
    
    sample2_np = sample_np*sample_np
    
    chunk_sample2_np = sample2_np[chunk_idx_np]
    chunk_sample2_sum_np = numpy.sum(chunk_sample2_np,axis=1)

    s_threshold = numpy.sort(chunk_sample2_sum_np)[chunk_len//10]

    ret_chunk_list = []
    active = True
    inactive_count = 0
    active_start = None
    for i in range(chunk_len):
        s = chunk_sample2_sum_np[i]
        t = i*400
        if active:
            if s >= s_threshold:
                inactive_count = 0
            else:
                inactive_count += 1
                if inactive_count >= 4:
                    active = False
                    if active_start:
                        active_end = t-400
                        if active_end - active_start > 8000*2:
                            ret_chunk_list.append({
                                'start':'{0}'.format(active_start),
                                'end'  :'{0}'.format(active_end)
                            })
        else:
            if s >= s_threshold:
                inactive_count = 0
                active = True
                active_start = t-400
    
    return ret_chunk_list

def file_to_sample_np(filename):
    bytes, _ = ffmpeg \
        .input(filename) \
        .output('-', format='s16le', acodec='pcm_s16le', ac=1, ar='8k') \
        .overwrite_output() \
        .global_args('-loglevel', 'quiet') \
        .run(capture_stdout=True)
    sample_np = numpy.fromstring(bytes, numpy.dtype(numpy.int16))
    sample_np = sample_np/32768
    return sample_np

def audio_path_to_chunk_list_path(output, input):
    with tempfile.TemporaryDirectory() as tempdir:
        tmp_input = os.path.join(tempdir, 'input')
        tmp_output = os.path.join(tempdir, 'output')

        futsu.storage.path_to_local(tmp_input, input)
        sample_np = file_to_sample_np(tmp_input)
        chunk_list = sample_np_to_chunk_list(sample_np)
        futsu.json.data_to_file(tmp_output, chunk_list)
        futsu.storage.local_to_path(output, tmp_output)

def gcf_trigger_sample_np_to_chunk_list(data, context):
    if 'attributes' not in data:
        print("EHXAVCTXPR 'attributes' not in data")
        return None
    if 'input' not in data['attributes']:
        print("IRVQBOUHPN 'input' not in data['attributes']")
        return None
    if 'output' not in data['attributes']:
        print("LYRPCIBWOQ 'output' not in data['attributes']")
        return None
    if 'ext' not in data['attributes']:
        print("BYWPPXXCAR 'ext' not in data['attributes']")
        return None

    gcf_sample_np_to_chunk_list(**data['attributes'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input')
    parser.add_argument('--output')
    args = parser.parse_args()

    audio_path_to_chunk_list_path(args.output, args.input)
