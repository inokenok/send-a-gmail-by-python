import os
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from email.mime.application import MIMEApplication

def send_mail(to, subject, body):
    ID = 'your gmail id'
    PASS = os.environ['MAIL_PASS']  # 環境変数から取得するアプリパスワード
    HOST = 'smtp.gmail.com'
    PORT = 587

    msg = MIMEMultipart()
    msg.attach(MIMEText(body, 'html'))
    msg['Subject'] = subject
    msg['From'] = ID
    msg['To'] = to

    # SMTPサーバーに接続し、メールを送信
    try:
        with SMTP(HOST, PORT) as server:
            server.starttls()  # TLS暗号化を開始
            server.login(ID, PASS)  # 認証
            server.sendmail(ID, to, msg.as_string())  # メールを送信
            print("メールが送信されました")
    except Exception as e:
        print(f"エラーが発生しました: {e}")



