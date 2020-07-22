"""
with: 通过with去打开文件，操作完了之后会自动关闭文件

"""

with open("017CD1CE.gif", 'rb') as f:
    content = f.read()

with open("002.gif", 'wb') as f2:
    f2.write(content)




# # 图片的复制
# # 第一步：打开文件
# f1 = open("apicases.xlsx", 'rb')
# f2 = open("musen.xlsx", "wb")
# # 第二步：读取内容，写入新文件
# content = f1.read()
# f2.write(content)
# # 第三步：关闭文件
# f1.close()
# f2.close()
