"""
============================
Author:柠檬班-木森
Time:2020/7/2   20:30
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
# 字符串的常用方法

"""
索引（下标）
python musen
0123456789




"""
# 1、find：查找字符串,返回的是字符串的索引（下标）,找不到返回的是-1
# 注意：如果存在多个，返回的是第一个
# s = "python musen"
# res = s.find('h')
# print(res)


# 2、count：计算字符的个数
# s2 = "abcdddffttttt"
# res2 = s2.count('a')
# print(res2)


# 3、replace:替换字符串的内容
# 默认所有符合要求的都替换，可以通过第三个参数指定替换的次数
# s3 = "python php java c++ java c++ java"
# res3 = s3.replace('java', 'python', 1)
# print(res3)


# 4、split：字符串分割
# s4 = "data:111,url:wwww.baidu,mobile:1311121324"
# res4 = s4.split(',')
# print(res4)


# 5、upper:把小写的字母转换为大写
# method = "post"
# print(method.upper())
# 工作可以会用到的场景
# print("POST" == method.upper())

# 6、lower：把大写的字母转换为小写
# str6 = "MUSEN"
# print(str6.lower())

# 7、strip:去除字符串首尾的空格
# str7 = "    python:666    java:8888       "
# print(str7.strip())

# 通过替换来去除
# res8 = str7.replace(" ","")
# print(res8)

# 8、join:字符串拼接
# a = 'hello'
# b = 'python18'
# c = '!'
# res8 = "-*-".join([a, b, c])  # 和 a +"-*-" + b + "-*-" +c效果是一样的
# print(res8)

# 9、format
