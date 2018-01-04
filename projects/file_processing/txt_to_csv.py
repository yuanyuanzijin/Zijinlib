import os

def csv_str(a,b,c,d,e,f,g,h):
    back = [a,b,c,d,e,f,g,h]
    return ",".join(back)

dir_list = os.listdir('./')
csv_file = 'train_labels.csv'
total_num = 0
with open(csv_file, mode='w', encoding='utf-8') as f2:
    header = csv_str("filename", "width", "height", "class", "xmin", "ymin", "xmax", "ymax")
    f2.writelines(header + '\n')

    for txt in dir_list:
        if txt.endswith('.txt'):
            print('开始处理%s...' % txt)
            txt_file = txt
            num = 0
            with open(txt_file, mode='r', encoding='utf-8') as f1:
                for i in f1:
                    i = i.split('\n')[0]
                    d = i.split(" ")
                    if int(d[6]) == 0:
                        filename = txt.strip('.txt') + "_" + d[5] + ".jpg"
                        classname = d[9]
                        x1 = d[1]
                        y1 = d[2]
                        x2 = d[3]
                        y2 = d[4]
                        content = csv_str(filename, "720", "405", classname, x1, y1, x2, y2)
                        f2.writelines(content + '\n')
                        num += 1
            print("%s处理完成，完成条数%d" % (txt, num))
            total_num += num
print("\n全部处理完成，共完成条数%d" % total_num)