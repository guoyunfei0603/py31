"""
============================
Author:柠檬班-木森
Time:2020/7/21   21:18
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
异常处理：
try:
    有可能会出现错误的代码，放到try下面
except:
    当try里面的代码出错了，就会执行except里面的代码（可以在此处，处理异常）  
else:
    try里面的代码没有出现异常就会执行else
finally:
    不管try里面的代码是否出现异常，始终都会执行
    
# try里面的代码
1、涉及用户输入
2、涉及到文件操作
3、涉及到网络请求

通过异常捕获可以提高代码的容错性
"""

print("----------1--------")

print("----------2--------")

# try:
#     # 有可能会出现错误的代码，放到try下面
#     num = int(input("请输入一个数值："))
# except:
#     # 当try里面的代码出错了，就会执行except里面的代码（可以在此处处理异常）
#     print("您输入的不是数字！")

print("----------3--------")
# 捕获指定的异常类型,不同的异常类型做不同的处理
# try:
#     # 有可能会出现错误的代码，放到try下面
#     num = int(input("请输入一个数值："))  # ValueError
#     with open("demo01__路径处理的方法.py", 'r',encoding='utf8') as f:  # FileNotFoundError
#         f.read()
# except ValueError as e:
#     print("您输入的不是数字！")
#     print(e)
# except FileNotFoundError:
#     print("您打开的文件没找到！")

print("----------4--------")
# 所有的异常类型，做相同的处理
try:
    # 有可能会出现错误的代码，放到try下面
    num = int(input("请输入一个数值："))  # ValueError
    with open("demo01__路径处理的方法1.py", 'r', encoding='utf8') as f:  # FileNotFoundError
        f.read()
except Exception as e:
    print("代码错误信息为：", e)

print("----------5--------")
