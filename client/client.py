import socket
import json
import threading 

SERVER_IP = "192.168.43.210"
PORT = 3000
BUFFER = 1024

def update(server) :
    while True :
        server_data = json.loads(server.recv(BUFFER).decode('utf-8'))
        if not server_data:
            break
        print(server_data['username'] + " : " + server_data['message'])
    
    server.close()

    

def main() :
    try :
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect((SERVER_IP , PORT))
    except :
        print("Internet Fail")
    username = input("USERNAME : ")

    ud = threading.Thread(target = update, args = [server])
    ud.start()

    while True:
        message = input("PRESS MESSAGE : ")
        data = {"username" : username , "message" : message}
        try :
            server.send(json.dumps(data).encode('utf-8'))
        except :
            print("Sorry Sending Fail")
    server.close()
    
main()