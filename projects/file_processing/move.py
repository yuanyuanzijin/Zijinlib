import os, shutil

dir_list = os.listdir('./')
for i in dir_list:
    if os.path.isdir(i):
        print("正在处理总文件夹%s..." % i)
        num = 0
        path = i + "/0/"
        if os.path.exists(path):
            dir_list2 = os.listdir(path)
            for j in dir_list2:
                path2 = path + j
                print("正在处理子文件夹%s..." % path2)
                file_list = os.listdir(path2)
                for k in file_list:
                    shutil.move(path2 + "/" + k, i)
                    num += 1
                os.rmdir(path2)
            os.rmdir(path)
        print("总文件夹%s处理完成，共处理%d个文件！\n" % (i, num))
