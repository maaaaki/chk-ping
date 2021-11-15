import smtplib
from email import message
import sys
args=sys.argv
body = 'This is check alert of connection *** to *** ' 
smtp_host = 'smtp.gmail.com'
smtp_port = 587
username = '***@gmail.com'
password = '***'    #プログラムをメールで送る用のパスワードを入力

from_email = 'a:::@gmail.com'
to_email = '***@***

msg = message.EmailMessage()
msg.set_content(body)
msg['Subject'] = 'connection-alert : *** to ***'
msg['From'] = from_email
msg['To'] = to_email

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
server.quit()
