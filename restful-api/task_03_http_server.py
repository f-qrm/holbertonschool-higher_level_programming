#!/usr/bin/env python3
"""
Simple HTTP server providing a minimal API with three endpoints.

This server handles GET requests on three paths:
- "/" returns a plain text greeting message.
- "/data" returns a JSON object with sample user data.
- "/status" returns a plain text status message "OK".

For any other path, the server responds with a 404 Not Found error.

Classes:
    Server(BaseHTTPRequestHandler): Handles HTTP GET requests and sends
    appropriate
    responses.

Usage:
    Run the script to start the server on port 8000.
"""
from http.server import *
import json


class Server(BaseHTTPRequestHandler):
    """
    HTTP request handler class that processes GET requests for predefined
    endpoints.

    Methods:
        do_GET(): Handle GET requests; send responses based on the request
        path.
    """
    def do_GET(self):
        """
        Handle GET HTTP requests.

        Responds differently depending on the request path:
        - '/'      : sends a plain text greeting.
        - '/data'  : sends JSON content with sample data.
        - '/status': sends a plain text "OK" status message.
        - Others   : sends a 404 Not Found error.

        Returns:
            None
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header('content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('content-type', 'application/json')
            self.end_headers()
            dict = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(dict).encode("utf-8"))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header('content-type', 'application/json')
            self.end_headers()  
            self.wfile.write(b"404 Not Found")


port = HTTPServer(('', 8000), Server)
port.serve_forever()
