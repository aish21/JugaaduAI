'''
Python Script for the final set of functions to be called.
'''

import cv2
import os
import subprocess
import moviepy.editor as mp
from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.editor import *
import numpy as np
from multiprocessing import Pool
import speech_recognition as sr
import pysrt


def extract_audio(input_video):
  audio_file = input_video
  subprocess.call(['ffmpeg', '-i', input_video, '-vn', '-acodec', 'pcm_s16le', '-ar', '44100', '-ac', '2', audio_file])
  return audio_file

def add_audio_to_video(input_video, input_audio, output_video):
    # Use ffmpeg to merge the audio and video files
    command = ["ffmpeg", "-i", input_video, "-i", input_audio, "-c:v", "copy", "-c:a", "aac", "-map", "0:v:0", "-map", "1:a:0", "-shortest", output_video]
    subprocess.run(command)
    return output_video

def combine_videos(input_path1, input_path2):
    clip1 = VideoFileClip(input_path1)
    clip2 = VideoFileClip(input_path2)

     # Add a small buffer time to the end of the first clip
    clip1 = clip1.set_end(clip1.duration + 0.1)

    # Concatenate the clips and preserve audio
    final_clip = concatenate_videoclips([clip1.set_audio(clip1.audio.set_duration(clip1.duration+clip2.duration)), clip2.set_audio(clip2.audio.set_start(clip1.duration))])

    # Write the output file
    output_path = 'output.mp4'
    final_clip.write_videofile(output_path, fps=clip1.fps, codec='libx264', audio_codec='aac', temp_audiofile='temp-audio.m4a', remove_temp=True)

    return output_path

def split_video(input_video_path, timestamp1, timestamp2):
    # Create output file names
    part1_video_path = os.path.splitext(input_video_path)[0] + '_part1.mp4'
    part2_video_path = os.path.splitext(input_video_path)[0] + '_part2.mp4'
    part3_video_path = os.path.splitext(input_video_path)[0] + '_part3.mp4'

    # Calculate start and end times for each part
    start_time1 = '00:00:00'
    end_time1 = f'{int(timestamp1//3600):02d}:{int((timestamp1%3600)//60):02d}:{int(timestamp1%60):02d}'
    start_time2 = end_time1
    end_time2 = f'{int(timestamp2//3600):02d}:{int((timestamp2%3600)//60):02d}:{int(timestamp2%60):02d}'
    start_time3 = end_time2
    end_time3 = '999:59:59'

    # Split the video into three parts while preserving the original audio
    subprocess.call([
        'ffmpeg',
        '-i', input_video_path,
        '-map', '0:v',
        '-map', '0:a',
        '-ss', start_time1,
        '-to', end_time1,
        '-c', 'copy',
        '-y', part1_video_path
    ])
    subprocess.call([
        'ffmpeg',
        '-i', input_video_path,
        '-map', '0:v',
        '-map', '0:a',
        '-ss', start_time2,
        '-to', end_time2,
        '-c', 'copy',
        '-y', part2_video_path
    ])
    subprocess.call([
        'ffmpeg',
        '-i', input_video_path,
        '-map', '0:v',
        '-map', '0:a',
        '-ss', start_time3,
        '-to', end_time3,
        '-c', 'copy',
        '-y', part3_video_path
    ])

    return snip_video(part1_video_path, part3_video_path)

def snip_video(act1, act2):
    video_filenames = []
    video_filenames.append(act1)
    video_filenames.append(act2)
    combine_videos(video_filenames, '/Users/aishwarya/Desktop/intuition-v9.0-Jugaadus/backend/tests/output_snipped.mp4')

def trim_video(input_video_path, start_time, end_time, output_video_path):
    # Open input video file
    cap = cv2.VideoCapture(input_video_path)

    # Get video frame rate and dimensions
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Calculate start and end frame numbers
    start_frame = int(start_time * fps)
    end_frame = int(end_time * fps)
    if end_frame > frame_count:
        end_frame = frame_count

    # Set video writer parameters
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out_params = (fourcc, fps, (width, height))

    # Create video writer
    out = cv2.VideoWriter(output_video_path, *out_params)

    # Read frames and write to output video
    frame_num = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_num >= start_frame and frame_num < end_frame:
            out.write(frame)
        if frame_num >= end_frame:
            break
        frame_num += 1

    # Release resources
    cap.release()
    out.release()

    # Add audio to output video
    command = f"ffmpeg -i {input_video_path} -ss {start_time} -to {end_time} -c copy -map 0:v:0 -map 0:a:0 {os.path.splitext(output_video_path)[0]}_temp.mp4"
    os.system(command)
    os.rename(f"{os.path.splitext(output_video_path)[0]}_temp.mp4", output_video_path)
    
    return output_video_path

