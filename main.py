from connections.event_loop import EventLoop
from connections.socket_manager import SocketManager
from connections.connection_pool import ConnectionPool

def main():
    max_connections = 10
    connection_pool = ConnectionPool(max_connections)
    event_loop = EventLoop()  # Create the event loop
    socket_manager = SocketManager(connection_pool, event_loop)  # Pass event loop to SocketManager

    # Set up the event loop and server socket
    server_socket = socket_manager.create_server_socket()

    # Register the server socket with the event loop
    event_loop.add_event(server_socket, socket_manager.handle_new_connection)

    # Run the event loop
    event_loop.run()

if __name__ == "__main__":
    main()
