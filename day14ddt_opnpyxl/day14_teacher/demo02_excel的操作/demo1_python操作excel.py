"""
============================
Author:柠檬班-木森
Time:2020/7/30   20:47
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import openpyxl

"""
excel操作三大对象：
工作簿：一个excel文件会被加载为一个工作簿对象Workbook
工作表：excel文件每个sheet表达会被加载成一个工作表对象(sheet)
单元格：工作表中的每一个格子就是一个表格对象（cell）

pip install 包名 -i 

"""
# 第一步：将excel文件加载到一个工作簿对象中
wb = openpyxl.load_workbook("musen.xlsx")

# 第二步：选择文件中的表单
sh = wb["login"]
print(sh)

# 第三步：读取内容
res = sh.cell(row=1,column=1)
print(res.value)
