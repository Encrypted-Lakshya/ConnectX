import streamlit as st
from twilio.rest import Client
from instagrapi import Client as insta
import smtplib
from email.message import EmailMessage
import pywhatkit as whatsapp
from linkedin_api import Linkedin
import tempfile
import pyttsx3

# ------------------------------
# Text-to-Speech Engine
# ------------------------------
def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()

# ------------------------------
# Callable functions
# ------------------------------

def send_email():
    st.subheader("📧 Send Email")
    with st.form(key="email_form"):
        email_sender = st.text_input("Enter your Gmail address:")
        email_password = st.text_input("Enter your App Password:", type="password")
        email_receiver = st.text_input("Enter receiver's email:")

        subject = st.text_input("Subject:")
        body = st.text_area("Message Body:")

        submit_email = st.form_submit_button("📤 Send Email")
        if submit_email:
            if not (email_sender and email_password and email_receiver and subject and body):
                st.warning("⚠️ Please fill in all fields.")
                speak_text("Please fill in all fields.")
            else:
                try:
                    msg = EmailMessage()
                    msg['From'] = email_sender
                    msg['To'] = email_receiver
                    msg['Subject'] = subject
                    msg.set_content(body)

                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                        smtp.login(email_sender, email_password)
                        smtp.send_message(msg)

                    st.success("✅ Email sent successfully!")
                    speak_text("Email sent successfully")
                    st.code(f"To: {email_receiver}\nSubject: {subject}")
                except Exception as e:
                    st.error(f"❌ Failed to send email: {e}")
                    speak_text("Failed to send email")

def get_twilio_info():
    st.subheader("🔐 Twilio Credentials")
    with st.form(key="twilio_form"):
        account_sid = st.text_input("Enter your Twilio Account SID:")
        auth_token = st.text_input("Enter your Twilio Authentication Token:", type="password")
        submit_twilio = st.form_submit_button("🔐 Save Credentials")
        if submit_twilio and account_sid and auth_token:
            return Client(account_sid, auth_token)
    return None

def send_sms():
    client = get_twilio_info()
    if client:
        st.subheader("📱 Send SMS")
        with st.form(key="sms_form"):
            from_number = st.text_input("Enter your Twilio phone number:")
            to_number = st.text_input("Enter the recipient's phone number:")
            sms_body = st.text_input("Enter the message you want to send:")
            submit_sms = st.form_submit_button("Send SMS")

            if submit_sms:
                if not from_number or not to_number or not sms_body:
                    st.warning("⚠️ Please fill in all fields.")
                    speak_text("Please fill in all fields.")
                else:
                    try:
                        message = client.messages.create(
                            body=sms_body,
                            from_=from_number,
                            to=to_number
                        )
                        st.success("📱 SMS sent successfully!")
                        speak_text("SMS sent successfully")
                        st.code(f"SID: {message.sid}")
                    except Exception as e:
                        st.error(f"❌ Failed to send SMS: {e}")
                        speak_text("Failed to send SMS")

def make_voice_call():
    client = get_twilio_info()
    if client:
        st.subheader("☎️ Place a Call")
        with st.form(key="call_form"):
            from_number = st.text_input("Your Twilio Phone Number:")
            to_number = st.text_input("Recipient Phone Number:")
            call_message = st.text_area("Message to Speak During the Call:")
            submit_call = st.form_submit_button("📞 Make Call")

            if submit_call:
                if not from_number or not to_number or not call_message:
                    st.warning("⚠️ Please fill in all fields.")
                    speak_text("Please fill in all fields.")
                else:
                    try:
                        call = client.calls.create(
                            to=to_number,
                            from_=from_number,
                            twiml=f"<Response><Say>{call_message}</Say></Response>"
                        )
                        st.success("✅ Call initiated successfully!")
                        speak_text("Call initiated successfully")
                        st.code(f"Call SID: {call.sid}")
                    except Exception as e:
                        st.error(f"❌ Failed to place the call: {e}")
                        speak_text("Failed to place the call")

