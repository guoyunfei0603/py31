"""
============================
Author:小白31
Time:2020/8/5 23:44
E-mail:1359239107@qq.com
============================
"""
import logging

# 第一步：创建日志收集器
# 1. 定义一个日志收集器
my_log = logging.getLogger(name="xiaobai")
# 2. 设置日志收集器等级
my_log.setLevel("DEBUG") # 必须大写

# 第二步: 创建日志输出渠道: 控制台/文件

# 渠道一：输出到控制台
# 1. 创建一个输出到控制台的输出渠道
sh = logging.StreamHandler()
# 2. 设置输出到控制台的输出等级
sh.setLevel("DEBUG")

# 渠道二：输出到文件
fh = logging.FileHandler(filename="xiaobai.log", mode="a", encoding="utf-8")
fh.setLevel("INFO")



# 第三步: 将输出渠道添加到收集器中
my_log.addHandler(sh)
my_log.addHandler(fh)

#---------------设置日志输出格式-------------------------
formats = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
mat = logging.Formatter(formats)

fh.setFormatter(mat)
sh.setFormatter(mat)





my_log.debug("----debug-----日志")
my_log.info("----info-----日志")
my_log.warning("----warning-----日志")
my_log.error("----error-----日志")
my_log.critical("---critical-----日志")
