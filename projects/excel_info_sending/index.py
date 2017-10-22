import xlrd
import os
import zijinlib.mail as zmail

excel_path = os.path.join('projects', 'excel_info_sending', "tmp", "info.xlsx")  # 自行导入，本例中第一列是学号，第二列是姓名，第三列是邮箱，第四列是要发送的密码
data = xlrd.open_workbook(excel_path)
table = data.sheets()[0]
nrows = table.nrows

config_path = os.path.join('projects', 'excel_info_sending', 'mail_config.ini')
config = zmail.init(config_path)

print('开始邮件发送......')
successnum = 0
failnum = 0
for i in range(nrows): 
    data = table.row_values(i)
    name = data[1]
    emailaddr = data[2]
    password = data[3]
    subject = "心理测评密码"
    content = """
        <p>网址：http://xinli.gzedu.com/</p>
        <p>%s你好，你的心理测评密码为：%s</p>
    """ % (name, password)
    back = zmail.send(config, emailaddr, content, subject)
    if back:
        print(name+'发送成功')
        successnum += 1
    else:
        print(name+'发送失败！！！')
        failnum += 1

print('邮件发送完毕，成功%d条，失败%d条' % (successnum, failnum))
