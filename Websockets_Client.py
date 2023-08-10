import asyncio
from autobahn.asyncio.websocket import WebSocketClientProtocol, WebSocketClientFactory

class EchoClientProtocol(WebSocketClientProtocol):

    async def onConnect(self, response):
        print(f"Connected to WebSocket server: {response.peer}")

        # Send a message as soon as the connection is established
        self.sendMessage("Hello, WebSocket server!".encode("utf-8"))

    def onOpen(self):
        print("WebSocket connection opened")

    def onMessage(self, payload, isBinary):
        # Print the received message from the server
        print(f"Received message from server: {payload.decode('utf-8')}")

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed")

if __name__ == "__main__":
    # Create the WebSocket client factory
    factory = WebSocketClientFactory()
    factory.protocol = EchoClientProtocol

    # Connect to the WebSocket server running on localhost, port 8765
    loop = asyncio.get_event_loop()
    coro = loop.create_connection(factory, 'localhost', 8765)
    loop.run_until_complete(coro)

    # Start the asyncio event loop to run the client
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
