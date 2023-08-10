from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory

class EchoServerProtocol(WebSocketServerProtocol):

    def onMessage(self, payload, isBinary):
        # Echo the received message back to the client
        self.sendMessage(payload, isBinary)

if __name__ == "__main__":
    # Create the WebSocket server factory
    factory = WebSocketServerFactory()
    factory.protocol = EchoServerProtocol

    # Listen on localhost, port 8765
    reactor.listenTCP(8765, factory)

    print("WebSocket server started at ws://localhost:8765")

    # Start the Twisted reactor to run the server
    reactor.run()
