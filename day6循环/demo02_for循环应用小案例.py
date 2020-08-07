"""
============================
Author:柠檬班-木森
Time:2020/7/9   20:48
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
range():
range(n):默认生成一个 0到n-1的整数序列，对于这个整数序列，我们可以通过list()函数转化为列表类型的数据。
range(n,m)：默认生成一个n到m-1的整数序列，对于这个整数序列，我们可以通过list()函数转化为列表类型的数据。
range(n,m,k)：相当于其他函数里面的for循环。n 初始值  m 结束值 ， k 步长，会生成初始值为n,结束值为m-1,递减或者是递增的整数序列。


break：强制性的跳出循环
continue: 中止当前本轮循环，开启下一轮循环(执行到continue，直接回到条件判断的地方)



"""

# 批量判断成绩是否及格
# li = [78, 32, 55, 77, 88, 90, 54, 24, 67, 39]
#
# for i in li:
#     if i >= 60:
#         print(f"您的成绩是{i},考试及格")
#     else:
#         print(f"您的成绩是{i},考试不及格")


# 案例二：打印100遍hello python

# li = [1, 2, 3, 4, 5, 6, 7]

# for i in range(1, 101):
#     print(f"这个是第{i}遍:hello python")

# range的使用：
# res = list(range(100))
# print(res)


# for 循环中的break和continue

# break
# for i in range(1, 10):
#     if i == 6:
#         break
#     print(f"这个是第{i}遍:hello python")
#
# print("--for外面-----")


# continue
# for i in range(1, 10):
#     if i == 6:
#         continue
#     print(f"这个是第{i}遍:hello python")
#
# print("--for外面-----")
