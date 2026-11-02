# 🎙️ Python Voice Assistant

A beginner-friendly voice assistant built with Python that listens to voice commands, responds with spoken audio, and performs useful desktop tasks such as web searching and opening websites.

The project uses speech recognition to understand user commands and text-to-speech technology to make the assistant respond aloud instead of only displaying text.

## ✨ Features

- **Voice Input:** Listens to commands through the microphone.
- **Voice Output:** Speaks responses using Windows SAPI5 and `pyttsx3`.
- **Speech Recognition:** Converts spoken words into text.
- **Google Search:** Opens Google search results for a spoken topic.
- **YouTube Search:** Searches YouTube for videos.
- **Website Launcher:** Opens supported websites such as Google, YouTube, Gmail, GitHub, and LinkedIn.
- **Time and Date:** Announces the current time and date.
- **Command Handling:** Responds to greetings and recognizes the goodbye command.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| SpeechRecognition | Converts speech into text |
| PyAudioWPatch | Microphone audio input |
| pyttsx3 | Text-to-speech output |
| Windows SAPI5 | Windows speech engine |
| Web Browser | Opens websites and search results |

## 📁 Project Structure

```text
Voice-Assistant/
│
├── assistant.py
├── README.md
└── requirements.txt
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

Replace `YOUR_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Navigate to the project folder

```bash
cd Voice-Assistant
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install SpeechRecognition pyttsx3 PyAudioWPatch requests
```

## ▶️ How to Run

Run the following command in the terminal:

```bash
python assistant.py
```

When the assistant starts, speak clearly into your microphone.

## 🗣️ Example Voice Commands

| Voice Command | Assistant Action |
|---|---|
| "Hello" | Responds with a greeting |
| "What is the time?" | Announces the current time |
| "What is the date?" | Announces the current date |
| "Search for Python tutorials" | Opens Google search results |
| "Search YouTube for Python tutorials" | Opens YouTube search results |
| "Open Gmail" | Opens Gmail in the browser |
| "Open GitHub" | Opens GitHub in the browser |
| "Goodbye" | Stops the assistant |

## 🔊 Voice Output

The assistant uses `pyttsx3` with the Windows SAPI5 speech engine to generate spoken responses.

This allows the assistant to speak without relying on an online text-to-speech service.

Speech recognition uses Google's recognition service through the SpeechRecognition library and requires an internet connection.

## 🚀 Future Improvements

Planned enhancements for the project:

- AI-powered conversational responses
- Email sending with user confirmation
- Weather information
- Reminders and alarms
- More advanced voice command handling
- Improved error handling and microphone selection
- A graphical user interface

These are planned improvements and are not currently included in the basic version.

## 📌 Learning Outcomes

Through this project, I practiced:

- Python functions and modules
- Speech recognition and audio processing
- Text-to-speech implementation
- Handling user input through voice
- Working with external libraries
- Opening websites programmatically
- Building a practical Python application

## 👩‍💻 Author

**Sapana Yadav**

Aspiring Data Analyst | Python • SQL • Excel • Power BI

- GitHub: [Sapna2026](https://github.com/Sapna2026)
- LinkedIn: [Sapana Yadav](https://www.linkedin.com/in/sapana-yadav-a2171441b/)

---

⭐ If you find this project useful, feel free to explore the repository and share your feedback.
