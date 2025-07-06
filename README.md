# 📲 ConnectX

**ConnectX** is a powerful and beginner-friendly **Streamlit-based application** that allows you to communicate across multiple platforms — including **Email, SMS, WhatsApp, Instagram, LinkedIn**, and **Voice Calls** — all from one unified dashboard.

## 🚀 Features

* 📧 Send Emails using Gmail and SMTP
* 📱 Send SMS using Twilio
* ☎️ Make Voice Calls using Twilio
* 💬 Send WhatsApp messages using `pywhatkit`
* 📸 Post images to Instagram with caption
* 🔗 Publish LinkedIn text posts
* 🎙️ Get real-time voice feedback with Text-to-Speech (TTS)

## 🛠️ Tech Stack

* Python 3.10+
* [Streamlit](https://streamlit.io)
* [Twilio](https://www.twilio.com)
* [pyttsx3](https://pypi.org/project/pyttsx3/) for Text-to-Speech
* [pywhatkit](https://pypi.org/project/pywhatkit/)
* [instagrapi](https://github.com/adw0rd/instagrapi)
* [linkedin-api](https://github.com/tomquirk/linkedin-api)

## ⚙️ Installation

```bash
# Clone this repository
git clone https://github.com/yourusername/multi-channel-communicator.git
cd multi-channel-communicator

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## ▶️ Run the App

```bash
streamlit run Task.py
```

## 🔐 Requirements

### Email

* Gmail account
* App password (for 2FA enabled accounts)

### Twilio

* Twilio account with verified phone number
* Account SID & Auth Token

### Instagram

* Valid Instagram credentials

### WhatsApp

* WhatsApp Web must be logged in on your browser

### LinkedIn

* LinkedIn username & password

## 📁 File Structure

```bash
multi-channel-communicator/
├── Task.py           # Main Streamlit app
├── README.md         # You're reading it 😁
└── requirements.txt  # Required Python packages
```

## 🧪 Example Use-Cases

* One-click digital marketing
* Personal multi-platform broadcast
* Send scheduled reminders to clients or students
* Share media posts across platforms easily
* Make your application more accessible with TTS-enabled feedback

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

## 🛡️ License

[MIT](https://choosealicense.com/licenses/mit/)

---

> Made with ❤️ by Lakshya Rohra
