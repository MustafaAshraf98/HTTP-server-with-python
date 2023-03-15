import time
from http.server import HTTPServer, BaseHTTPRequestHandler

host = "172.19.224.1"
port = 5555


class NeuralHTTP(BaseHTTPRequestHandler):

    # Main Function to print Hello World on http server.
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(
            bytes("<html><body><h1>Hello World</h1></body></html>", "utf-8"))

    # A Function to show time.
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        date = time.strftime("%Y-%M-%D %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"time": "' + date + '"}', "utf-8"))


server = HTTPServer((host, port), NeuralHTTP)
print("\nServer is running now...")
server.serve_forever()
server.server_close()
print("Server is Stopped")
