import os

members = ['小王', '小李']
groups = ['群名', ]

def send(members, content):
    for name in members:
        os.system('qq send buddy %s %s' % (name, content))

def send_group(groups, content):
    for group in groups:
        os.system('qq send group "%s" "%s"' % (group, content))

send(members, '嘿嘿')
send(groups, '大家好')
