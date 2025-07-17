## Slowloris Attack

## The core concept of this attack is to create multiple sockets, sending some parts of header to the server and thereby never completing a HTTP request. This occupies the server's connection pool hence denying all other legit reqests coming to the server.

### For executing the file, git clone the repo and configure the ip and port. Then, 
python3 slowlor.py
