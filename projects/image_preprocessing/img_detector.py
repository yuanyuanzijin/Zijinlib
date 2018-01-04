# python 3.6.1
import os
import imghdr
import zijinlib.file as zfile

classname = input('请输入要检测的分类名称：')
path = 'D:\\program\\object-detection\\data\\' + classname
suffix = input('请输入要检测的图片后缀（默认为jpg）')
if not suffix:
    suffix = 'jpg'
print('开始检测损坏的%s文件...' % suffix)

filelist = zfile.sort(path, suffix)
filenum = len(filelist)
print('共检测到%d张%s后缀的图片' % (filenum, suffix))

dellist = zfile.detect_damage(filelist)
delnum = len(dellist)

if not dellist:
    print('检测完毕，没有图片损坏')
    exit()

print('检测到%d张图片已损坏，它们是：' % delnum)
for i in dellist:
    print(i)

s = input('是否删除这些文件？([y]/n)：')
if not s:
    s = 'y'
if s == ('y' or 'Y'):
    print('开始删除任务队列...')
    delnumsuccess, delnumfail = zfile.delete_files(dellist)
    print('删除完毕，任务队列%d个文件，成功删除%d个文件，未删除%d个文件' 
        % (delnum, delnumsuccess, delnumfail))
    print('删除后请重新执行sffix_filter.py')
else:
    print('您已取消，未进行操作')
