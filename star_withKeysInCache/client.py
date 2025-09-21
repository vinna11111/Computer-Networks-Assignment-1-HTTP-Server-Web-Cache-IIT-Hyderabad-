# client.py (for H1)
import socket
import time

def send_request(request):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("10.0.1.2", 8080))  # Connect to H2 (Cache)
    client_socket.send(request)

    response = client_socket.recv(1024)
    print("Response from server:", response)

    client_socket.close()

# Example GET request for key1
get_request = "GET /assignment1?key=key1 HTTP/1.1"
start_time = time.time()
send_request(get_request)
end_time = time.time()
print("Time taken:", end_time - start_time)

get_request = "GET /assignment1?key=key2 HTTP/1.1"
start_time = time.time()
send_request(get_request)
end_time = time.time()
print("Time taken:", end_time - start_time)

get_request = "GET /assignment1?key=key3 HTTP/1.1"
start_time = time.time()
send_request(get_request)
end_time = time.time()
print("Time taken:", end_time - start_time)

get_request = "GET /assignment1?key=key4 HTTP/1.1"
start_time = time.time()
send_request(get_request)
end_time = time.time()
print("Time taken:", end_time - start_time)

get_request = "GET /assignment1?key=key5 HTTP/1.1"
start_time = time.time()
send_request(get_request)
end_time = time.time()
print("Time taken:", end_time - start_time)

get_request = "GET /assignment1?key=key6 HTTP/1.1"
start_time = time.time()
send_request(get_request)
end_time = time.time()
print("Time taken:", end_time - start_time)