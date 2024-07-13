import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # / path / to / your / file

        self.directory = r"D:\MyTestEngineer\Pythonworkspace\PycharmProjects\iJmeter\application\persondata.yml"
        super().__init__(*args, **kwargs)


Handler = MyHandler
