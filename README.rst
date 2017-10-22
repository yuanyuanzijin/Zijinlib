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

使用GET方法访问网站，自动识别编码并解析网站（也可指定编码），返回网站内容

* spider.post(url, data=None, headers=None, charset=None)

向指定网址发送POST请求，会自动对data进行urlencode，返回响应内容

* spider.open_proxy(proxy)

开启http上网代理，只需运行一次

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
