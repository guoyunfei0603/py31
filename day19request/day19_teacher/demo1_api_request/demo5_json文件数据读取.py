"""
============================
Author:柠檬班-木森
Time:2020/8/11   21:51
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import json
from jsonpath import jsonpath

# 读取json文件中的数据，转换为python中的字典
with open("data.json", "r", encoding="utf-8") as f:
    res = json.load(f)

res = jsonpath(res, "$.toplists[1].id")
print(res)
