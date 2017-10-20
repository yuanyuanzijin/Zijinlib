import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header

def mail_init():
    mail_host="smtp.qq.com"  #设置服务器
    secret_path = os.path.join('excel_info_sending', "secret.txt")
    with open(secret_path) as f:
        content = f.readlines()
        mail_user = content[0]
        mail_pass = content[1]
    return mail_host, mail_user, mail_pass

def send_email(name, emailaddr, content, subject):
    mail_host, mail_user, mail_pass = mail_init()
    sender = mail_user
    receivers = [emailaddr]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    mail_msg = content
    message = MIMEText(mail_msg, 'html', 'utf-8')
    message['From'] = mail_user
    message['To'] =  emailaddr
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP_SSL() 
        smtpObj.connect(mail_host, 465)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        return name+"发送成功"
    except smtplib.SMTPException:
        return name+"邮件发送失败！！！"