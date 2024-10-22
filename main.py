from mail import send_mail
to = input("送信先")
subject = input("題")
body = input("内容")

send_mail(to, subject, body)