import socket

def send_message(message):
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server's address and port
    server_address = ('localhost', 12345)
    client_socket.connect(server_address)

    try:
        # Send data to the server
        client_socket.sendall(message.encode('utf-8'))

        # Receive the response from the server
        response = client_socket.recv(1024).decode('utf-8')

        print(f"Received response from server: {response}")

    finally:
        # Clean up the connection
        client_socket.close()

if __name__ == "__main__":
    message_to_send = "Hello, server!"
    send_message(message_to_send)
