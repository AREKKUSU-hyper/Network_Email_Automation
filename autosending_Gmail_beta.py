import email.message
msg=email.message.EmailMessage()
msg["From"]="Email"
msg["To"]="Email"
msg["Subject"]="Final Test(連送五次~我不是垃圾郵件)"

# 寄送比較多樣式的內容 (html)
# msg.add_alternative("<h1>優惠卷</h1>大華堡買一送一",subtype="html")

import smtplib
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("Email","Email")

T=0
for i in range(T):
    msg.set_content("第{0}次 QQ自動送信測試({0}/{1})".format(i+1,T))
    server.send_message(msg)

msg2=email.message.EmailMessage()
msg2["From"]="Email"
msg2["To"]="Email"
msg2["Subject"]="肯Q基"
msg2.add_alternative("<h1>假優惠卷</h1>大QQ華堡買一送一",subtype="html")
server.send_message(msg2)

server.close()


