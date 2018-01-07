import getpass, time, os
import zijinlib.mail as zmail
import dutsso

config_path = os.path.join('mail_config.ini')
config = zmail.init(config_path)

def send_email(scores, obj):
    if obj.first_use:
        subject = "欢迎使用新成绩提醒系统！"
        content = "<p>%s您好，您已订阅新成绩提醒系统，我们将在检测新成绩后为您推送邮件~</p>" % obj.username
    else:
        subject = "发现新成绩！"
        content = "<p>%s您好，发现一条新成绩</p>" % obj.username
    content += '*****共找到%d条必修课成绩<br />' % len(scores["bx"])
    for i in scores["bx"].keys():
        line = "<p>" + i + " " + scores["bx"][i] + "</p>"
        content += line
    content += '*****共找到%d条选修课成绩' % len(scores["xx"])
    for i in scores["xx"].keys():
        line = "<p>" + i + " " + scores["xx"][i] + "</p>"
        content += line
    content += "<hr /><p>我的Github主页：<a href='https://github.com/yuanyuanzijin'>https://github.com/yuanyuanzijin</a></p><p>Powered by Zijin</p>"
    back = zmail.send(config, obj.emailaddr, content, subject)
    obj.first_use = 0
    return back

print('\n********** 欢迎使用大连理工大学研究生成绩自助查询系统 **********')
print('*********************** Powered by Zijin ***********************')

u_len = int(input("请输入同时检测的人数："))
u = {}
for i in range(u_len):
    u['u'+str(i)] = dutsso.User()
    u['u'+str(i)].old_num = 0
    u['u'+str(i)].first_use = 1

    while 1:
        u['u'+str(i)].username = input('\n请输入第%d个用户的学号：' % (i+1))
        u['u'+str(i)].password = getpass.getpass('请输入第%d个的用户密码：' % (i+1))
        u['u'+str(i)].emailaddr = input("请输入第%d个用户的提醒邮箱：" % (i+1))

        # SSO登录
        login = u['u'+str(i)].login()
        if login:
            print(u['u'+str(i)].username + "第%d个用户登录成功！" % (i+1))
            break
        else:
            print("第%d个用户用户名密码错误！" % i)

atime = time.time()
alert_times = 0

while 1:
    # 查询研究生成绩
    for i in range(u_len):
        if not u['u'+str(i)].isactive():
            print('\n第%d个用户登录状态过期，正在重连...' % (i+1))
            if u['u'+str(i)].login(try_cookies=False):
                print('第%d个用户重新登陆成功！' % (i+1))

        scores = u['u'+str(i)].get_score()
        u['u'+str(i)].new_num = len(scores["bx"]) + len(scores["xx"])
        if u['u'+str(i)].new_num > u['u'+str(i)].old_num:
            if u['u'+str(i)].first_use:
                print("\n%s您好，您已订阅新成绩提醒系统！提醒邮箱%s" % (u['u'+str(i)].username,  u['u'+str(i)].emailaddr))
            else:
                print("\n%s发现新成绩！您的研究生成绩信息为：" % u['u'+str(i)].username)
            print('*****共找到%d条必修课成绩' % len(scores["bx"]))
            for m in scores["bx"].keys():
                print(m, scores["bx"][m])
            print('*****共找到%d条选修课成绩' % len(scores["xx"]))
            for m in scores["xx"].keys():
                print(m, scores["xx"][m])
            back = send_email(scores, u['u'+str(i)])
            if back:
                print("邮件发送成功！" + u['u'+str(i)].emailaddr)
                alert_times += 1
            else:
                print("邮件发送失败！" + u['u'+str(i)].emailaddr)

            u['u'+str(i)].old_num = len(scores["bx"]) + len(scores["xx"])

    btime = time.time()
    cost = btime - atime
    hour = int(cost/3600)
    minute = int((cost%3600)/60)
    print("\r已稳定运行%d小时%d分，共发现新成绩%d次" %(hour, minute, alert_times), end="")
    time.sleep(60)


            