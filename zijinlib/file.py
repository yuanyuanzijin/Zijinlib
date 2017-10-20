import os
import imghdr
import json

def search_two_suffixes(sourcelist, targetlist):
    targetlist_new = []
    dellist = []
    for t in targetlist:
        target = t.split('.')[:-1]
        targetlist_new.append(target)
        
    for s in sourcelist:
        source = s.split('.')[:-1]
        # 不存在对应的target文件则删除source文件
        if source not in targetlist_new:
            dellist.append(s)
    return dellist

def delete_from_list(dellist):
    delnumsuccess = 0
    delnumfail = 0
    for delpath in dellist:
        try:
            os.remove(delpath)
            delnumsuccess += 1
            print('已删除'+delpath)
        except Exception as e:
            delnumfail += 1
            print(delpath+'删除失败')
    return delnumsuccess, delnumfail

def sort_suffix(path, suffix):
    filelist = []
    for f in os.listdir(path):
        if f.endswith(suffix):
            filelist.append(path+f)
    return filelist

def detect_damaged_pictures(filelist):
    dellist = []
    for f in filelist:
        if not imghdr.what(f):
            dellist.append(f)
    return dellist

