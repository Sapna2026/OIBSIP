"""
OIBSIP Task 5: Real-Time Chat Application
Run this server before starting any clients.
"""
import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"  # localhost; use "0.0.0.0" for LAN access
PORT = 5000
clients = {}  # socket -> username
lock = threading.Lock()


def timestamp():
    return datetime.now().strftime("%H:%M")


def broadcast(message, exclude=None):
    """Send a message to all connected clients except an optional socket."""
    with lock:
        recipients = list(clients.keys())

    for client in recipients:
        if client is exclude:
            continue
        try:
            client.sendall((message + "\n").encode("utf-8"))
        except OSError:
            # The client handler will remove disconnected clients.
            pass


def handle_client(client, address):
    username = "Guest"
    try:
        client.sendall(b"Enter your username: ")
        username = client.recv(1024).decode("utf-8").strip() or "Guest"

        with lock:
            clients[client] = username

        broadcast(f"[{timestamp()}] * {username} joined the chat *")
        client.sendall(
            f"[{timestamp()}] * Welcome, {username}! Type /quit to leave. *\n".encode("utf-8")
        )

        buffer = ""
        while True:
            data = client.recv(1024)
            if not data:
                break

            buffer += data.decode("utf-8", errors="replace")
            while "\n" in buffer:
                message, buffer = buffer.split("\n", 1)
                message = message.strip()
                if not message:
                    continue
                if message.lower() == "/quit":
                    return
                broadcast(f"[{timestamp()}] {username}: {message}")

    except (ConnectionError, OSError):
        pass
    finally:
        with lock:
            existed = clients.pop(client, None) is not None
        try:
            client.close()
        except OSError:
            pass
        if existed:
            broadcast(f"[{timestamp()}] * {username} disconnected *")


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Chat server listening on {HOST}:{PORT}")
    print("Press Ctrl+C to stop the server.")

    try:
        while True:
            client, address = server.accept()
            print(f"Connection from {address}")
            threading.Thread(
                target=handle_client, args=(client, address), daemon=True
            ).start()
    except KeyboardInterrupt:
        print("\nStopping server...")
    finally:
        server.close()


if __name__ == "__main__":
    main()
