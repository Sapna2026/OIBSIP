# 💬 Real-Time Chat Application using Python

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Networking-TCP-orange" />
  <img src="https://img.shields.io/badge/Concurrency-Threading-green" />
  <img src="https://img.shields.io/badge/Internship-OIBSIP-purple" />
</p>

## 📌 Project Overview

This project is a real-time chat application developed using Python socket programming and multithreading.

It allows multiple users to connect to a central server and exchange messages instantly. The server manages client connections and broadcasts messages to connected users.

This project was developed as **Task 5 — Chat Application** for the Oasis Infobyte Python Programming Internship (OIBSIP).

## 🎯 Objectives

- Understand client-server architecture.
- Implement TCP socket communication.
- Enable real-time messaging between users.
- Handle multiple clients using threading.
- Display messages with timestamps.
- Manage client disconnections gracefully.

## ✨ Features

- Real-time bidirectional communication.
- Multiple users can join the chat.
- Username-based messaging.
- Timestamped messages.
- Automatic join and disconnect notifications.
- Graceful disconnection using `/quit`.
- Localhost communication.
- Lightweight implementation without external libraries.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Socket | Network communication |
| Threading | Concurrent client handling |
| TCP/IP | Reliable communication protocol |
| datetime | Message timestamps |

## 📂 Project Structure

```text
Task-5-Chat-Application/
│
├── server.py       # Chat server
├── client.py       # Chat client
└── README.md       # Project documentation
```

## ⚙️ Installation

### Prerequisites

- Python 3.8 or higher
- Visual Studio Code or any Python editor
- Basic knowledge of terminal commands

Check Python installation:

```bash
python --version
```

No additional Python packages are required.

## 🚀 How to Run

### Step 1: Clone the repository

```bash
git clone https://github.com/Sapna2026/OIBSIP.git
```

### Step 2: Navigate to the project folder

```bash
cd OIBSIP/Task-5-Chat-Application
```

### Step 3: Start the server

Open the first terminal:

```bash
python server.py
```

Expected output:

```text
Chat server listening on 127.0.0.1:5000
Press Ctrl+C to stop the server.
```

### Step 4: Start the first client

Open a second terminal:

```bash
python client.py
```

Enter a username:

```text
Enter your username: Alice
```

### Step 5: Start another client

Open a third terminal:

```bash
python client.py
```

Enter another username:

```text
Enter your username: Bob
```

Now both users can communicate in real time.

### Step 6: Disconnect

Type the following command in the client terminal:

```text
/quit
```

The server will notify the remaining connected users.

## 💻 Example Output

**Alice's terminal**

```text
Enter your username: Alice

[14:35] * Welcome, Alice! *
[14:35] Alice: Hello everyone!
[14:36] Bob: Hi Alice!
```

**Bob's terminal**

```text
Enter your username: Bob

[14:35] * Welcome, Bob! *
[14:35] Alice: Hello everyone!
[14:36] Bob: Hi Alice!
```

## 🔍 How It Works

1. The server creates a TCP socket and listens for incoming connections.
2. Each client connects to the server using localhost.
3. The server requests a username from the client.
4. A separate thread handles each connected client.
5. When a client sends a message, the server broadcasts it to connected users.
6. Messages are displayed with timestamps.
7. When a client disconnects, the server announces the disconnection.

## 🔐 Security and Privacy

This project is an educational demonstration of socket programming.

- Messages are transmitted over TCP without encryption.
- The server can read all messages sent through it.
- End-to-end encryption is not implemented.
- User authentication is not implemented.
- Messages are not stored in a database or persistent file.
- The application is configured for localhost communication.

**Important:** Do not use this application to transmit sensitive information or expose it directly to the public internet.

## 📚 Learning Outcomes

By completing this project, I gained practical experience in:

- Python socket programming.
- TCP client-server communication.
- Multithreading and concurrency.
- Real-time data exchange.
- Network connection management.
- Error handling and graceful disconnection.

## 🔮 Future Improvements

- GUI chat interface using Tkinter.
- User registration and login.
- Multiple chat rooms.
- SQLite message history.
- Emoji support.
- Desktop notifications.
- Secure communication using TLS.

## 👩‍💻 Author

**Sapana Yadav**

Aspiring Python Developer | Aspiring Data Analyst

- GitHub: [Sapna2026](https://github.com/Sapna2026)
- LinkedIn: [Sapana Yadav](https://www.linkedin.com/in/sapana-yadav-a2171441b/)

## 🏢 Internship

**Oasis Infobyte — OIBSIP**

Track: Python Programming  
Task: 5 — Chat Application

---

⭐ If you find this project useful, feel free to explore the repository and share your feedback!
