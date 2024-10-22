# in ierminal
from mail import send_mail
import time
n = int(input("Number of people："))
tol = []
bodyl = []
subjectl = []
for i in range(n):
    tol.append(input(f"person you want to send{i + 1}："))
    bodyl.append(input(f"message you want to send {i + 1} person："))
    subjectl.append(input(f"{i + 1}person title："))
for i in range(n):
    to = tol[i]
    body = bodyl[i]
    subject = subjectl[i]
    send_mail(to, body, subject)
    print(f"{i+1}person done")
    time.sleep(5)
print("All Succes")
