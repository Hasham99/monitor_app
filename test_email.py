import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load your .env file
load_dotenv()

GMAIL_USER = os.getenv('GMAIL_USER')
# IF THIS FAILS, HARDCODE THE PASSWORD HERE TO TEST:
# GMAIL_PASSWORD = "huzq xquo dcpx slqp" 
GMAIL_PASSWORD = os.getenv('GMAIL_PASSWORD')
ALERT_RECIPIENT = os.getenv('ALERT_RECIPIENT')

print(f"1. User: {GMAIL_USER}")
print(f"2. Recipient: {ALERT_RECIPIENT}")
print(f"3. Password Length: {len(GMAIL_PASSWORD) if GMAIL_PASSWORD else 'None'}")

msg = MIMEText("This is a test email from your Python script.")
msg['Subject'] = "Test Email Connection"
msg['From'] = GMAIL_USER
msg['To'] = ALERT_RECIPIENT

try:
    print("\n4. Connecting to smtp.gmail.com:465...")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        print("5. Connected. Logging in...")
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        print("6. Logged in. Sending message...")
        server.send_message(msg)
        print("7. SUCCESS! Email sent.")
except Exception as e:
    print(f"\n❌ FAILURE: {e}")
    # Common error hints
    if "Timeout" in str(e):
        print(">> HINT: Your Antivirus or Firewall is blocking Python.")
    if "Username and Password not accepted" in str(e):
        print(">> HINT: Double check the App Password. Are there spaces?")