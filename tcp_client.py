'Objective: Create a simple chatroom which can only be used in local machine'
import socket
import threading

HOST = '127.0.0.1'#ip address specifically for your own computer
PORT = 12345#Diffent ports are for diffent applications. 
'''
0-1023: Reserved for standard services
1024-49151: Assigned to applications 
49152-65535: Temporary/ephemeral use 
'''

#Write a function to continuously receive information from the server
def receive(sock):
    while True:
        try:
            message = sock.recv(1024).decode()#sock.recv(1024) blocks waiting for up to 1024 bytes; .decode() converts bytes → text 
            if not message:
                break
            print(message, flush = True)#flush=True tells Python to immediately send output to the screen instead of storing it in a buffer.
        except Exception:
            print("Disconnected from the server.")
            break

#Connect to the server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#AF_INET: ipv4, SOCK_STREAM: tcp
sock.connect(HOST, PORT)#Establish connection to the server.
print(f"Connected to {HOST}: {PORT}")

#background thread: receive messages when we type
threading.Thread(target = receive, args = (sock,), daemon = True)
'''
target = receive: Specify which function the thread should execute
args = (sock,): specify the parameter assigned to the targeted function. Because the type of args is tuple, so we assign a tuple of one element
daemon = True: Thread dies when main program exits
daemon = False: Program waits for thread to finish before exiting
'''

#Main loop:
while True:
    try:
        msg = input()
        sock.send(msg.encode())
    except (KeyboardInterrupt, EOFError):
        print("\nleaving chat.")
        sock.close()
        break
    