"""
============================
Author:柠檬班-木森
Time:2020/7/21   20:35
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
os模块


路径处理
os.path.dirname:获取文件/文件夹 所在的目录路径
os.path.join:路径拼接的方法
os.path.abspath:获取绝对路径


__file__: 在那个文件里面，打印的就是那个文件的文件名

"""
import os

# os.path.dirname:获取文件/文件夹 所在的目录路径
# file_path = r"C:\project\py31_class\py31_01day\demo1_01day.py"
# res = os.path.dirname(file_path)
# print(res)


# os.path.join:路径拼接的方法
# path01 = r"C:\project\py31_class\py31_01day"
# file_name = "demo1_01day.py"
# file_path = os.path.join(path01,file_name) # 等同于 "\".join(path01,file_name)
# print(file_path)

# 获取绝对路径
# res3 = os.path.abspath(".")
# print(res3)

# print("__file__:",__file__)
# res = os.path.abspath(__file__)
# print(res)


