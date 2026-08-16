import smtplib
from email.message import EmailMessage

sender = "your_email@example.com"
receiver = "receiver@example.com"

subject = "Python Practice Email"
message = "Hello! This is a practice email created using Python."

email = EmailMessage()
email["From"] = sender
email["To"] = receiver
email["Subject"] = subject
email.set_content(message)

print("Email created successfully!")
print("From:", sender)
print("To:", receiver)
print("Subject:", subject)
print("Message:", message)