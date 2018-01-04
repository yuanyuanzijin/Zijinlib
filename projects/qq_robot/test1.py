import zijinlib.qq as zqq

# 更新好友，群和讨论组列表
zqq.update()

mode = 0   # 好友0, 群1, 讨论组2
members = ['小王']      # QQ号，群号和备注名均可，多人可群发
content = '你好啊'
zqq.send(mode, members, content)

