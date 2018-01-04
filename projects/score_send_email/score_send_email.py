import getpass, time, os
import zijinlib.mail as zmail
import dutsso

emailaddr = "jinluyuan@vip.qq.com"
config_path = os.path.join('mail_config.ini')
config = zmail.init(config_path)

def send_email(scores):
    subject = "发现新成绩！"
    content = "<p>发现一条新成绩</p>"
    content += '*****共找到%d条必修课成绩<br />' % len(scores["bx"])
    for i in scores["bx"].keys():
        line = "<p>" + i + " " + scores["bx"][i] + "</p>"
        content += line
    content += '*****共找到%d条选修课成绩' % len(scores["xx"])
    for i in scores["xx"].keys():
        line = "<p>" + i + " " + scores["xx"][i] + "</p>"
        content += line
    back = zmail.send(config, emailaddr, content, subject)
    return back

print('\n********** 欢迎使用大连理工大学研究生成绩自助查询系统 **********')
print('*********************** Powered by Zijin ***********************')
user = dutsso.User()

while 1:
    username = input('\n请输入学号：')
    password = getpass.getpass('请输入密码：')

    # SSO登录
    login = user.login(username, password)
    if login:
        print(username + "登录成功！开始检测成绩...")
        break
    else:
        print("用户名密码错误！")

old_num = 0
while 1:
    # 查询研究生成绩
    scores = user.get_score()
    new_num = len(scores["bx"]) + len(scores["xx"])
    if old_num != new_num:
        print("\n发现新成绩！您的研究生成绩信息为：")
        print('*****共找到%d条必修课成绩' % len(scores["bx"]))
        for i in scores["bx"].keys():
            print(i, scores["bx"][i])
        print('*****共找到%d条选修课成绩' % len(scores["xx"]))
        for i in scores["xx"].keys():
            print(i, scores["xx"][i])
        atime = time.time()
        back = send_email(scores)
        if back:
            print("邮件发送成功！" + emailaddr)
        else:
            print("邮件发送失败！" + emailaddr)
        
    else:
        btime = time.time()
        cost = btime - atime
        hour = int(cost/3600)
        minute = int((cost%3600)/60)
        print("距离上次找到新成绩已过去%d小时%d分" %(hour, minute), end="\r")
    old_num = len(scores["bx"]) + len(scores["xx"])
    time.sleep(60)


