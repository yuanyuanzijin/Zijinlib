import xlrd
import os
from sendemail import send

excel_path = os.path.join('excel_info_sending', "tmp", "info.xls")  # 自行导入，本例中第一列是学号，第二列是要发送的密码，第三列是姓名，第四列是邮箱
data = xlrd.open_workbook(excel_path)
table = data.sheets()[0]
nrows = table.nrows
for i in range(nrows): 
    data = table.row_values(i)
    name = data[2]
    emailaddr = data[3]
    password = data[1]
    subject = "心理测评密码"
    content = """
        <p>网址：http://xinli.gzedu.com/</p>
        <p>%s你好，你的心理测评密码为：%s</p>
        <p>学校代码为:10141</p>
        <p>请大家在22日（周日）中午前完成！务必！以免被通报批评！</p>
        <p>因为密码必须私自发给你们，所以选用了这种方式哈哈。填写时如果有问题请QQ找我。</p>
        <p>from：爱你们的班长</p>
    """ % (name, password)
    back = send(name, emailaddr, content, subject)
    print(back)
