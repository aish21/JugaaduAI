'''
Python Script to get information about the input video
'''

import ffmpeg

def get_video_info(video_path):
    probe = ffmpeg.probe(video_path)
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    audio_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'audio'), None)
    duration = float(video_stream['duration'])
    bitrate = int(video_stream['bit_rate'])
    codec = video_stream['codec_name']
    width = int(video_stream['width'])
    height = int(video_stream['height'])
    fps = int(eval(video_stream.get('r', '25')))
    audio_codec = audio_stream['codec_name']
    audio_bitrate = int(audio_stream['bit_rate'])
    audio_sample_rate = int(audio_stream['sample_rate'])
    container = probe['format']['format_name']
    return {'duration': duration, 'bitrate': bitrate, 'codec': codec, 'width': width, 'height': height, 'fps': fps, 'audio_codec': audio_codec, 'audio_bitrate': audio_bitrate, 'audio_sample_rate': audio_sample_rate, 'container': container}


metadata = get_video_info('/Users/aishwarya/Desktop/intuition-v9.0-Jugaadus/backend/tests/original_video.MOV')
print(metadata)