def compress_video_ffmpeg(input_file, output_file, bitrate='1000k'):
    # Create the FFmpeg command to compress the video
    command = f'ffmpeg -i {input_file} -vcodec libx264 -b:v {bitrate} -preset slow -pix_fmt yuv420p -movflags +faststart {output_file}'

    # Run the FFmpeg command
    os.system(command)

    print(f'Compressed video saved to {output_file}')
    return output_file


def slowed_down(input_path, output_path, scale=2, interpolation=cv2.INTER_CUBIC):
    # Upscale video
    cap = cv2.VideoCapture(input_path)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), 30, (width*scale, height*scale))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.resize(frame, (width*scale, height*scale), interpolation=interpolation)
            out.write(frame)
        else:
            break

    cap.release()
    out.release()

def process_frame(frame):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    brightness_factor = target_brightness / hsv_frame[:, :, 2].mean()
    saturation_factor = target_saturation / hsv_frame[:, :, 1].mean()
    
    hsv_frame[:, :, 1] = np.clip(hsv_frame[:, :, 1] * saturation_factor, 0, 255)
    hsv_frame[:, :, 2] = np.clip(hsv_frame[:, :, 2] * brightness_factor, 0, 255)
    
    modified_frame = cv2.cvtColor(hsv_frame, cv2.COLOR_HSV2BGR)
    # rotated_frame = cv2.rotate(modified_frame, cv2.ROTATE_180)
    return modified_frame

def saturation_brightness(video):
    # Calculate the average brightness and saturation of the video
    avg_saturation = 0
    avg_brightness = 0
    frame_count = 0

    while True:
        ret, frame = video.read()
        if not ret:
            break
        
        # Convert the frame to the HSV color space
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Compute the average brightness and saturation values of the frame
        avg_saturation += hsv_frame[:, :, 1].mean()
        avg_brightness += hsv_frame[:, :, 2].mean()
        frame_count += 1

    avg_saturation /= frame_count
    avg_brightness /= frame_count

    # Define the target brightness and saturation values
    target_saturation = 1.2 * avg_saturation
    target_brightness = 32 + avg_brightness

    # Set up the output video codec and format
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    fps = int(video.get(cv2.CAP_PROP_FPS))
    frame_size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    # Set up the output video file
    output_file = cv2.VideoWriter("output.mp4", fourcc, fps, frame_size)
    output_file.set(cv2.VIDEOWRITER_PROP_NSTRIPES, -1)

    # Loop through the frames of the input video and adjust the brightness and saturation
    video.set(cv2.CAP_PROP_POS_FRAMES, 0) # reset the frame counter
    while True:
        ret, frame = video.read()
        if not ret:
            break
        
        # Convert the frame to the HSV color space
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Calculate the brightness and saturation scaling factors based on the deviation from the target values
        brightness_factor = target_brightness / hsv_frame[:, :, 2].mean()
        saturation_factor = target_saturation / hsv_frame[:, :, 1].mean()
        
        # Scale the brightness and saturation of the frame
        hsv_frame[:, :, 1] = np.clip(hsv_frame[:, :, 1] * saturation_factor, 0, 255)
        hsv_frame[:, :, 2] = np.clip(hsv_frame[:, :, 2] * brightness_factor, 0, 255)
        
        # Convert the frame back to the BGR color space
        modified_frame = cv2.cvtColor(hsv_frame, cv2.COLOR_HSV2BGR)
        #rotated_frame = cv2.rotate(modified_frame, cv2.ROTATE_180)
        # Write the modified frame to the output video file
        output_file.write(frame)

    # Release the input and output video files and close all windows
    video.release()
    output_file.release()
    cv2.destroyAllWindows()

