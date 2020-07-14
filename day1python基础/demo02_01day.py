"""
============================
Author:柠檬班-木森
Time:2020/6/23   20:31
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
变量的定义:
变量先定义，才能使用，(不然就会报错提示，变量没有定义)

变量的命名规范：
1、变量只能使用数字、字母、下划线组成
2、变量不能使用数字开头
3、不能使用python中的关键字
    'False', 'None', 'True', 'and', 'as',
    'assert', 'async', 'await', 'break', 'class',
    'continue', 'def', 'del', 'elif', 'else',
    'except', 'finally', 'for', 'from', 'global',
    'if', 'import', 'in', 'is', 'lambda', 
    'nonlocal', 'not', 'or', 'pass', 'raise',
    'return', 'try', 'while', 'with', 'yield'
    
注意点：python中严格区分大小写字母：   and  和 And 是不一样的

变量的命令风格：
    1、下划线命名法：单词和单词之间使用下划线隔开(推荐使用这种)
        例子：age_max = 19
             age_min = 17
             age_min_name = 'rabbit兔'

    2、驼峰命名法：
        1、大驼峰：每个单词的第一个字母大写
            例子、AgeMax、AgeMin
        2、小驼峰：第一个单词首字母小写，后面的每个单词的第一个字母大写
            例子：ageMax、ageMinName



标识符：在python中只要自己起的名字都叫标识符
    标识符：变量、函数名、类名、模块名（py文件）、包名

    标识符的命令风格：
        1、下划线命名法：单词和单词之间使用下划线隔开
            例子：age_max = 19
                 age_min = 17
                 age_min_name = 'rabbit兔'
        2、驼峰命名法：
            1、大驼峰：每个单词的第一个字母大写
                例子、AgeMax、AgeMin
            2、小驼峰：第一个单词首字母小写，后面的每个单词的第一个字母大写
                例子：ageMax、ageMinName   
                     
    标识符的命名规范：
        1、变量只能使用数字、字母、下划线组成
        2、变量不能使用数字开头
        3、不能使用python中的关键字



"""

name = "木森"
age = 18
sex = "男"

print(name, age, sex)

# 姓名 = '木森'     # 错误示范
# 1name = '木森'   # 错误示范
# and = "木森"      # 错误示范


And = 18


# 查看python中的关键字
import keyword

print(keyword.kwlist)


