class ConnectionPool:
    def __init__(self, max_connections):
        self.max_connections = max_connections
        self.connection_pool = [None] * max_connections  # Pre-allocated slots

    def allocate_connection(self, client_socket):
        """
        Allocates a connection slot for a client socket.
        """
        for i in range(self.max_connections):
            if self.connection_pool[i] is None:
                self.connection_pool[i] = client_socket
                return i  # Slot index
        return None

    def release_connection(self, index):
        """
        Releases a connection slot when a client disconnects.
        """
        self.connection_pool[index] = None

    def get_connection_index(self, client_socket):
        """
        Finds the index of the client socket in the connection pool.
        """
        for i, sock in enumerate(self.connection_pool):
            if sock == client_socket:
                return i
        return None
