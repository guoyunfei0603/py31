"""
============================
Author:柠檬班-木森
Time:2020/6/30   20:09
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
字符串(str类型):在python中引号包起来的叫做字符串
    
    1、字符串的定义：
        1、单引号
        2、双引号
        3、三引号：定义字符串的时候，可以自由的换行
        
        注意点：单引号和双引号定义字符串 没有任何的区别
     
    2、字符串的转义？
    \' :表示 '
    \" :表示 " 
    \n :表示 换行符
    \t :制表符
    
    3、关闭字符串转义？
    r:在字符串前面加个r
    
    
    
    

需求：字符串中如果有单引号怎么定义？  python'java

需求：字符串中如果有单引号和双引号怎么定义？  python'java"php


"""

s1 = '报告显示'
s2 = "123"
s3 = """
报告显示，2020年上半年，二手房访问热度高峰出现在3月份至5月份。
一线城市中，北京、上海、深圳二手房访问热度同比涨幅均超过10%。
其中，上海的二手房找房热度领先，其次为北京。

新一线城市中，重庆、成都、沈阳二手房访问热度排前三。
成都、长沙、东莞二手房访问热度同比涨幅超过一成。
分析认为，这些城市不仅经济增长速度快，
美食美景和舒适的生活氛围等也得到许多年轻人的青睐
"""

# print(s1, type(s1))
# print(s2, type(s2))
# print(s3, type(s3))

# 需求：字符串中如果有单引号怎么定义？  python'java
# s4 = "python'java"
# print(s4)

# 需求：字符串中如果有单引号和双引号怎么定义？  python'java"php
# s5 = """python'java"php"""
# print(s5)


# 字符串转义？  \ 可以对有特殊意义字符进行转义
# s6 = 'python\'java\"php'
# print(s6)

# 换行符：\n
# s7 = "pyhton\njava\nphp"
# print(s7)

# 水平制表符:\t
# s8 = "pyhton1\t\tjava\t\tphp"
# s9 = "pyhton\t\tjava44\t\tphp444"
# s10 = "pyhton2\t\tjava333\t\tphp"
# print(s8)
# print(s9)
# print(s10)

# 如果去关闭字符串转义？

file_path = r"C:\project\py31_class\py31_02day\task_01day.py"

print(file_path)