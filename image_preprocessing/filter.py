# python 3.6.1
import os
from common import search, delete

path = 'D:\\program\\object-detection\\data\\strawberry\\'

print('开始检测...')
sourcenum1, delnum1, dellist1 = search(path, '.jpg', '.xml')
sourcenum2, delnum2, dellist2 = search(path, '.xml', '.jpg')
dellist = dellist1 + dellist2

print('检测到%d张图片和%d个xml文件，其中有%d张图片和%d个xml文件缺少对应项。'\
    % (sourcenum1, sourcenum2, delnum1, delnum2))

if not dellist:
    print('没有需要处理的文件')
    exit()

s = input('是否删除这些文件？([y]/n)：')
if not s:
    s = 'y'

if s == ('y' or 'Y'):
    print('开始删除任务队列...')
    deleteresult = delete(path, dellist)
    print('删除完毕，任务队列%d个文件，成功删除%d个文件，未删除%d个文件' 
        % (len(dellist), deleteresult[0], deleteresult[1]))
else:
    print('您已取消，未进行操作')
