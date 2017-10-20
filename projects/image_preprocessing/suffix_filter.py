# python 3.6.1
import os
import zijinlib as zj

classname = input('请输入要检测的分类名称：')
path = 'D:\\program\\object-detection\\data\\' + classname

suffix1 = 'jpg'
suffix2 = 'xml'
list1 = zj.file.sort_suffix(path, suffix1)
list2 = zj.file.sort_suffix(path, suffix2)
listnum1 = len(list1)
listnum2 = len(list2)

dellist1 = zj.file.search_two_suffixes(list1, list2)
delnum1 = len(dellist1)
dellist2 = zj.file.search_two_suffixes(list2, list1)
delnum2 = len(dellist2)
dellist = dellist1 + dellist2

print('检测到%d张图片和%d个xml文件，其中有%d张图片和%d个xml文件缺少对应项。'\
    % (listnum1, listnum2, delnum1, delnum2))

if not dellist:
    print('没有需要处理的文件')
    exit()

s = input('是否删除这些文件？([y]/n)：')
if not s:
    s = 'y'
if s == ('y' or 'Y'):
    print('开始删除任务队列...')
    deleteresult = zj.file.delete_from_list(dellist)
    print('删除完毕，任务队列%d个文件，成功删除%d个文件，未删除%d个文件' 
        % (len(dellist), deleteresult[0], deleteresult[1]))
else:
    print('您已取消，未进行操作')
