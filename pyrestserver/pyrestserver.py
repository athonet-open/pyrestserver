PORT = 8080

#import http.server
import socketserver
# import json
# import simplejson
#import os
from pyrestserver.FakeServerHandler import FakeServerHandler

def main():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), FakeServerHandler) as httpd:
        print("Serving at port {}".format(PORT))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            httpd.server_close()
            print("Closing... BYE!")