def send_whatsapp_message():
    st.subheader("💬 Send WhatsApp Message")
    with st.form(key="whatsapp_form"):
        phone = st.text_input("📱 Enter receiver's number (with country code):")
        message = st.text_input("💬 Enter the message text:")
        hour = st.number_input("🕐 Hour (24-hour format):", min_value=0, max_value=23)
        minute = st.number_input("🕒 Minute:", min_value=0, max_value=59)
        submit_whatsapp = st.form_submit_button("📤 Send Message")

        if submit_whatsapp:
            if not phone or not message:
                st.warning("⚠️ Please fill in all fields.")
                speak_text("Please fill in all fields.")
            else:
                try:
                    whatsapp.sendwhatmsg(
                        phone_no=phone,
                        message=message,
                        time_hour=int(hour),
                        time_min=int(minute)
                    )
                    st.success("✅ WhatsApp message scheduled successfully!")
                    speak_text("WhatsApp message scheduled successfully")
                except Exception as e:
                    st.error(f"❌ Failed to send message: {e}")
                    speak_text("Failed to send WhatsApp message")

def post_to_instagram():
    st.subheader("📸 Post to Instagram")
    with st.form(key="instagram_form"):
        username = st.text_input("Enter your Instagram Username:")
        password = st.text_input("Enter your Instagram Password:", type="password")
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
        caption = st.text_area("Enter Caption:")
        submit_ig = st.form_submit_button("📤 Post to Instagram")

        if submit_ig:
            if not username or not password:
                st.error("❌ Please enter your Instagram credentials.")
                speak_text("Please enter your Instagram credentials")
            elif uploaded_file is None:
                st.error("❌ Please upload an image.")
                speak_text("Please upload an image")
            elif not caption:
                st.error("❌ Please enter a caption.")
                speak_text("Please enter a caption")
            else:
                try:
                    cl = insta()
                    cl.login(username, password)
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
                        tmp_file.write(uploaded_file.read())
                        tmp_file_path = tmp_file.name
                    cl.photo_upload(tmp_file_path, caption)
                    st.success("✅ Successfully posted to Instagram!")
                    speak_text("Successfully posted to Instagram")
                except Exception as e:
                    st.error(f"❌ Error: {e}")
                    speak_text("Failed to post to Instagram")

def post_to_linkedin():
    st.subheader("🔗 Post to LinkedIn")
    with st.form(key="linkedin_form"):
        username = st.text_input("Enter your LinkedIn Email:")
        password = st.text_input("Enter your LinkedIn Password:", type="password")
        post_text = st.text_area("Write your post:")
        submit_ln = st.form_submit_button("📤 Post to LinkedIn")

        if submit_ln:
            if not username or not password or not post_text:
                st.warning("⚠️ Please fill in all fields.")
                speak_text("Please fill in all fields")
            else:
                try:
                    api = Linkedin(username, password)
                    my_profile = api.get_profile()
                    urn = my_profile["entityUrn"].split(":")[-1]
                    response = api.submit_share(
                        author_urn=f"urn:li:person:{urn}",
                        text=post_text
                    )
                    st.success("✅ Post uploaded successfully!")
                    speak_text("Post uploaded successfully")
                    st.code(str(response))
                except Exception as e:
                    st.error(f"❌ Failed to post: {e}")
                    speak_text("Failed to post to LinkedIn")

# ------------------------------
# Streamlit Interface
# ------------------------------

st.set_page_config(page_title="ConnectX", layout="centered")
st.title("📲 ConnectX")
speak_text("Welcome to ConnectX.")
st.write("Select a communication task from the dropdown menu below:")

task = st.selectbox("Choose an action:", [
    "Send Email",
    "Send SMS",
    "Make Voice Call",
    "Send WhatsApp Message",
    "Post on Instagram",
    "Post on LinkedIn"
])
speak_text("Select a communication task from the dropdown menu below.")

if task == "Send Email":
    send_email()
elif task == "Send SMS":
    send_sms()
elif task == "Make Voice Call":
    make_voice_call()
elif task == "Send WhatsApp Message":
    send_whatsapp_message()
elif task == "Post on Instagram":
    post_to_instagram()
elif task == "Post on LinkedIn":
    post_to_linkedin()
