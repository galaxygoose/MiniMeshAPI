# MiniMeshAPI

MiniMeshAPI is a lightweight, secure, and efficient API framework designed specifically for IoT devices. It allows multiple devices to communicate seamlessly with each other over persistent connections, with a focus on security and low CPU usage.

## Features

- **Persistent Connections**: Maintain open connections with IoT devices for real-time communication.
- **Secure Authentication**: Ensure only authorized devices can connect and communicate.
- **Low Resource Usage**: Optimized for low CPU and memory usage, making it ideal for resource-constrained environments.
- **Custom Event Loop**: Handles multiple connections asynchronously, without relying on external libraries.

## Installation

To clone the repository and set up MiniMeshAPI on your local machine, run the following commands:
```bash
git clone https://github.com/yourusername/MiniMeshAPI.git
```

##Usage
To start the MiniMeshAPI server, run: 
```python main.py```
You can then connect to the server using a client script or tools like telnet or netcat to test the connection.

##Testing
To test the MiniMeshAPI, you can create a simple client script (client.py) to send and receive messages from the server. Here’s an example of how set up a basic client:
```import socket

def run_client():
    # Set up the client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080))
    
    try:
        # Send a message to the server
        client_socket.sendall(b"Hello, MiniMeshAPI!")
        
        # Receive a response from the server
        response = client_socket.recv(1024)
        print(f"Received: {response.decode()}")
    finally:
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    run_client()
```
How to Run the Test:
- **Start the MiniMeshAPI server
- **In a separate terminal, run the client.py script
- **You should see the client sending a message to the server and receiving a response

## Contributing
I welcome contributions! If you'd like to contribute, please fork the repository, make your changes, and submit a pull request. I'm a novice and any help is always appreciated!

#License

This project is licensed under the MIT License
