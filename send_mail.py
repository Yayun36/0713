import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
sender = "elisa.y.cheng@gmail.com"
receiver = ["elisa_y_cheng@yahoo.co.uk"]

for i in receiver:
    msg = MIMEMultipart()
    msg["From"]= sender
    msg["To"] = i
    header =Header("Test Send Email","utf-8")
    msg["Subject"] = header.encode()

    body = "This is email sent from python"
    msg.attach(MIMEText(body))
    ssl_context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",465, context=ssl_context) as server:
        server.login(sender,"d o s t g m l d u i d g j k q q")
        server.sendmail(sender,receiver,msg.as_string())
print("sucess send email")