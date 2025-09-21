# cache.py (for H2)
import socket

# In-memory cache store
cache = {}

def forward_request_to_server(request):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(("10.0.1.3", 8080))  # Connect to H3 (Server)
    server_socket.send(request)
    response = server_socket.recv(1024)
    server_socket.close()
    return response

def handle_get_request(request):
    try:
        key = request.split("=")[1].split(" ")[0]
        if key in cache:
            value = cache[key]
            response = "HTTP/1.1 200 OK\n\n{0}".format(value)
            print("Cache hit: Returning value from cache")
        else:
            print("Cache miss: Forwarding request to H3 (Server)")
            response = forward_request_to_server(request)
            if "200 OK" in response:
                value = response.split("\n\n")[1]
                cache[key] = value  # Store value in cache
    except Exception as e:
        response = "HTTP/1.1 400 Bad Request\n\nMalformed Request"
    return response

# Set up cache server
cache_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cache_socket.bind(("10.0.1.2", 8080))  # H2's IP address
cache_socket.listen(5)
print("Cache H2 listening on port 8080...")

# Handle client requests
while True:
    client_socket, addr = cache_socket.accept()
    print("Connection established with", addr)

    request = client_socket.recv(1024)
    print("Request received:", request)

    if request.startswith("GET"):
        response = handle_get_request(request)
    else:
        response = "HTTP/1.1 400 Bad Request\n\nInvalid HTTP Method"

    client_socket.send(response)
    client_socket.close()