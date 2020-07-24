"""
============================
Author:柠檬班-木森
Time:2020/7/23   20:17
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
异常处理：


try---except:


try--except---else:


try--except---else---finally:


"""
# name ="musen"
# dic={}
# 一个except 捕获指定的多个异常类型
# try:
#     print(name)
#     a = 10/2
#     print(dic['name'])
# except (NameError,ZeroDivisionError,KeyError) as e:
#     print(e)


# Exception 捕获所有的异常类型
# try:
#     print(name)
#     a = 10 / 0
#     print(dic['name'])
# except Exception as e:
#     print(e)



# try:
#     print(name)
# except Exception as e:
#     print("代码报错了")
#     print(e)
# else:
#     print("try里面的代码没有出错")
#

name = 111

try:
    a = 100/5
    print(name)
    f = open("task_10day.py",'r')
    f.write([111,33,444])

except NameError as e:
    print("代码报错了")
    print(e)
else:
    # 代码不出错才会执行
    print("else:try里面的代码没有出错")
finally:
    # 不管出不出错都会执行
    print("------finally-------------")
    f.close()
print("888888888888888888888888")











