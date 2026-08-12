import http.server
import socketserver
import os

PORT = 3000

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def send_error(self, code, message=None, explain=None):
        if code == 404:
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            if os.path.exists("404.html"):
                with open("404.html", "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.wfile.write(b"404 Not Found")
        else:
            super().send_error(code, message, explain)

if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"Serving local dev server on http://localhost:{PORT} with custom 404 handling...")
        httpd.serve_forever()
