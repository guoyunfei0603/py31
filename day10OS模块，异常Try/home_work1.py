"""
============================
Author:小白31
Time:2020/7/22 23:26
E-mail:1359239107@qq.com
============================
"""

# 1、实现一个文件复制器函数，通过给函数传入一个路径，复制该路径下面所有的文件(目录不用复制)到当前目录，
# 要求：如果传路径不存在，不能报错                提示：os模块结合文件读写操作 、异常捕获 即可实现

'''
疑惑：
我的代码，
1. 自己新建了一个cp_file.txt文件
2. 判断路径下是否有文件，如果有的话
3. 读取文件内容，追加到cp_file.txt

没有实现文件的复制，只是文件内容的复制
'''
import os


def file_copy(file_path):
    # 获取当前路径下的文件、文件夹
    list_dir = os.listdir(file_path)

    # 遍历目录下每个文件、文件夹
    for i in list_dir:
        # join 拼接
        res = os.path.join(file_path, i)

        if os.path.isfile(res):
            # print('文件：',res,type(res))
            # li.append(res)

            try:
                # 读取文件内容
                with open(res, 'r', encoding='utf-8')as file:
                    f1 = file.read()
                # 复制  ===>这个 是写入，如果多个文件没法处理
                with open(r'D:\py31\git_code\py31\day10OS模块，异常Try\cp_file', 'a', encoding='utf-8')as file:
                    f2 = file.write(f1)
            except Exception as e:
                print("错误信息为：",e)


file_copy(r"D:\py31\git_code\py31\day10OS模块，异常Try")



