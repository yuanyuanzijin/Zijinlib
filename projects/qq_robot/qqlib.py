import os

def send(members, content):
    for name in members:
        os.system('qq send buddy %s %s' % (name, content))

def send_group(groups, content):
    for group in groups:
        os.system('qq send group %s %s' % (group, content))
