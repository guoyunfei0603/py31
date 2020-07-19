"""
============================
Author:柠檬班-木森
Time:2020/7/16   21:11
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
enumerate:利用它可以同时获得序列类型数据的下标和值

eval:可以识别字符串中有效的python表达式(去除字符串的引号)

filter:过滤器函数



"""
# 打印列表中的每个元素以及下标
# li = ["aa", "bb", "cc", "dd"]
# # res = enumerate(li)
# for i, v in enumerate(li):
#     print(f"下标{i},值{v}")


#  eval
a = "[11,22,33,44]"

b = "{'a':11,'b':22}"

c = "77>99"

d = "print('hello python')"

res = eval(a)  # [11,22,33,44]
print(res, type(res))

res2 = eval(b)  # {'a':11,'b':22}
print(res2, type(res2))
res3 = eval(c)  # 77>99
print(res3)

eval(d)  # print('hello python')
