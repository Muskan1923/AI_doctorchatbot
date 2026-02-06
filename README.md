# AI_doctorchatbot
# 🩺 AI Doctor Voice Chatbot

An AI-powered Doctor Voice Assistant that allows users to speak, upload medical images, and receive intelligent health-related responses using advanced AI models.

---

## 🚀 Features
- 🎤 Voice Input (Speech-to-Text using Groq Whisper)
- 🖼️ Medical Image Analysis
- 🧠 AI-based Doctor Reasoning
- 🌐 Gradio Web Interface
- ⚡ Fast local deployment

---

## 🧩 Tech Stack
- Python 3.12
- Gradio
- Groq API (Whisper)
- OpenAI Vision / LLM
- Pygame
- python-dotenv

---

## 📁 Project Structure
ai_doctor_voicebot/
├── gradio_app.py
├── voice_of_patient.py
├── brain.py
├── .env
├── requirements.txt
└── README.md

---

## 🔑 Environment Setup
Create a `.env` file in the project root:

GROQ_API_KEY=your_groq_api_key_here  
OPENAI_API_KEY=your_openai_api_key_here

⚠️ Do not upload `.env` to GitHub.

---

## ▶️ How to Run
pip install -r requirements.txt  
python gradio_app.py

Open in browser:
http://127.0.0.1:7860

---

## 🧠 How It Works
1. User speaks → audio captured
2. Groq Whisper converts audio to text
3. Optional medical image is encoded
4. Text + image sent to AI model
5. AI generates a doctor-style response
6. Response shown in Gradio UI

---

## 🛡️ Disclaimer
This project is for educational purposes only and does not replace professional medical advice.

---

## 👨‍💻 Author
Muskan Jhala  
B.Tech – Artificial Intelligence & Data Science


