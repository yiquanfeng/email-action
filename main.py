import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(content:str, receiver_email:str):
    # init config
    sender_email = "yiquanfeng@qq.com"
    receiver_email = receiver_email
    password = os.getenv('EMAIL_PASSWORD')

    subject = "测试邮件"


    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(content, 'plain'))

    try:
        with smtplib.SMTP("smtp.qq.com", 587) as server:
            server.set_debuglevel(1)  # 打开调试模式
            server.starttls()  # 启用 TLS 加密
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("邮件发送成功")    
    except Exception as e:
        print(f"邮件发送失败: {e}")

if __name__ == "__main__":
    send_email("in github action, to greet you", "2979276763@qq.com")
    send_email("in github action, to greet you", "3677966872@qq.com")