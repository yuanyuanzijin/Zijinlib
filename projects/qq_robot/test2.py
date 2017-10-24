from qqbot import _bot as bot

bl = bot.List('buddy', '梅海洋')
if bl:
    b = bl[0]
    bot.SendTo(b, '我说我世界第二帅，恐怕没人敢说第一了吧？')
