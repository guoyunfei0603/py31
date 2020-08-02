"""
============================
Author:小白31
Time:2020/8/2 22:03
E-mail:1359239107@qq.com
============================
"""
# 生成1-100到列表
# li = []
# for i in range(1,101):
#     li.append(i)
#
# print(li)
#
# print(list(range(1,101)))

# 生成 ["学号101","学号102","学号103"..."学号150"]
li = []
for i in range(101,151):
    li.append("学号{}".format(i))
print(li)

print("-----------------列表推导式------------------")
li2 = ["学号{}".format(i) for i in range(101,151)]
print(li2)