import socket
import pickle
import threading
import seeker
import pygame

SERVER_IP = "192.168.43.175"
PORT = 3000

BUFFER = 4096

clients = []

seeker = pygame.sprite.Group()

    
    ############INIT

def service(client , address) :
    while True:
        recv = pickle.loads(client.recv(BUFFER))
        if not data :
            clients.remove(client)
            break
        for c in clients :
            c.sendall(pickle.dumps(recv))

    client.close()

def main() :
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server.bind((SERVER_IP , PORT))
    server.listen()
    while True:
        client , address = server.accept()
        clients.append(client)
        sv = threading.Thread(target = service, args = [client, address])
        sv.start()
    server.close()

main()
    