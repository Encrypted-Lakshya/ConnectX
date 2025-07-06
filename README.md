# ConnectX

ConnectX is a multi-channel communication tool built with **Streamlit** that lets you:

- 📧 Send Emails
- 📱 Send SMS via Twilio
- ☎️ Make Voice Calls
- 💬 Send WhatsApp Messages
- 📸 Post to Instagram
- 🔗 Post to LinkedIn
- 🎙️ Text-to-Speech notifications

## 🔊 New Feature: Text-to-Speech (TTS)
- The app uses **pyttsx3** to provide voice feedback:
  - At the start of the app
  - After each task (success/failure)
  - When required fields are missing

This enhances accessibility and makes interactions more intuitive.

## 🛠 Technologies Used
- Python
- Streamlit
- Twilio API
- pyttsx3 (TTS engine)
- pywhatkit
- instagrapi
- linkedin-api

## ⚙️ Features
- Simple, clean Streamlit interface
- Real-time form validation and feedback
- Secure credential handling (via Streamlit forms)
- TTS alerts for all tasks

## 📦 How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🔐 Notes
- For Email: Use **Gmail App Password**
- For Instagram: You may need to enable less secure apps or use a session
- For LinkedIn: This uses a community-maintained API and may have limitations

## 📄 License
MIT

---
Feel free to contribute or suggest improvements!
