"""
============================
Author:柠檬班-木森
Time:2020/7/7   21:17
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
控制流程

顺序:从上往下一行一行执行
分支:条件语句
循环:循环语句


python的代码块处理:
    1, python是通过缩进来区分代码块的
    2,缩进通常是一个tab键(四个空格)


条件语句:
    if
    
    if--else
    
    if--elif--else


    if 条件1：
	    # 条件1成立是执行的代码
    elif 条件2：
        # 条件2成立执行的代码
    elif 条件3：
        # 条件3成立执行的代码
    else:
        # 以上条件不成立时执行的代码

注意点:
一个条件语句只有(必须)一个if,else(0个或者1个),elif(0个或者n个)




"""

# 需求一：用户输入考试成绩，请判断是否及格？

# score = float(input("请输入你的考试成绩:"))

# if score >= 60:
#     print("及格")


# if score >= 60:
#     print("考试及格:获得一个么么哒!")
#     print("考试及格:奖励100块!")
# else:
#     print("考试不及格:获得一个大嘴巴子!")
#     print("考试不及格:跪到天亮")


"""
需求三：请根据用户输入成绩，按以下等级区分：

- < 40 ：E
- 40-59：D
- 60-75：C
- 76-85：B
- 86-100：A

"""

score = float(input("请输入你的考试成绩:"))

# if 0 <= score < 40:
#     print("您的成绩为:E")
# elif 40 <= score <= 59:
#     print("您的成绩为:D")
# elif 60 <= score <= 75:
#     print("您的成绩为:C")
# elif 76 <= score <= 85:
#     print("您的成绩为:B")
# elif 86 <= score <= 100:
#     print("您的成绩为:A")
# else:
#     print("您输入的成绩有误!")
#
#
# print("程序执行结束!")


if 0 <= score < 40:
    print("您的成绩为:E")

if 40 <= score <= 59:
    print("您的成绩为:D")

if 60 <= score <= 75:
    print("您的成绩为:C")

if 76 <= score <= 85:
    print("您的成绩为:B")

if 86 <= score <= 100:
    print("您的成绩为:A")

print("程序执行结束!")
