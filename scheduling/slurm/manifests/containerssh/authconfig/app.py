import cgi
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # print("Request headers:", self.headers)
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        data = json.loads(self.rfile.read(int(self.headers.get('Content-Length'))))

        if "publicKey" in data.keys():
            if data["publicKey"] == "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC8a9Y3Er6C6rN3HIOGIJf5x/nrngRfVBwL/e7lh0Xe2q8a53xEveWy4jk/4XLaD8g4mmTIzhqShfgUqr7zd/vVeMxr3ALRBuDU9/R36XA0OCfaJ0Rv6Xn9JZALv80bdHKWfSSOTdG3ujbIZ/cWHUUTzf51AXnX6YTZKn68ryBxzDuKHHDQ3rGZS6evjrtRlulkx5CLhFXvoAEATMZJtExz96sABC1/ookPhABeklp0ECl5uAfHh6r0JCU6sSywB5PdfBwjWOY8YUB4eDrvAASoTy3BIUHqwClc72CrSSxcpcVZYquTj785xMV0uduj99GxU4B0TVlkGocSqUngnTq8RS2Nb5960tLwcTJ+hvkn4mu+ehqehBcrnhvA8CXaT7WH9T27eROrhE1eIMKuYprP6DleXld3H4Smt+DKosWmdVUSLjTEaN31xis7lgXkoWDZNGJvwYotJo1xrmf0CZHgQCtbG/WKDkHydHchRvFPmkrUBBBQyBtuLlszOWJjQCyLlb1Ox29ouwH9XCOAO6iYZ2tsHHFnqOLNkcSbF5R17CJjcvbnEIKIwB6/7eSdAyRqP8GDv7Ukz4G3dUBMjkz0/IGI1F8ckA5X6MBJxO2g7Qw/osZ+/Y7oL3EhgV04b/cNcsA2zO5Ms3mZ/u1ZeuziJv8z1o7pOTUzCHzdTgEvLQ==":
                self.wfile.write(bytes("{\"success\": true}", "utf-8"))
            else:
                print("not trusted: ", data)
                self.wfile.write(bytes("{\"success\": false}", "utf-8"))
        else:
            print("no publicKey: ", data)
            self.wfile.write(bytes("{\"success\": false}", "utf-8"))

def main():
    print('Listening on 0.0.0.0:8080')
    server = HTTPServer(('', 8080), RequestHandler)
    server.serve_forever()

if __name__ == "__main__":
    main()