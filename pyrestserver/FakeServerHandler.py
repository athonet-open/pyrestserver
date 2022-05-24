import http.server
import json
import simplejson

server_data = {}

class FakeServerHandler(http.server.SimpleHTTPRequestHandler):
    def parse_data(self):
        self.data_string = "{}"
        if int(self.headers.get('Content-Length', 0)) > 0:
            self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        self.data = simplejson.loads(self.data_string)
    
    def json_response(self, code=200, data={}):
        txt = json.dumps(data, sort_keys=True, indent=4)
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write("{}\n".format(txt).encode('utf-8'))
        return

    def do_GET(self):
        global server_data
        if self.path == '/data':
            self.json_response(200, server_data)
        else:
            self.json_response(200, {'msg': 'Hey'})
    
    def do_PUT(self):
        global server_data
        if self.path == '/data':
            self.parse_data()
            server_data = self.data
            self.json_response(200, server_data)
        else:
            self.json_response(200, {'msg': 'Hey'})