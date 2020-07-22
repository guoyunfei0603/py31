"""
在python中读取文件
open(文件名，打开文件的模式,encoding="utf-8")


注意点：
    被打开的文件和当前文件在同一路径下，可以写文件名
    被打开的文件和当前文件在不在同一路径下，可以写文件完整的路径


"""
# 1、打开
f = open(r"C:\project\py31_class\py31_01day\test01day.txt", "r", encoding="utf-8")

# 2、读取所有的内容
content = f.read()

print(content)

# 3、关闭文件
f.close()
