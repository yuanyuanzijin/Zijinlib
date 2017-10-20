# python-zijinlib
Zijinlib is a common python package written by me. Every project in this repo will import modules from this package.

## Description
Breif introductions.

### zj.file
Some methods of processing the file.

#### zj.file.sort_suffix(path, suffix)
在给定path中选出指定后缀名的文件，返回这些文件的绝对路径的数组。

#### zj.file.detect_damaged_pictures(filelist)
检测给定的图片路径列表中是否有损坏的图片。

#### zj.file.delete_from_list(dellist)
删除给定文件路径列表中的文件。

#### zj.file.search_two_suffixes(sourcelist, targetlist)
在给定的两组不同后缀名的文件路径列表中选出没有成对后缀的文件，返回这些文件的绝对路径的数组。

### zj.mail
Some methods of sending emails via python.

#### zj.mail.send_email(emailaddr, content, subject)
向给定emailaddr发送邮件，返回发送结果。

## Installation
So before you use, please run the code below in the root directory.

`pip install git+https://github.com/yuanyuanzijin/python-zijinlib`

or

`python setup.py install`

Since this project is in a period of rapid development, please confirm the current version of your package when using this project. We recommend that you run the above instructions to update your package when you update this repo.

## Usage
The document will be written soon. Before it has been written, please refer the examples in the projects folder.

The project folder contains several examlpes of using this python package. For specific instructions, see the various folders. Each folder is a script project.

