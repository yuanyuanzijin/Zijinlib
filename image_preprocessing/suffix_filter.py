# python 3.6.1
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.split(__file__)[0], os.pardir)))
import zijinlib as zj

path = 'D:\\program\\object-detection\\data\\strawberry\\'

print('开始检测...')
sourcenum1, delnum1, dellist1 = zj.file.search_two_suffixes(path, '.jpg', '.xml')
sourcenum2, delnum2, dellist2 = zj.file.search_two_suffixes(path, '.xml', '.jpg')
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
    deleteresult = zj.file.delete_from_list(path, dellist)
    print('删除完毕，任务队列%d个文件，成功删除%d个文件，未删除%d个文件' 
        % (len(dellist), deleteresult[0], deleteresult[1]))
else:
    print('您已取消，未进行操作')
