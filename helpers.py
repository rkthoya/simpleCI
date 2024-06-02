import socket

def communicate(host, port, request):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    request_bytes = request.encode()
    s.send(request_bytes)
    response = s.recv(1024)
    s.close()
    return response