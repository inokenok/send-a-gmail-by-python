import os
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from email.mime.application import MIMEApplication
def send_mail(to, subject, body):
    ID = 'gmail address'
    PASS = os.environ['MAIL_PASS']# application pass in google account settings and set in windows
    HOST = 'smtp.gmail.com'
    PORT = 587
    msg = MIMEMultipart()
    msg.attach(MIMEText(body,'html'))
    msg['Subject'] = subject
    msg['From'] = ID
    msg['To'] = to
