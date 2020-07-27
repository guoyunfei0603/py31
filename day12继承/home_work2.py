"""
============================
Author:小白31
Time:2020/7/26 17:54
E-mail:1359239107@qq.com
============================
"""
'''
2、有一组数据，如下格式：
{'case_id': 1, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过','excepted': '通过'},

定义一个如下的类，
请通过setattr将上面字典中的键值对，分别设置为类的属性和属性值，
键作为属性名，对应的值作为属性值
class CaseData:
    pass
'''


class CaseData:
    pass


dic = {'case_id': 1, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过', 'excepted': '通过'}
for k,v in dic.items():
    setattr(CaseData,k,v)

# setattr(CaseData,'caseid',100)
print(CaseData.__dict__)