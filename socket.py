import socket
HOST = '127.0.0.1'
PORT = 8000
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.bind((HOST,PORT))
listen_socket.listen(2)
connection,address = listen_socket.accept()
request = connection.recv(1024)
connection.sendall("""HTTP/1.1 200 OK
Content-type:text/html

<html>
<body>
hello world
<body>
</html>""")
