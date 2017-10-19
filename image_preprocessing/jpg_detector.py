# python 3.6.1
import os
import imghdr
from common import detector, delete

path = 'D:\\program\\object-detection\\data\\strawberry\\'

print('开始检测损坏的jpg文件...')
delnum, dellist = detector(path)

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
    delnumsuccess, delnumfail = delete(path, dellist)
    print('删除完毕，任务队列%d个文件，成功删除%d个文件，未删除%d个文件' 
        % (len(dellist), delnumsuccess, delnumfail))
    print('删除后请重新执行filter.py')
else:
    print('您已取消，未进行操作')
