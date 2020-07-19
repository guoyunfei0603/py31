"""
============================
Author:小白31
Time:2020/7/19 20:03
E-mail:1359239107@qq.com
============================
"""
'''
错误1：
UnicodeDecodeError: 'gbk' codec can't decode byte 0xac in position 2: illegal multibyte sequence
编码格式改为：UTF-8

'''
'''
r: 读     read
w: 写     write
a: 追加   append
'''
f = open('data.txt', 'r', encoding='utf-8')
# 一次性全部读取
# f1 = f.read()
# print(f1)

# 每次读取一行 可以结合for 循环遍历读取
# f2 = f.readline()
# print(f2)
# for i in range(5):
#     print(f.readline())

# 存到一个列表里面 可以切片获取指定行
# f3 = f.readlines()
# print(f3)
# print(f3[2])
# # 关闭文件资源
# f.close()

# ------------------上下文管理器-----------------------
# 推荐 with  自动关闭文件
with open(r'D:\py31\git_code\py31\day1python基础\test.txt','a',encoding='utf-8')as file:
    # file.write("99999999999999")
    file.write('追加的内容')
