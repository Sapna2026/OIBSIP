"""
OIBSIP Task 5: Real-Time Chat Application
Run this client in a separate terminal for each participant.
"""
import socket
import threading

HOST = "127.0.0.1"
PORT = 5000


def receive_messages(sock):
    """Continuously receive and display messages from the server."""
    try:
        while True:
            data = sock.recv(4096)
            if not data:
                print("\nServer closed the connection.")
                break
            print(data.decode("utf-8", errors="replace"), end="", flush=True)
    except (ConnectionError, OSError):
        print("\nDisconnected from the server.")


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
        # Username prompt is sent by the server without a newline.
        prompt = client.recv(1024).decode("utf-8", errors="replace")
        username = input(prompt)
        client.sendall((username.strip() or "Guest").encode("utf-8"))

        threading.Thread(target=receive_messages, args=(client,), daemon=True).start()
        print("You are connected. Type a message; use /quit to exit.")

        while True:
            message = input()
            client.sendall((message + "\n").encode("utf-8"))
            if message.strip().lower() == "/quit":
                break

    except (ConnectionError, OSError) as error:
        print(f"Could not connect: {error}")
        print("Check that server.py is running.")
    except KeyboardInterrupt:
        try:
            client.sendall(b"/quit\n")
        except OSError:
            pass
    finally:
        client.close()


if __name__ == "__main__":
    main()
