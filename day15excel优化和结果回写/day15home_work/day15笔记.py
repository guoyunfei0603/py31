"""
============================
Author:小白31
Time:2020/8/2 23:37
E-mail:1359239107@qq.com
============================
"""
'''
1. myddt 源码用的是木森老师改过的，测试报告可以显示用例描述
2. 已封装hand_excel（包括列表推导式）
3. unittestreport title,dis等，源码修改为自己的
'''
# 生成 ["学号101","学号102","学号103"..."学号150"]
li = []
for i in range(101,151):
    li.append("学号{}".format(i))
print(li)

print("-----------------列表推导式------------------")
li2 = ["学号{}".format(i) for i in range(101,151)]
print(li2)

'''
关于日志的等级：
debug：调试日志
info：记录程序正常执行的关键信息
warning：输入警告信息
error:记录代码的错误信息（代码运行出错，但是程序还可以继续执行）
critical：记录代码更为严重的错误（程序运行崩溃，无法继续执行）
'''
import logging

logging.debug("小白输出debug级别的日志")
logging.info("小白输出info级别的日志")
logging.warning("小白输出warning级别的日志")
logging.error("小白输出error级别的日志")
logging.critical("小白输出critical级别的日志")

