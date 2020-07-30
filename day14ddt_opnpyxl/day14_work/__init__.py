"""
============================
Author:小白31
Time:2020/7/30 22:46
E-mail:1359239107@qq.com
============================
"""
import openpyxl

# 第一步：将excel文件加载到一个工作簿对象中
wb = openpyxl.load_workbook("cases.xlsx")

# 第二步：选择文件中的表单
sh = wb["login"]

# 第三步：读取内容
res = sh.cell(row=1,column=1)
# print(res.value)

