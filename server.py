from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import psycopg2

IP = 'localhost'
PORT = 8000

# connecting to existing db server with table "cities"
conn = psycopg2.connect(dbname='spa_db', user='postgres', password='Qwerty123', host='localhost', port='5433')
cursor = conn.cursor()


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = (IP, PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


class MyHandler(BaseHTTPRequestHandler):
    # A custom request-handler with overridden method do_GET.

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")  # when data is returned, there should be at least one header line of the form Content-type: <type>/<subtype> where <type> and <subtype> should be registered MIME types, e.g. "text/html" or "text/plain".
        self.end_headers() # blank line for cut-off headers from data
        # read database
        # modify view in page.html
        # print updated view
        # where should be placed a controller function ?
        self.wfile.write(html.encode())  # data of response


with open('page.html', 'r', encoding='utf-8') as file:
    html = file.read()

if __name__ == '__main__':
    run(handler_class=MyHandler)
