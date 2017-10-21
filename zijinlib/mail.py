import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header
import configparser 

def init(config_path):
    c = ConfigParser.ConfigParser() 
    with open(config_path) as f: 
        c.readfp(f) 
        mail_host = c.get('info', 'mail_host')  #设置服务器
        mail_port = c.get('info', 'mail_port')
        mail_user = c.get('info', 'mail_user')
        mail_pass = c.get('info', 'mail_pass')
        sender = c.get('info', 'sender')
    return mail_host, mail_port, mail_user, mail_pass, sender

def send(config, emailaddr, content, subject):
    mail_host, mail_port, mail_user, mail_pass, sender = config
    receivers = [emailaddr]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    mail_msg = content
    m = MIMEText(mail_msg, 'html', 'utf-8')
    m['From'] = mail_user
    m['To'] =  emailaddr
    m['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP_SSL() 
        smtpObj.connect(mail_host, mail_port)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, m.as_string())
        return True
    except smtplib.SMTPException:
        return False
    