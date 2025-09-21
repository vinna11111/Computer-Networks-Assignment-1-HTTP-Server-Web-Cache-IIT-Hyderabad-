import socket
import time
def send_request(request):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("10.0.1.2", 8080))
    client_socket.send(request.encode())
    
    response = client_socket.recv(1024).decode()
    print("Response from server:", response)
    
    client_socket.close()

# Example usage of sending different requests

# PUT request
put_request1 = "PUT /assignment1/key1/val1 HTTP/1.1"
send_request(put_request1)
put_request2 = "PUT /assignment1/key2/val2 HTTP/1.1"
send_request(put_request2)

put_request3= "PUT /assignment1/key3/val3 HTTP/1.1"
send_request(put_request3)

put_request4 = "PUT /assignment1/key4/val4 HTTP/1.1"
send_request(put_request4)
put_request5 = "PUT /assignment1/key5/val5 HTTP/1.1"
send_request(put_request5)
put_request6 = "PUT /assignment1/key6/val6 HTTP/1.1"
send_request(put_request6)


# GET request
get_request = "GET /assignment1?request=key1 HTTP/1.1"
start_time = time.time()
send_request(get_request)
end_time = time.time()

print("Time taken:", end_time - start_time)
get_request = "GET /assignment1?request=key2 HTTP/1.1"
get_requestart_time = time.time()
send_request(get_request)
end_time = time.time()

print("Time taken:", end_time - start_time)
get_request = "GET /assignment1?request=key3 HTTP/1.1"
start_time = time.time()
send_request(get_request)
end_time = time.time()

print("Time taken:", end_time - start_time)
get_request = "GET /assignment1?request=key4 HTTP/1.1"
start_time = time.time()
send_request(get_request)
end_time = time.time()

print("Time taken:", end_time - start_time)
get_request = "GET /assignment1?request=key5 HTTP/1.1"
start_time = time.time()
send_request(get_request)
end_time = time.time()

print("Time taken:", end_time - start_time)
get_request = "GET /assignment1?request=key6 HTTP/1.1"
start_time = time.time()
send_request(get_request)
end_time = time.time()

print("Time taken:", end_time - start_time)


# DELETE request
delete_request = "DELETE /assignment1/key1 HTTP/1.1"
send_request(delete_request)
delete_request = "DELETE /assignment1/key2 HTTP/1.1"
send_request(delete_request)
delete_request = "DELETE /assignment1/key3 HTTP/1.1"
send_request(delete_request)
delete_request = "DELETE /assignment1/key4 HTTP/1.1"
send_request(delete_request)
delete_request = "DELETE /assignment1/key5 HTTP/1.1"
send_request(delete_request)
delete_request = "DELETE /assignment1/key6 HTTP/1.1"
send_request(delete_request)


