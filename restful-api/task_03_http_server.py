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
import http.server
import socketserver
import json


class Server(http.server.BaseHTTPRequestHandler):
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
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write('Hello, this is a simple API!'.encode("utf-8"))
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write("OK".encode("utf-8"))
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write("Endpoint not found".encode("utf-8"))


if __name__ == "__main__":
    with socketserver.TCPServer(('', 8000), Server) as httpd:
        httpd.serve_forever()
