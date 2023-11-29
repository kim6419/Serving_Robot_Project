from http.server import BaseHTTPRequestHandler, HTTPServer

# 서버 설정
host = '10.42.0.1'
port = 8080

class MenuHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/menu':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            menu = """
<html>
<head>
    <title> menu </title>
</head>
<body>
    <h1> Group-C MENU T1 </h1>
    <p>
        <img src="data:image/jpeg;base64,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" width="200" height="150" alt="치킨 이미지">
        CHICKEN
    </p>
    <p>
        <img src="hamburger.jpg" width="200" height="150" alt="햄버거 이미지">
        HAMBURGER 
    </p>
    <p>
        <img src="pizza.jpg" width="200" height="150" alt="피자 이미지">
        PIZZA 
    </p>
</body>   
</html>
            """
            self.wfile.write(menu.encode())
        elif self.path == '/option1':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'option_1 selected')
        elif self.path == '/option2':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'option_2 selected')
        elif self.path == '/option3':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'option_3 selected')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'out of boundary_group_c')



if __name__ == '__main__':
    web_server = HTTPServer((host, port), MenuHandler)
    print(f"서버가 {host}:{port}에서 실행 중…")
    web_server.serve_forever()
