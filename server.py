from http.server import HTTPServer, SimpleHTTPRequestHandler;
port = 3000

class miServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/":
            self.path = "index.html"
            return SimpleHTTPRequestHandler.do_GET(self)
print("Ejecutando serer en puerto", port)
server = HTTPServer(("localhost", port), miServer)
server.serve_forever()