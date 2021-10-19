# https://www.askpython.com/python-modules/python-httpserver
# server.py
import http.server # Our http server handler for http requests
import socketserver # Establish the TCP Socket connections
 
PORT = 9000
 
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
 
Handler = MyHttpRequestHandler
 
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Http Server Serving at port", PORT)
    httpd.serve_forever()


# 
# if __name__ == "__main__":
#     URL = 'https://restapi.amap.com/v3/geocode/geo'
#     parameters = {
#         'key':amap_key,
#         'address':"水果湖",
#         'output':'json',
#     }
# python -m http.server 9000