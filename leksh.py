from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>This pc</title>
    </head>
    <body>
        <h4>Device specification-25016373</h4>
        <table border="3">
            <tr>
                <th>.s.no</th>
                <th>data</th>
                <th>specification</th>
            </tr>
            <tr>
                <th>1</th>
                <th>device name</th>
                <th>ThO215-75-G2</th>
            </tr>
            <tr>
                <th>2</th>
                <th>processor</th>
                <th>Intel core i3</th>
            </tr>
        </table>
    </body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()