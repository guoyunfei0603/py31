"""
============================
Author:小白31
Time:2020/8/2 21:30
E-mail:1359239107@qq.com
============================
"""
import openpyxl

wb = openpyxl.load_workbook("test_data.xlsx")

sh = wb["login"]
# 获取所有行
res = list(sh.rows)

for i in res:  # 遍历所有行
    for j in i:  # 遍历每一行的单元格
        print(j.value,end=" ")
    print()
