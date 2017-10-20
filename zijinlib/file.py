import os
import imghdr

def search_two_suffixes(path, source, target):
    sourcenum = 0
    delnum = 0
    dellist = []

    for f in os.listdir(path):
        # 筛选出source文件
        sourcefile = f
        if sourcefile.endswith(source):
            sourcenum += 1
            sourcename = sourcefile.strip(source)
            # 不存在对应的target文件则删除source文件
            targetpath = os.path.join(path, sourcename+target)
            if not os.path.exists(targetpath):
                delpath = os.path.join(path, sourcefile)
                dellist.append(delpath)
                delnum += 1
    return sourcenum, delnum, dellist

def delete_from_list(path, dellist):
    delnumsuccess = 0
    delnumfail = 0
    for delfile in dellist:
        delpath = os.path.join(path, delfile)
        try:
            os.remove(delpath)
            delnumsuccess += 1
            print('已删除'+delpath)
        except Exception as e:
            delnumfail += 1
            print(delpath+'删除失败')
    return delnumsuccess, delnumfail

def detect_damaged_pictures(path, suffix):
    delnum = 0
    dellist = []
    for f in os.listdir(path):
        # 筛选出图片文件
        image = f
        if image.endswith(suffix):
            jpgpath = os.path.join(path, image)
            if not imghdr.what(jpgpath):
                delnum += 1
                dellist.append(image)
    return delnum, dellist