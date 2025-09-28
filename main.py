import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(content:str):
    # init config
    sender_email = "yiquanfeng@qq.com"
    receiver_email = "yiquanfeng063@gmail.com" ## lyq's qq
    password = os.getenv('EMAIL_PASSWORD')

    subject = "测试邮件"


    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(content, 'plain'))

    try:
        with smtplib.SMTP_SSL("smtp.qq.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            server.quit()
            print("邮件发送成功")    
    except Exception as e:
        print(f"邮件发送失败: {e}")

if __name__ == "__main__":
    send_email("in github action, to greet you")