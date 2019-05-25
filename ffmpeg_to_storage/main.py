import argparse
import ffmpeg
from google.cloud import storage
import tempfile
import os

def ffmpeg_to_storage(input,output_bucket,output_blob_name):
    print('TOJEPRUAFL ffmpeg_to_storage start input={0}, output_bucket={1}, output_blob_name={2}' \
        .format(input,output_bucket,output_blob_name))

    with tempfile.TemporaryDirectory() as tempdir:
        tmp_out_fn = os.path.join(tempdir,output_blob_name)
        print('RQHDKPRBKL tmp_out_fn={0}'.format(tmp_out_fn))

        print('WXXEEBRBZO run ffmpeg start')
        ffmpeg \
            .input(input).output(tmp_out_fn) \
            .global_args('-loglevel', 'quiet') \
            .run()
        print('ROCDCUAFDS run ffmpeg end')

        print('MPAUZXUBBF google cloud storage prepare')
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(output_bucket)
        blob = bucket.blob(output_blob_name)
        
        print('IUZUOVORBN upload')
        blob.upload_from_filename(tmp_out_fn)

        print('FYOQZXFWOY ffmpeg_to_storage done')

def gcf_ffmpeg_to_storage(data, context):
#    if 'data' not in data: return None
#    if 'input' not in data['data']: return None
#    if 'output_bucket' not in data['data']: return None
#    if 'output_blob_name' not in data['data']: return None
#    ffmpeg_to_storage(
#        data['data']['input'],
#        data['data']['output_bucket'],
#        data['data']['output_blob_name']
#    )
    if 'attributes' not in data:
        print("ZROCVEXAJA 'attributes' not in data")
        return None
    if 'input' not in data['attributes']:
        print("NUOHGGYRLP 'input' not in data['attributes']")
        return None
    if 'output_bucket' not in data['attributes']:
        print("JLQWEOLPSF 'output_bucket' not in data['attributes']")
        return None
    if 'output_blob_name' not in data['attributes']:
        print("XVTJXUXRQG 'output_blob_name' not in data['attributes']")
        return None
    print("RLNPYXIWSS run")
    ffmpeg_to_storage(
        data['attributes']['input'],
        data['attributes']['output_bucket'],
        data['attributes']['output_blob_name']
    )
    print("AHXFQMZVEO done")
    return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input')
    parser.add_argument('--output_bucket')
    parser.add_argument('--output_blob_name')
    args = parser.parse_args()

    ffmpeg_to_storage(args.input,args.output_bucket,args.output_blob_name)
