from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('127.0.0.1', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


class MyHandler(BaseHTTPRequestHandler):
    # A custom handler with overridden method do_GET.

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())


with open('page.html', 'r', encoding='utf-8') as file:
    html = file.read()

run(handler_class=MyHandler)
