from qqbot import _bot as bot
bot.Login(['-q', '1877174005'])
bl = bot.List('buddy', '渊渊子衿')
if bl:
    b = bl[0]
    bot.SendTo(b, '我说我世界第二帅，恐怕没人敢说第一了吧？')
