def login_check(username=None, password=None):
    """
    登录校验的函数
    :param username: 账号
    :param password:  密码
    :return: dict type
    """
    if username != None and password != None: # 注意这里的None 不是空字符串，测试用例要写成None
        if 6 <= len(username) <= 18 and 6 <= len(password) <= 18:
            if username == 'python31' and password == 'lemonban':
                return {"code": 0, "msg": "登录成功"}
            else:
                return {"code": 1, "msg": "账号或密码不正确"}
        else:
            return {"code": 1, "msg": "账号和密码必须在6-18位之间"}
    else:
        return {"code": 1, "msg": "所有的参数不能为空"}


if __name__ == '__main__':
    res = login_check("python31", "lemonban")
    print(res)
