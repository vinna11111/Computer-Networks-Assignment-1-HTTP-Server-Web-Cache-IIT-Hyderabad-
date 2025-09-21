# server.py (for H3)
import socket

# In-memory key-value store
store = {
    "key1": "val1",
    "key2": "val2",
    "key3": "val3",
    "key4": "val4",
    "key5": "val5",
    "key6": "val6"
}

def handle_get_request(request):
    try:
        key = request.split("=")[1].split(" ")[0]
        value = store.get(key, None)
        if value:
            response = "HTTP/1.1 200 OK\n\n{0}".format(value)
        else:
            response = "HTTP/1.1 404 Not Found\n\nKey not found"
    except Exception as e:
        response = "HTTP/1.1 400 Bad Request\n\nMalformed Request"
    return response

# Set up server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("10.0.1.3", 8080))  # H3's IP address
server_socket.listen(5)
print("Server H3 listening on port 8080...")

# Handle client requests
while True:
    client_socket, addr = server_socket.accept()
    print("Connection established with", addr)

    request = client_socket.recv(1024)
    print("Request received:", request)

    if request.startswith("GET"):
        response = handle_get_request(request)
    else:
        response = "HTTP/1.1 400 Bad Request\n\nInvalid HTTP Method"

    client_socket.send(response)
    client_socket.close()