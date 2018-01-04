import os

dir_list = os.listdir('./')
for i in dir_list:
    if os.path.isdir(i):
        print("正在处理总文件夹%s..." % i)
        num = 0
        path = i
        if os.path.exists(path):
            file_list = os.listdir(path)
            for k in file_list:
                if not k.startswith(path):
                    os.rename(path+"/"+k, path+"/"+path+"_"+k)  
                    num += 1
                    print('正在处理%s，已完成%d个文件' % (k, num), end="\r")
        print("\n总文件夹%s处理完成！\n" % i)
