"""
============================
Author:小白31
Time:2020/7/19 20:25
E-mail:1359239107@qq.com
============================
"""
'''
1. 把data.txt的数据读取出来，转换为以下格式
{'data0':'数据aaa','data1':'数据bbb','data2':'数据ccc','data3':'数据ddd'}

提示：读取出来的如果有换行\n 想办法去掉 （字符串替换）
'''

# todo 考虑写成函数，处理 替换\n
with open('data.txt', 'r', encoding='utf-8')as file:
    f = file.readlines()  # 这个遍历出来是一个列表包含data.txt的数据
    # 定义一个空列表，用来存放 替换\n后的元素
    new_list = []

    for i in f:
        # 替换\n
        new_str = i.replace('\n', '')
        # 把替换后的元素添加到新列表
        new_list.append(new_str)
    # print(new_list)

# li = ['data0','data1','data2','data3'] # 直接定义，

li = []
for item in range(4):
    li.append('data'+str(item))
print(li)

res = dict(zip(li,new_list))
print(res)

