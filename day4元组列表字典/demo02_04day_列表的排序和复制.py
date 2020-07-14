"""
============================
Author:柠檬班-木森
Time:2020/7/4   9:43
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
列表的其他方法
sort:排序
    # 升序排序  li.sort()

    # 降序排序  li.sort(reverse=True)
    
reverse：列表反转


copy:复制

    

"""

# 1、列表排序
# li = [1, 23, 44, 4545, 11, 22, 4, 2, 1, 33, 332]
# li = ['a', 'cccc', 'aaa', 'asas', 'das','11','AAA','B','C']
# 升序排序
# li.sort()

# 降序排序
# li.sort(reverse=True)
# print(li)

# 2、列表反转reverse
# 如何将一个列表中元素的位置反转
# li = [11, 22, '11', 'ccc', 111, 2222, 3333]
# print(li[::-1])
# li.reverse()
# print(li)

# 3,复制列表
li = [11, 22, 33]
li3 = li
li2 = li.copy()
li3.append(99)
print(li)
print(li2)
print(li3)

"""
#  扩展:代码中为什么有灰色的波浪线 ?
        不符合python的pep8编码规范
        ctrl+alt+L
        


# 代码中为什么有红色的波浪线 ?
        通常以为代码语法错误?(少写了,或者多写了什么东西)




"""
a = 111
b = 333


