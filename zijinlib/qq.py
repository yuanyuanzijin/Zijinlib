import os

def send(mode, members, content):
    if mode == 0:
        target = 'buddy'
    elif mode == 1:
        target = 'group'
    elif mode == 2:
        target = 'discuss'
    else:
        print('模式错误，好友为0，群为1，讨论组为2')

    for member in members:
        os.system('qq send %s %s %s' % (target, member, content))

def update():
    os.system('qq update buddy')
    os.system('qq update group')
    os.system('qq update discuss')