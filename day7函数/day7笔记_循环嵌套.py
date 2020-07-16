"""
============================
Author:小白31
Time:2020/7/16 8:08
E-mail:1359239107@qq.com
============================

"""
# python之禅：扁平胜于嵌套

# while 嵌套  --用的较少
# while True:
#     num = int(input('请输入一个数字：'))
#     n = 0
#     while n<=num:
#         print(n)
#         n+=1
#     break

# for循环  --用的较多    遍历测试数据
# 打印一个5 * 5 的三角形

'''
外层 i 是 *的行数，控制打印几行
内层 j 是 *的个数，控制每行打印几个*
'''
# for i in range(1,6):
#     print("第{}行".format(i))
#     for j in range(i):
#         print("*",end="")

'''
print() 源码 ： print(self, *args, sep=' ', end='\n', file=None)
end='\n' 有默认参数，是换行
'''
for i in range(1,6):
    for j in range(i):
        print("* ",end="")  # end="" 不换行输出
    print() # print()的作用是，内层 j 打印完后，换行
