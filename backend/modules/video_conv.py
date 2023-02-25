import subprocess

input_file = "/Users/aishwarya/Desktop/intuition-v9.0-Jugaadus/backend/tests/original_video.MOV"
output_file = "/Users/aishwarya/Desktop/intuition-v9.0-Jugaadus/backend/tests/output.mp4"

# Use FFmpeg to convert the video
subprocess.run(['ffmpeg', '-i', input_file, '-c:v', 'libx264', '-preset', 'slow', '-crf', '22', '-c:a', 'copy', output_file])
