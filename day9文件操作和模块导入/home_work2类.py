"""
============================
Author:小白31
Time:2020/7/19 20:58
E-mail:1359239107@qq.com
============================
"""
'''
# 文件中数据
url:www.baidu.com,mobilephone:13760246701,pwd:123456
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
​
# 要求一： 请把这些数据读取出来，到并且存到list中，格式如下
[
{'url': 'www.baidu.com', 'mobilephone': '13760246701', 'pwd': '123456'},
{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
{'url': 'www.baidu.com', 'mobilephone': '15678934552', 'pwd': '234555'},
{'url': 'www.baidu.com', 'mobilephone': '15678934553', 'pwd': '234555'},
{'url': 'www.baidu.com', 'mobilephone': '15678934554', 'pwd': '234555'}
]
'''

'''
为了简写一部分代码，就写成类了
'''


class test_data:

    def read_data(self, file):
        with open(file, 'r', encoding='utf-8')as f:
            t1 = f.readlines()

        list1 = []
        dic = {}
        for i in t1:
            # 去掉\n 以 , 分割
            str1 = i.strip('\n').split(',')
            # 再遍历
            for j in str1:
                # print(j)  # url:www.baidu.com
                #     key = j.split(':')[0]
                #     value = j.split(':')[1]
                # dic = {key: value}
                dic[j.split(':')[0]] = j.split(':')[1]

            list1.append(dic)

        return list1

    # 要求二：将上述数据再次进行转换，转换为下面这种字典格式格式​
    # {
    #    'data1':{'url': 'www.baidu.com', 'mobilephone': '13760246701', 'pwd': '123456'},
    #    'data2':{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
    #    'data3':{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
    #    'data4':{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
    #    'data5':{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'}
    # }

    def change_data(self):
        dic2 = {}
        for j in range(1, 6):
            s = 'data' + str(j)
            for i in self.read_data('data2.txt'):
                dic2[s] = i
        return dic2

# 防止其他模块导入 调用当前模块里面的方法  使用main
if __name__ == '__main__':
    test = test_data()
    # 第一题
    res1 = test.read_data('data2.txt')
    print(res1)
    # 第二题
    res2 = test.change_data()
    print(res2)
