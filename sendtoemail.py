import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Run Python file
subprocess.run(["python", "your_script.py"])

# Email settings
sender_email = "sender@example.com"
recipient_email = "recipient@example.com"
subject = "Results"
body = "Please find attached the results of your script"

# File to be attached
file_path = "results.txt"

# Create message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject

# Attach body
msg.attach(MIMEText(body, 'plain'))

# Attach file
with open(file_path, "rb") as f:
    attach_file = MIMEApplication(f.read(), _subtype="txt")
    attach_file.add_header('Content-Disposition', 'attachment', filename="results.txt")
    msg.attach(attach_file)

# Send email
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "your_username"
smtp_password = "your_password"

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())

print("Email sent!")
