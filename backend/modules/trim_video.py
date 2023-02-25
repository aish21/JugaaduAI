import os
import subprocess

def trim_video(start_time, end_time, video_path):
    # Create output file name
    output_file = os.path.splitext(video_path)[0] + '_trimmed.mp4'
    
    # Run FFmpeg to trim video
    cmd = (f'ffmpeg -ss {start_time} -i "{video_path}" '
           f'-ss 0 -t {end_time} '
           f'-c copy "{output_file}"')
    subprocess.call(cmd, shell=True)
    
    # Return output file path
    return output_file

output_file = trim_video('00:00:00', '00:00:10', '/Users/aishwarya/Desktop/intuition-v9.0-Jugaadus/backend/tests/output.mp4')
print(output_file)
