"""
============================
Author:柠檬班-木森
Time:2020/8/1   11:23
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import logging

"""
关于日志的等级：
debug：调试日志
info：记录程序正常执行的关键信息
warning：输入警告信息
error:记录代码的错误信息（代码运行出错，但是程序还可以继续执行）
critical：记录代码更为严重的错误（程序运行崩溃，无法继续执行）
"""
logging.debug("这个是木森输出的debug级别的日志")
logging.info("这个是木森输出的debug级别的日志")
logging.warning("这个是木森输出的debug级别的日志")
logging.error("这个是木森输出的debug级别的日志")
logging.critical("这个是木森输出的debug级别的日志")

# import openpyxl
# wb = openpyxl.load_workbook(r"C:\project\py31_class\py31_15day\task_14day\cases.xlsx")
# sh = wb.get_sheet_by_name("login")
# print(sh.cell(1,1).value)

