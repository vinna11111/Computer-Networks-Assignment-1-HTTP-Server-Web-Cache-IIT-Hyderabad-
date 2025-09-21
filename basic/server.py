import socket

# Set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("10.0.1.2", 8080))
server_socket.listen(5)
print("Server listening on port 8080...")

# In-memory key-value store
store = {}

def handle_get_request(request):
    part_after_equals = request.split("=")[1]
        # Extract the key before the space
    key = part_after_equals.split(" ")[0]
    value = store.get(key, None)
    if value:
        response = "HTTP/1.1 200 OK\n\n{0}".format(value)
    else:
        response = "HTTP/1.1 404 Not Found\n\nKey not found"
    return response

def handle_put_request(request):
    parts = request.split("/")
    key = parts[2]
    value = parts[3].split(" ")[0]  # Extract key and value
    store[key] = value
    response = "HTTP/1.1 200 OK\n\nKey-Value stored successfully"
    return response

def handle_delete_request(request):
    key = request.split("/")[2].split(" ")[0]
    if key in store:
        del store[key]
        response = "HTTP/1.1 200 OK\n\nKey-Value pair deleted successfully"
    else:
        response = "HTTP/1.1 404 Not Found\n\nKey not found"
    return response

# Handle client requests
while True:
    client_socket, addr = server_socket.accept()
    print("Connection established with", addr)
    
    request = client_socket.recv(1024).decode()
    print("Request received:", request)
    
    if request.startswith("GET"):
        response = handle_get_request(request)
    elif request.startswith("PUT"):
        response = handle_put_request(request)
    elif request.startswith("DELETE"):
        response = handle_delete_request(request)
    else:
        response = "HTTP/1.1 400 Bad Request\n\nInvalid HTTP Method"
    
    client_socket.send(response.encode())
    client_socket.close()