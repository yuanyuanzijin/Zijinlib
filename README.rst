===============================================
python-zijinlib
===============================================

Zijinlib is a common python package written by me. Every project in this repo will import modules from this package.

Installation
================

So before you use, please run the code below in the root directory.

``pip install zijinlib`` 

for installing the stable version.

or

``pip install git+https://github.com/yuanyuanzijin/python-zijinlib`` 

for installing and updating the newest version.

Since this project is in a period of rapid development, please confirm the current version of your package when using this project. We recommend that you update your package when you see new changes in this repo.

Usage
=============

The document will be written soon. Before it has been written, please refer the examples in the projects folder.

The project folder contains several examlpes of using this python package. For specific instructions, see the various folders. Each folder is a script project.

Description
================

Brief introductions.

zijinlib.file
-------------

Some methods of processing the file. You can use

``import zijinlib.file as file``

to import zijinlib.file module.

* file.sort(path, suffix)

在给定path中选出指定后缀名的文件，返回这些文件的绝对路径的数组。

* file.detect_damage(filelist)

检测给定的图片路径列表中是否有损坏的图片。

* file.delete_files(dellist)

删除给定文件路径列表中的文件。

* file.compare_suffixes(sourcelist, targetlist)

在给定的两组不同后缀名的文件路径列表中选出没有成对后缀的文件，返回这些文件的绝对路径的数组。

zijinlib.spider
-----------------

Some methods of writing web crawler.You can use

``import zijinlib.spider as spider``

to import zijinlib.spider module.

* spider.open(url, charset=None)

使用GET方法访问网站，自动识别编码并解析网站（也可指定编码），返回网站内容。

* spider.post(url, data=None, headers=None, charset=None)

向指定网址发送POST请求，会自动对data进行urlencode，返回响应内容。

* spider.open_proxy(proxy)

开启http上网代理，只需运行一次。

* class spider.Cookie()

Cookie类，在网站访问前定义对象，如cookie = spider.Cookie()，网站访问后可使用print(cookie)查看cookie字典，以及cookie.get(key)方法获取指定cookie值。

zijinlib.mail
------------------

Some methods of sending emails via python.You can use

``import zijinlib.mail as mail``

to import zijinlib.mail module.

* mail.init(config_path)

从给定路径读取配置文件，返回邮箱配置信息。

* mail.send(config, emailaddr, content, subject)

向给定emailaddr发送邮件，返回发送结果，第一个参数为mail.init()的返回值。

zijinlib.qq
-----------------

Some methods of send qq message via python.

注意！！本模块基于qqbot，使用前，请在终端运行 ``pip install qqbot`` 安装该模块。安装后，在终端运行 ``qqbot`` 扫码登录。登录后会保存登录信息，两天内可通过 ``qqbot -q qq号码`` 免扫码自动登录。

After that, you can use

``import zijinlib.qq as qq``

to import zijinlib.qq module.

* qq.update()

更新好友，群，讨论组列表。

* qq.send(mode, members, content)

发送QQ消息，mode代表模式（0好友，1群，2讨论组），members为发送对象（数组形式，可群发），content为消息内容。