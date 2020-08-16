"""
============================
Author:小白31
Time:2020/8/13 0:28
E-mail:1359239107@qq.com
============================
"""
'''
常见的接口请求参数类型：


1、查询字符串参数：常用于get请求（其他的请求方法用的少），参数会直接拼接在url地址后面
    requests发送请求，传递查询字符串参数，要使用params

2、json类型的参数：
     请求参数类型为 Content-Type：application/json,
     requests发送请求，传递json参数，就应该使用json去传递

3、表单类型的参数
    请求参数类型：content-type: application/x-www-form-urlencoded
    requests发送请求，传递表单参数，就应该使用data去传递

4、文件上传：
    请求参数类型：content-type: multipart/form-data
    文件参数要使用files进行传递
    文件参数的组装：
        {"参数名": ("文件名", open以rb模式打开文件, "文件类型")}
        [("参数名", ("文件名", open以rb模式打开文件, "文件类型"))]
        
响应对象response：

一、http响应码：response.status_code

二、返回的数据提取：
1、text属性（str）:获取的是原生的json字符串
2、content属性(bytes)：可以使用decode指定编码转换为字符串
3、json()方法(dict)：获取到的是json转换的字典/列表


json类型的数据和  python中数据的对比
      json        python       
{}:  对象           字典
[]:  数组           列表
空    null         None
布尔  false        False
      true         True
'''