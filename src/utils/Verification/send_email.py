import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(sender, recipient, subject, message):
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(os.getenv("GMAIL"), os.getenv("GMAIL_PASSWORD"))
        email = f"Subject: {subject}\n\n{message}"
        server.sendmail(sender, recipient, email)

# Usage
# send_email(os.getenv("GMAIL"), 'eulagly@gmail.com', 'Hello', 'This is a test email.')
