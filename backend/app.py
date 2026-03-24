from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello from Effective Mobile!")

if __name__ == "__main__":
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleHandler)
    httpd.serve_forever()
    