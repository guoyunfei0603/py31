"""
============================
Author:小白31
Time:2020/7/22 22:47
E-mail:1359239107@qq.com
============================
"""
import os
'''


'''

# 去掉文件名 返回目录
# res = os.path.dirname(r'D:\py31\git_code\py31\day10OS模块，异常Try\day10_01笔记.py')
# print(res) #D:\py31\git_code\py31\day10OS模块，异常Try

# 当前包路径
# package_path = os.path.abspath('.')

# join 拼接路径
f1 = r'D:\py31\git_code\py31\day10OS模块，异常Try'
f2 = 'home_work1.py'

res = os.path.join(f1, f2)
print(res)

# 获取绝对路径
res3 = os.path.abspath(".")
print(res3)

print("__file__:",__file__)
res = os.path.abspath(__file__)
print(res)

