import time
import selectors

class EventLoop:
    def __init__(self):
        self.selector = selectors.DefaultSelector()

    def add_event(self, sock, callback, mask=selectors.EVENT_READ):
        """
        Registers a socket and its callback function with the event loop.
        """
        self.selector.register(sock, mask, callback)

    def run(self):
        """
        Runs the event loop, processing events asynchronously.
        """
        print("Event loop started")
        try:
            while True:
                events = self.selector.select(timeout=1)
                for key, mask in events:
                    callback = key.data
                    callback(key.fileobj, mask)
                # Prevent high CPU usage by sleeping briefly
                time.sleep(0.01)
        except KeyboardInterrupt:
            print("Event loop stopped")

    def stop(self):
        """
        Stops the event loop.
        """
        self.selector.close()
