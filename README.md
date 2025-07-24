# 🗣️ Whisper Meeting Minutes Bot

An AI-powered bot that transcribes meeting audio, summarizes the key points, and generates structured meeting minutes automatically using OpenAI Whisper and GPT models.

---

## 📌 Features

- 🎤 **Audio Transcription** using OpenAI Whisper
- 🧠 **Summary Generation** using GPT
- 📝 **Automated Meeting Minutes** output
- 📂 Upload and manage audio files easily
- 🌐 `.env` based API key configuration

---

## 🛠️ Technologies Used

- Python
- OpenAI Whisper
- OpenAI GPT
- Python `dotenv`
- `pydub`, `speech_recognition`, and `whisper` libraries

---

## 📁 Folder Structure

```
whisper-meeting-minutes-bot/
│
├── transcriber.py         # Whisper transcription logic
├── summarizer.py          # GPT-based summary generation
├── app.py                 # Main CLI interface
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variable template
├── LICENSE                # MIT License
└── README.md              # Project documentation
```

---

## ⚙️ Setup & Run Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Vsandeep-ai-dev/whisper-meeting-minutes-bot.git
cd whisper-meeting-minutes-bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your API key

Create a `.env` file like this:

```
OPENAI_API_KEY=your_openai_key_here
```

Or copy the template:

```bash
cp .env.example .env
```

### 4. Run the bot

```bash
python app.py
```

---

## ✅ Example Workflow

1. Upload or record a meeting `.mp3` or `.wav` file  
2. The bot transcribes using Whisper  
3. It summarizes using GPT  
4. Outputs structured minutes in plain text

---

## 🧠 Future Improvements

- GUI with drag-and-drop interface
- Email integration for automatic sending
- Multi-language transcription support
- Live meeting capture

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

## 👨‍💻 Author

Sandeep Reddy – [@Vsandeep-ai-dev](https://github.com/Vsandeep-ai-dev)
