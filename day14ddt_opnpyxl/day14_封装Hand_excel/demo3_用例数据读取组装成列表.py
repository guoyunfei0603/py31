"""
============================
Author:小白31
Time:2020/8/2 21:36
E-mail:1359239107@qq.com
============================
"""
import openpyxl

wb = openpyxl.load_workbook("test_data.xlsx")

sh = wb["login"]

res  = list(sh.rows)

# 获取第一行的title
title = []
for i in res[0]:
    title.append(i.value)

print(title)

case_data = [] # 存放用例数据
# 获取除第一行以外的所有行数据
for i in res[1:]:
    data = []
    for j in i:
        data.append(j.value)
    res = dict(zip(title,data))
    case_data.append(res)
print(case_data)