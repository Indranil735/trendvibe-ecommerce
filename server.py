#!/usr/bin/env python3
"""
TrendVibe Production Web Server
Serves the consumer storefront on Render cloud container / VM.
"""
import os
import sys
import http.server
import socketserver

PORT = int(os.environ.get("PORT", 8080))
WEB_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "demo")

if not os.path.exists(WEB_DIR):
    WEB_DIR = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)

    def do_GET(self):
        if self.path == "/healthz" or self.path == "/health":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b"{\"status\":\"ok\",\"service\":\"trendvibe-ecommerce\"}")
            return
        return super().do_GET()

print(f"=================================================")
print(f" TrendVibe E-Commerce Cloud Server Running")
print(f" Serving catalog from: {WEB_DIR}")
print(f" Listening on port: {PORT}")
print(f"=================================================")

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            httpd.server_close()
