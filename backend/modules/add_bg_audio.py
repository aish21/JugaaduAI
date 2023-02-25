'''
Python Script to add background audio to a video
'''

import subprocess

# Set the input video file and audio file paths
input_video = '/Users/aishwarya/Desktop/intuition-v9.0-Jugaadus/backend/tests/output.mp4'
input_audio = '/Users/aishwarya/Desktop/intuition-v9.0-Jugaadus/backend/tests/custom_audio.mp3'

# Set the output video file path
output_video = '/Users/aishwarya/Desktop/intuition-v9.0-Jugaadus/backend/tests/output_audio_vid.mp4'

# Use ffmpeg to merge the audio and video files
command = ["ffmpeg", "-i", input_video, "-i", input_audio, "-c:v", "copy", "-c:a", "aac", "-map", "0:v:0", "-map", "1:a:0", "-shortest", output_video]
subprocess.run(command)
