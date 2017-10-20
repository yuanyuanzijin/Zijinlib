import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header

def mail_init():
    secret_path = os.path.join('excel_info_sending', "secret.txt")
    with open(secret_path) as f:
        content = f.readlines()
        mail_host = content[0].strip()  #设置服务器
        mail_user = content[1].strip()
        mail_pass = content[2].strip()
        sender = content[3].strip()
    return mail_host, mail_user, mail_pass, sender

def send_email(emailaddr, content, subject):
    mail_host, mail_user, mail_pass, sender = mail_init()
    receivers = [emailaddr]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    mail_msg = content
    m = MIMEText(mail_msg, 'html', 'utf-8')
    m['From'] = mail_user
    m['To'] =  emailaddr
    m['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP_SSL() 
        smtpObj.connect(mail_host, 465)
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(mail_user, receivers, m.as_string())
        return True
    except smtplib.SMTPException:
        return False
    