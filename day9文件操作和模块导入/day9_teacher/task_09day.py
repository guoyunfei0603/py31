"""
============================
Author:柠檬班-木森
Time:2020/7/20   10:10
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""


def work1():
    # 第一步：读取数据,每一行作为一个元素放到列表中
    with open('data.txt', encoding='utf8') as f:
        datas = f.readlines()
    # 第二步：将数据转换为字典
    title = []
    data = []
    for i in range(len(datas)):
        title.append("data{}".format(i))
        data.append(datas[i].replace("\n", ""))
    dic = dict(zip(title, data))
    return dic


def work2():
    # 第一步：读取数据,每一行作为一个元素放到列表中
    with open('cases.txt', 'r') as f:
        datas = f.readlines()
        print(datas)
    # 第二步：将数据转换为列表
    # 创建一个空列表
    cases = []
    # # 遍历出来每一行数据
    for i in datas:
        i = i.replace('\n', '')
        #     # 将该行数据使用split按，进行分割,得到一个列表
        itme = i.split(',')
        # 创建一个空字典，用例存放该行数据
        dic = {}
        # 遍历分割后的列表，
        for j in itme:
            # 将遍历出来的数据，按:分割，得到key,value,然后加入到字典中
            key = j.split(':')[0]
            value = j.split(':')[1]
            dic[key] = value
        # 将该行数据加入到列表中
        cases.append(dic)
    # # 完成转换之后，将转换后的数据 进行返回
    return cases


def work32(datas):
    # 第一步：读取数据,每一行作为一个元素放到列表中
    # 第二步：将数据转换为字典
    dic = {}
    for i in range(len(datas)):
        dic["data{}".format(i + 1)] = datas[i]
    return dic


def work3():
    try:
        # 读取文件中注册用户的数据
        with open('users.txt', 'r', encoding='utf8') as f:
            # 读取内容,使用eval识别字符串中的列表
            users = eval(f.read())
    except:
        users = []

    # 注册功能代码（上次作业写的，不需要改动）
    id = input('请输入新账号:')  # 输入账号
    pwd1 = input('请输入密码：')  # 输入密码
    pwd2 = input('请再次确认密码：')  # 再次确认密码

    for user in users:  # 遍历出所有账号，判断账号是否存在
        if id == user['uid']:
            print('该账户已存在')  # 账号存在，
            break
    else:
        # 判断两次密码是否一致
        if pwd1 == pwd2:
            users.append({'uid': id, 'pwd': pwd1})
            print('注册成功！')

        else:
            print('注册失败，两次输入的密码不一致')

    # 程序运行结束后，将所有用户的数据写入文件
    with open('users.txt', 'w', encoding='utf8') as f:
        # 将列表转换为字符串,写入文件
        f.write(str(users))


if __name__ == '__main__':

    # r1 = work1()
    # print(r1)

    # res = work2()
    # print(res)


    # print(work32(res))

    work3()
