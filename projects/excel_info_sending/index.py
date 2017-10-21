import xlrd
import os
import zijinlib as zj

excel_path = os.path.join('excel_info_sending', "tmp", "info.xlsx")  # 自行导入，本例中第一列是学号，第二列是姓名，第三列是邮箱，第四列是要发送的密码
data = xlrd.open_workbook(excel_path)
table = data.sheets()[0]
nrows = table.nrows

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
        <p>学校代码为:10141</p>
        <p>请大家在22日（周日）中午前完成！务必！以免被通报批评！</p>
        <p>因为密码必须私自发给你们，所以选用了这种方式哈哈。填写时如果有问题请QQ找我。</p>
        <p>from：爱你们的班长</p>
    """ % (name, password)
    back = zj.mail.send_email(emailaddr, content, subject)
    if back:
        print(name+'发送成功')
        successnum += 1
    else:
        print(name+'发送失败！！！')
        failnum += 1

print('邮件发送完毕，成功%d条，失败%d条' % (successnum, failnum))