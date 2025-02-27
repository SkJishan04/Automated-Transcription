# **Automated Transcription System**

## **📌 Overview**
The **Automated Transcription System** is a Python-based tool that uses **OpenAI's Whisper model** to automatically transcribe audio and video files. It continuously monitors a specified folder for new media files and transcribes them in real-time. The system also maintains a session log to prevent duplicate processing.

## **🛠 Tech Stack**
- **Python** – Core scripting and automation
- **Whisper AI** – Speech-to-text transcription
- **Watchdog** – Real-time folder monitoring
- **JSON** – Session tracking for processed files
- **OS Module** – File handling and directory management

## **✨ Features**
✅ **Automatic Transcription** – Converts speech in audio/video files to text
✅ **Real-time Folder Monitoring** – Detects new files and processes them instantly
✅ **Session Management** – Avoids duplicate processing using a session log
✅ **Supports Multiple Formats** – Works with `.mp3`, `.wav`, `.mp4`, `.mkv`, `.mov`, `.flv`, `.aac`, and `.m4a`
✅ **Lightweight & Fast** – Runs efficiently without manual intervention

## **🚀 Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/automated-transcription.git
cd automated-transcription
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Download the Whisper Model**
```python
import whisper
model = whisper.load_model("base")
```

### **4️⃣ Configure the System**
Edit `config.py` to set your **watch directory**:
```python
WATCH_DIRECTORY = r"C:\Users\YourName\Desktop\MediaFiles"
```

### **5️⃣ Run the System**
```bash
python main.py
```

## **📂 Project Structure**
```
├── transcriber.py        # Handles transcription using Whisper AI
├── monitor.py           # Monitors folder and triggers transcription
├── session_manager.py   # Tracks processed files to avoid duplication
├── config.py            # Configuration settings (watch directory, formats)
├── main.py              # Entry point for scanning and monitoring
├── session.json         # Stores processed file logs
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation
```

## **🎥 How It Works**
1️⃣ **Scans for existing files** in the monitored folder and transcribes them.
2️⃣ **Starts live monitoring** for new files.
3️⃣ **Transcribes new files** automatically when added to the folder.
4️⃣ **Saves transcriptions** as text files next to the original media files.
5️⃣ **Prevents re-processing** using a session log (`session.json`).

## **📝 Example Usage**
1. Add an `.mp3` or `.mp4` file to the media folder.
2. The system detects it and transcribes the speech.
3. A `.txt` file with the transcription is saved alongside the media file.
4. If you add the same file again, it will be skipped.

## **⚡ Future Enhancements**
- 🔹 **Multi-language support**
- 🔹 **Web-based UI for transcription preview**
- 🔹 **Cloud storage integration (Google Drive, AWS S3)**
- 🔹 **Error handling for corrupted files**

## **🙌 Contribution**
Feel free to contribute by opening issues or submitting pull requests! 😊

## **📄 License**
This project is licensed under the **MIT License**.

---

⭐ **If you found this project useful, give it a star on GitHub!** ⭐

