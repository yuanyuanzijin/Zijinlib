import getpass
import time
import os
from bs4 import BeautifulSoup
import zijinlib.mail as zmail
import dutsso

config_path = os.path.join('mail_config.ini')
config = zmail.init(config_path)

def send_email(course=None, all_list=None):
    if not course:
        subject = "欢迎使用Zijin选课助手！"
        content = "<p>%s您好，欢迎使用选课助手，我们将在成功选课后为您推送邮件~</p>" % u.name
        content += "<p>待选课程如下：</p>"
        for i in all_list:
            content += "<p>%s</p>" % i['c_name']
    else:
        subject = "课程《%s》选课成功！" % course['c_name']
        content = "<p>%s您好，已为您选择一门课程：</p>" % u.name
        content += course['c_name']

    content += "<hr /><p>我的Github主页：<a href='https://github.com/yuanyuanzijin'>https://github.com/yuanyuanzijin</a></p><p>Powered by Zijin</p>"
    back = zmail.send(config, u.emailaddr, content, subject)
    return back


print('\n********** 欢迎使用大连理工大学研究生选课系统 **********')
print('******************** Powered by Zijin ********************')

u = dutsso.User()
success = 0

while 1:
    u.username = input('\n请输入学号：')
    u.password = getpass.getpass('请输入密码：')
    u.emailaddr = input('请输入提醒邮箱（为空则表示不提醒）：')

    login = u.login()
    if not login:
        print("用户名密码错误！")
    else:
        print("%s（%s）登录成功！" % (u.name, u.type))
        break

course_list = u.get_course_not_choosed()
if course_list:
    print("\n发现未选课程如下：")
    for i in course_list:
        print(i['c_name'])

    print("\n开始为您选课...\n")
    if u.emailaddr:
        send_email(all_list=course_list)
    atime = time.time()

while 1:
    if not u.isactive():
        print("登录状态已失效，正在重新登录...")
        if u.login(try_cookies=False):
            print("重新登录成功！")
    
    for i in course_list:
        status = i['c_enable']
        # 如果可选
        if status: 
            back = u.choose_course(i)
            if back:
                print("******%s选课成功！" % i['c_name'])
                if u.emailaddr:
                    back = send_email(course=i)
                    if back:
                        print("邮件发送成功，提醒邮箱：%s" % u.emailaddr)
                success += 1
            else:
                print("******%s选课失败！" % i['c_name'])

    course_list = u.get_course_not_choosed()            
    if not course_list:
        print("\n恭喜您，您已选择全部课程！")
        break
    btime = time.time()
    cost = btime - atime
    hour = int(cost/3600)
    minute = int((cost%3600)/60)
    print("\r已稳定运行%d小时%d分，为您抢课%d门，待抢课%d门" % (hour, minute, success, len(course_list)), end='')
    time.sleep(3)
    