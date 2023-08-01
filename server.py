import socket

def modify_message(message):
    # This function will just add " (Server Modified)" to the message.
    return message + " (Server Modified)"

def start_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)

    print("Server is ready and listening...")

    while True:
        # Wait for a connection
        connection, client_address = server_socket.accept()

        try:
            print(f"Connection established with {client_address}")

            # Receive data from the client
            data = connection.recv(1024).decode('utf-8')

            if data:
                print(f"Received message from client: {data}")

                # Modify the message
                modified_message = modify_message(data)

                # Send the modified message back to the client
                connection.sendall(modified_message.encode('utf-8'))

        finally:
            # Clean up the connection
            connection.close()

if __name__ == "__main__":
    start_server()
