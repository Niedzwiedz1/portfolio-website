import smtplib, ssl
import os


def send_email(message):
    username = "niewadzilukasz@gmail.com"
    password = os.getenv("PASSWORD")

    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()
    receiver = "niewadzilukasz@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

