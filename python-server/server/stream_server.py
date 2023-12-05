import socket
import cv2
import numpy as np
import sys
import signal
import torch
from facenet_pytorch import MTCNN

# Function to handle SIGINT signal
def signal_handler(sig, frame):
    print('Exiting gracefully...')
    sys.exit(0)

# Set up the signal handler for graceful exit
signal.signal(signal.SIGINT, signal_handler)

# Initialize the face detector
mtcnn = MTCNN(keep_all=True, device='cpu')  # Use 'cuda:0' if you have GPU support

# Function to draw bounding boxes on the frame
def draw_boxes(frame, boxes):
    for box in boxes:
        cv2.rectangle(frame,
                      (int(box[0]), int(box[1])),  # Top left corner
                      (int(box[2]), int(box[3])),  # Bottom right corner
                      (0, 255, 0),  # Color (Green)
                      2)  # Thickness
    return frame

# Initialize and set up the socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 666))
server_socket.listen()
BUFFER_SIZE = 4096
HEADER_SIZE = 10

while True:
    print("Waiting for a connection...")
    client_socket, addr = server_socket.accept()
    print("Connection established.")

    # Receive the size of the incoming data
    data_size_str = client_socket.recv(HEADER_SIZE).decode('utf-8').strip()
    if not data_size_str:
        print("No data size received.")
        client_socket.close()
        continue

    # Receive the video data
    data_size = int(data_size_str)
    video_data = b''
    while len(video_data) < data_size:
        packet = client_socket.recv(BUFFER_SIZE)
        if not packet: break
        video_data += packet

    # Check for the "END" message
    end_message = client_socket.recv(3).decode('utf-8')
    if end_message == "END":
        print("Received end message.")
    else:
        print("Did not receive end message. Closing connection.")
    
    # Save the received video data to a file
    with open('received_video.mp4', 'wb') as video_file:
        video_file.write(video_data)

    # Process the saved video file for face detection
    cap = cv2.VideoCapture('received_video.mp4')
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to RGB as MTCNN expects RGB but OpenCV provides BGR
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect faces
        boxes, _ = mtcnn.detect(rgb_frame)
        
        # Draw boxes on the frame
        if boxes is not None:
            frame = draw_boxes(frame, boxes)

        # Display the frame
        cv2.imshow('Face Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    client_socket.close()

server_socket.close()