"""
============================
Author:小白31
Time:2020/7/24 22:57
E-mail:1359239107@qq.com
============================
"""
# 4、封装一个学生类，(自行分辨定义为类属性还是实例属性)
# 属性：，身份(学生)
# 姓名，年龄，性别，英语成绩，数学成绩，语文成绩，
# 方法一：计算总分，
# 方法二：计算三科平均分，
# 方法三：打印学生的个人信息。

'''
考虑到可重复性，所以就都定义为实例属性了
'''


class student:
    def __init__(self, job, name, age, sex, english_grade, math_grade, language_grade):
        self.job = job
        self.name = name
        self.age = age
        self.sex = sex
        self.english_grade = english_grade
        self.math_grade = math_grade
        self.language_grade = language_grade

    # 计算总分
    def my_sum(self):
        # sum 求和
        # res = sum([self.english_grade,self.math_grade,self.language_grade])
        res = self.english_grade + self.math_grade + self.language_grade
        return res

    # 计算平均分
    def my_avg(self):
        res = self.my_sum() / 3
        return res

    # 个人信息
    def my_info(self):
        res = f"我的姓名是{self.name},年龄是{self.age},性别是{self.sex},总分是{self.my_sum()},平均分是{self.my_avg()}"
        return res
    # def __init__(self,job,name,age,sex,english_grade,math_grade,language_grade):


s1 = student('学生', "小白", '22', '男', 100, 99, 98)
print(s1.my_sum())
print(s1.my_avg())
print(s1.my_info())


# 5、封装一个测试用例类(自行分辨定义为类属性还是实例属性)，
# 属性：用例编号
# url地址
# 请求参数
# 请求方法
# 预期结果
# 实际结果
class test_case:
    def __init__(self, case_id, url, data, method, expected, result):
        self.case_id = case_id
        self.url = url
        self.data = data
        self.method = method
        self.expected = expected
        self.result = result

    def test_01(self):
        print(self.case_id, self.url, self.data, self.method, self.expected, self.result)


test_case(1001, "www.baidu.com", "{'name':'小白'}", 'POST', '16', '18').test_01()
