import xlrd
import os

search = input('请输入查找内容：')
try:
    search = int(search)
except Exception as e:
    pass

excel_path = "projects/read_excel_info/tmp/1709.xlsx"
data = xlrd.open_workbook(excel_path)
table = data.sheets()[0]
nrows = table.nrows

for i in range(nrows):
    row_list = table.row_values(i)

    if search in row_list:
        name = row_list[1]
        id = int(row_list[0])
        qqnum = int(row_list[8])
        phonenum = int(row_list[7])
        room = int(row_list[10])

        print('**********为您找到符合数据：')
        print('姓名：' + name)
        print('学号：' + str(id))
        print('QQ:' + str(qqnum))
        print('手机号：' + str(phonenum))
        print('寝室：' + str(room))


