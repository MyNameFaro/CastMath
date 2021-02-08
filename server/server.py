import socket
import json
import threading
import seeker

SERVER_IP = "192.168.43.210"
PORT = 3000

BUFFER = 1024

clients = []

def service(client , address) :
    while True:
        recv = json.loads(client.recv(BUFFER).decode('utf-8'))
        if not data :
            clients.remove(client)
            break
        method = {
            "position"
        }
        send = pages[page]() 
        for c in clients :
            c.sendall(json.dumps(send).encode('utf-8'))

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
    