def extract_audio(video_file):
    audio_file = "audio_new.wav"
    subprocess.call(['ffmpeg', '-i', video_file, '-vn', '-acodec', 'pcm_s16le', '-ar', '44100', '-ac', '2', audio_file])
    return audio_file
    
def generate_subtitles(video_path):
  # Initialize the speech recognition engine
  r = sr.Recognizer()

  with sr.AudioFile(extract_audio(video_path)) as source:
      # Extract the audio from e video file
      audio = r.record(source)
  # Recognize the speech in the audio file
      speech_text = r.recognize_google(audio)

  # Split the speech text into chunks of 10 seconds
  speech_chunks = [speech_text[i:i+100] for i in range(0, len(speech_text), 100)]

  # Initialize a SRT object to store the captions
  captions = pysrt.SubRipFile()

  # Initialize a counter for the caption IDs
  caption_id = 1

  # Loop through the speech chunks and generate captions
  for speech_chunk in speech_chunks:
      # Create a new caption object
      caption = pysrt.SubRipItem()
      # Set the caption ID and start/end times
      caption.index = caption_id
      caption.start.seconds = (caption_id - 1) * 10
      caption.end.seconds = caption_id * 10
      # Set the caption text
      caption.text = speech_chunk
      # Add the caption to the SRT object
      captions.append(caption)
      # Increment the caption ID counter
      caption_id += 1

  # Save the captions as an SRT file
  srt_output = 'subtitles.srt'
  captions.save(srt_output)
  add_subtitles(video_path, srt_output)

def add_subtitles(input_video, captions):
    # Create output file name
    output_file = 'video_with_subtitles_added.mp4'

    # Run FFmpeg to add subtitles to video
    cmd = f'ffmpeg -i "{input_video}" -vf subtitles="{captions}" "{output_file}"'
    subprocess.call(cmd, shell=True)

    # Return output file path
    return output_file

input_path = '/Users/aishwarya/Desktop/intuition-v9.0-Jugaadus/backend/tests/OG.mp4'
input_path_aud = '/Users/aishwarya/Desktop/intuition-v9.0-Jugaadus/backend/tests/audio.wav'
output_vid = '/Users/aishwarya/Desktop/intuition-v9.0-Jugaadus/backend/tests/OG_transition.mp4'

# # Extract audio from mp4 file
# audio_file = extract_audio(input_path)
# print(audio_file)

# # Snip a section out of the video
# output_video_paths = split_video(input_path, 10, 20)
# print(output_video_paths)

# # Trim a section of video
# output_video_path = trim_video(input_path, 10.0, 20.0, '/Users/aishwarya/Desktop/intuition-v9.0-Jugaadus/backend/tests/output_trimmed.mp4')
# print(f"Trimmed video saved to {output_video_path}")

# Speed up a section of the video
# speed_up_video_pyav(input_path, '/Users/aishwarya/Desktop/intuition-v9.0-Jugaadus/backend/tests/OG_sped_up.mp4', 3.0)

# Video Compression
# compress_video_ffmpeg(input_path, '/Users/aishwarya/Desktop/intuition-v9.0-Jugaadus/backend/tests/OG_compressed.mp4', '500k')

# Video Slowdown
# slowed_down(input_path, '/Users/aishwarya/Desktop/intuition-v9.0-Jugaadus/backend/tests/OG_upscaled.mp4', scale=2, interpolation=cv2.INTER_LINEAR)

# # Add audio to video file
# added_audio = add_audio_to_video(input_path, input_path_aud, output_vid)
# print(added_audio)

# Combine
# combine_videos('/Users/aishwarya/Desktop/intuition-v9.0-Jugaadus/backend/tests/OG_part1.mp4', '/Users/aishwarya/Desktop/intuition-v9.0-Jugaadus/backend/tests/OG_part2.mp4')

# # Saturation and Brightness
# video = '/Users/aishwarya/Desktop/intuition-v9.0-Jugaadus/backend/tests/OG_part1.mp4'
# saturation_brightness(cv2.VideoCapture(video))

# Caption Generation
video_path = "/Users/aishwarya/Desktop/intuition-v9.0-Jugaadus/backend/tests/Shruthi.MOV"
generate_subtitles(video_path)