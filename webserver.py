#!/usr/bin/python
import SimpleHTTPServer
import SocketServer
import os

DIR_NAME = os.path.dirname(os.path.abspath(__file__))
PATH_FILE = os.join(DIR_NAME, "index.html")


PORT = 80

class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        p = self.path
        if not (p.endswith('.png')
               or p.endswith('.css')
               or p.endswith('.ico')
               or p.endswith('.ttf')
               or p.endswith('.woff')
               or p.endswith('.woff2')):
            _FD = open(PATH_FILE, 'r')
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.wfile.write('\n')
            self.wfile.write(_FD.read())
            _FD.close()
        else:
            return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

httpd = SocketServer.TCPServer(("", PORT), Handler)
httpd.serve_forever()
