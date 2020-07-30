"""
============================
Author:柠檬班-木森
Time:2020/7/30   21:24
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
一次性读取一个表单的数据



"""
import openpyxl

# 第一步：将excel文件加载到一个工作簿对象中
wb = openpyxl.load_workbook("musen.xlsx")

# 第二步：选择文件中的表单
sh = wb["login"]

res = list(sh.rows)

for item in res:
    for c in item:
        print(c.value,end="    ")

    print()

