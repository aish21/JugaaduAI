import ffmpeg
import cv2

input_path = "/Users/aishwarya/Desktop/intuition-v9.0-Jugaadus/backend/tests/output.mp4"
output_path = "/Users/aishwarya/Desktop/intuition-v9.0-Jugaadus/backend/tests/output_inc_res.mp4"

# Read input video
cap = cv2.VideoCapture(input_path)

# Get input video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create VideoWriter object to write output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Loop over frames and denoise each frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Apply denoising
    frame = cv2.fastNlMeansDenoisingColored(frame, None, 10, 10, 7, 21)

    # Write frame to output video
    out.write(frame)

# Release resources
cap.release()
out.release()
