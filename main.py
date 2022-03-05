import smtplib
import ssl
from email.message import EmailMessage

subject = "Python Email"
python = "dummy python email"
email = input("Provide email address: ")
sender_email = email
receiver_email = email
password = input("Enter a password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())