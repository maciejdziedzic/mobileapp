import socket
import time

def send_video(video_path, server_ip, server_port):
    BUFFER_SIZE = 4096
    HEADER_SIZE = 10

    # Create a socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    # Open the video file and read its content
    with open(video_path, 'rb') as video_file:
        video_data = video_file.read()
        
    # Send the size of the video data
    data_size_str = f"{len(video_data):<{HEADER_SIZE}}"
    client_socket.sendall(data_size_str.encode('utf-8'))

    # Send the video file in chunks
    for i in range(0, len(video_data), BUFFER_SIZE):
        print(len(video_data))
        client_socket.sendall(video_data[i:i + BUFFER_SIZE])

    # Slight delay before sending the "END" message
    time.sleep(0.5)
    end_message = "END".encode('utf-8')
    client_socket.sendall(end_message)

    client_socket.close()

# Example usage
send_video('face_rec.mp4', '127.0.0.1', 666)
