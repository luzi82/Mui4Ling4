import argparse
import ffmpeg
from google.cloud import storage
import tempfile
import os
import futsu.storage

def ffmpeg_to_storage(input,output,ext):
    print('TOJEPRUAFL ffmpeg_to_storage start input={0}, output={1}, ext={2}' \
        .format(input,output,ext))

    with tempfile.TemporaryDirectory() as tempdir:
        tmp_out_fn = os.path.join(tempdir,'output.{0}'.format(ext))
        print('RQHDKPRBKL tmp_out_fn={0}'.format(tmp_out_fn))

        print('WXXEEBRBZO run ffmpeg start')
        ffmpeg \
            .input(input).output(tmp_out_fn) \
            .global_args('-loglevel', 'quiet') \
            .run()
        print('ROCDCUAFDS run ffmpeg end')

        print('MPAUZXUBBF send to storage start')
        futsu.storage.local_to_path(output, tmp_out_fn)
        print('SVQGNKFBVI send to storage end')

        print('FYOQZXFWOY ffmpeg_to_storage end')

def gcf_ffmpeg_to_storage(data, context):
    if 'attributes' not in data:
        print("ZROCVEXAJA 'attributes' not in data")
        return None
    if 'input' not in data['attributes']:
        print("NUOHGGYRLP 'input' not in data['attributes']")
        return None
    if 'output' not in data['attributes']:
        print("JLQWEOLPSF 'output' not in data['attributes']")
        return None
    if 'ext' not in data['attributes']:
        print("JLQWEOLPSF 'ext' not in data['attributes']")
        return None
    print("RLNPYXIWSS run")
    ffmpeg_to_storage(
        **data['attributes']
    )
    print("AHXFQMZVEO done")
    return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input')
    parser.add_argument('--output')
    parser.add_argument('--ext')
    args = parser.parse_args()

    ffmpeg_to_storage(args.input,args.output,args.ext)
