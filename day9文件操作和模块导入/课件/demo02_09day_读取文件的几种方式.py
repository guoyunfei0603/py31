"""

read():读取文件中所有的内容


"""
# 1、打开
f = open(r"C:\project\py31_class\py31_01day\test01day.txt", "r", encoding="utf-8")

# # 2、读取内容
# 第一种方式：read：读取所有的内容
# content = f.read()

# 第二种方式：readline：每次读取一行内容
# content = f.readline()
# print('1', content)
# print('2', f.readline())
# print('3', f.readline())

# for i in range(8):
#     print(f.readline())

# 第三种方式：readlines：按行把所有的内容，读取到一个列表中,每一行就是列表中的一个元素
# content3 = f.readlines()
# print(content3)

# 读取第六行的内容
# c7 = f.readlines()[6]
# print(c7)



# 3、关闭文件
f.close()
