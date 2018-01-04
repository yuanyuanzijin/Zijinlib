import cv2

img_dict = {}
img_paths = 'E:/BaiduYunDownload/shuixiaceshi/all_train_data_0829/G0024172/'
csv_file = './G0024172.csv'
with open(csv_file, mode='r', encoding='utf-8') as f1:
    lines = f1.readlines()
    for index, i in enumerate(lines[1:]):
        data = i.split(',')
        filename = data[0]
        if not filename:
            continue
        if filename not in img_dict.keys():
            new_list = []
            new_list.append(index)
            img_dict[filename] = new_list
        else:
            new_list = img_dict[filename]
            new_list.append(index)
            img_dict[filename] = new_list

for i in img_dict.keys():
    img = cv2.imread('%s' % i)  # 读取本地图片，目前OpevCV支持bmp、jpg、png、tiff
    pos = img_dict[i]
    cv2.rectangle(img,(20,20),(100,100),(0,0,255),1)
    cv2.namedWindow("Image")  # 创建一个窗口用来显示图片
    cv2.imshow("Image", img)  # 显示图片
    cv2.waitKey(0)  # 等待输入,这里主要让图片持续显示。
    cv2.destroyAllWindows()  # 释放窗口