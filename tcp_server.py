import socket
import threading

HOST = "0.0.0.0"  # Listen on all network interfaces
PORT = 12345
clients = []      # Keep track of all connected client sockets

def broadcast(message, sender_conn=None):
    """Send a message to all clients except the sender."""
    for client in clients:
        if client != sender_conn:
            try:
                client.send(message)
            except Exception:
                clients.remove(client)

def handle_client(conn, addr):
    """Handle incoming messages from a single client in its own thread."""
    print(f"[+] {addr} connected")
    conn.send("Welcome to the chatroom!\n".encode())
    broadcast(f"[Server] {addr} has joined.\n".encode(), conn)

    while True:
        try:
            message = conn.recv(1024)   # Block until data is received
            if not message:             # Empty bytes = client disconnected
                break
            print(f"{addr}: {message.decode().strip()}")
            broadcast(f"{addr}: {message.decode()}".encode(), conn)
        except Exception:
            break

    # Cleanup on disconnect
    print(f"[-] {addr} disconnected")
    clients.remove(conn)
    broadcast(f"[Server] {addr} has left.\n".encode())
    conn.close()

# --- Server setup ---
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # Create a TCP socket
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow port reuse after restart
server.bind((HOST, PORT))
server.listen()  # Start listening for incoming connections
print(f"TCP server listening on {HOST}:{PORT}")

# Main loop: accept new connections and spawn a thread for each
while True:
    conn, addr = server.accept()  # Block until a client connects
    clients.append(conn)
    threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
