import socket

class SocketManager:
    def __init__(self, connection_pool, event_loop):
        self.connection_pool = connection_pool
        self.event_loop = event_loop  # Store the event loop reference

    def create_server_socket(self, host='localhost', port=8080):
        """
        Creates and returns a server socket bound to the specified host and port.
        """
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen()
        server_socket.setblocking(False)  # Non-blocking mode
        return server_socket

    def handle_new_connection(self, server_socket, mask):
        """
        Accepts a new connection and registers it with the event loop.
        """
        client_socket, addr = server_socket.accept()  # Should be ready to read
        print(f"Accepted connection from {addr}")
        client_socket.setblocking(False)

        connection_index = self.connection_pool.allocate_connection(client_socket)
        if connection_index is None:
            client_socket.close()
            return

        # Register the client socket to be monitored for incoming data
        self.event_loop.add_event(client_socket, self.handle_client_data)

    def handle_client_data(self, client_socket, mask):
        """
        Handles incoming data from the client.
        """
        try:
            data = client_socket.recv(1024)  # Should be ready to read
            if data:
                print(f"Received data: {data.decode()}")
                client_socket.sendall(data)  # Echo back the data
            else:
                print("No data received, closing connection")
                self.close_connection(client_socket)
        except ConnectionResetError:
            print("Connection reset by peer")
            self.close_connection(client_socket)
        except OSError as e:
            print(f"Socket error: {e}")
            self.close_connection(client_socket)

    def close_connection(self, client_socket):
        """
        Closes the connection and frees up the slot in the connection pool.
        """
        try:
            self.event_loop.selector.unregister(client_socket)
        except Exception as e:
            print(f"Failed to unregister socket: {e}")
        
        connection_index = self.connection_pool.get_connection_index(client_socket)
        if connection_index is not None:
            self.connection_pool.release_connection(connection_index)
        client_socket.close()
