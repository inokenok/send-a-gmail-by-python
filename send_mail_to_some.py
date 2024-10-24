from mail import send_mail
import time
n = int(input("Number of people："))
tol = []
bodyl = []
subjectl = []

for i in range(n):
    tol.append(input(f"送信先{i + 1}人目："))
    bodyl.append(input(f"メッセージ内容 {i + 1} 人目："))
    subjectl.append(input(f"題名{i + 1}人目："))
for i in range(n):
    to = tol[i]
    body = bodyl[i]
    subject = subjectl[i]
    send_mail(to, subject, body)
    print(f"{i+1}person done")
    time.sleep(5)
print("All Succes")
    
