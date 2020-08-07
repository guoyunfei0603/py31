"""
============================
Author:柠檬班-木森
Time:2020/8/1   11:23
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import logging

"""
关于日志的等级：
debug：调试日志
info：记录程序正常执行的关键信息
warning：输出警告信息
error:记录代码的错误信息（代码运行出错，但是程序还可以继续执行）
critical：记录代码更为严重的错误（程序运行崩溃，无法继续执行）


日志收集器：
    logging模块默认的日志收集器是root
    自定义日志收集器：
    
    收集器也可以设置日志收集的等级



日志输出渠道：
    1、输出到文件
    2、输出到控制台

    输出渠道可以设置输出日志的等级


"""
# 第一步：创建日志收集器
# 1、定义一个日志收集器
my_log = logging.getLogger("musen")
# 2、设置收集器等收集等级
my_log.setLevel("DEBUG")

# 第二步：创建日志输出渠道（输出到控制台）

# 渠道一：输出到控制台
# 1、创建一个输出到控制台的输出渠道
sh = logging.StreamHandler()
# 2、设置输出到控制台的输出等级
sh.setLevel("ERROR")
# 3、将输出渠道添加到收集器中
my_log.addHandler(sh)

# 渠道二：输出到文件
# 输出到文件的输出渠道
fh = logging.FileHandler(filename="musen.log", mode="a", encoding="utf-8")
fh.setLevel("INFO")
my_log.addHandler(fh)







my_log.debug("----debug-----日志")
my_log.info("----info-----日志")
my_log.warning("----warning-----日志")
my_log.error("----error-----日志")
my_log.critical("---critical-----日志")
