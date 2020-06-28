# 寄送Email的程式
# 準備訊息物件設定
import email.message
msg=email.message.EmailMessage()
msg["From"]="Email"
msg["To"]="Email"
msg["Subject"]="測試測試"

# 寄送純文字的內容
# msg.set_content("test")

# 寄送比較多樣式的內容 (html)
msg.add_alternative("<h3>優惠卷</h3>大華堡買一送一",subtype="html")

# 連線到 SMTP server, 驗證寄件人身分並發送郵件
# 搜尋 gmail smtp server / yahoo smtp server
# 簡單郵件傳輸協定（Simple Mail Transfer Protocol，SMTP）
import smtplib
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("Email","Email")
server.send_message(msg)
server.close()