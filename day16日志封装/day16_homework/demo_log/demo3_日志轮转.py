"""
============================
Author:小白31
Time:2020/8/5 23:40
E-mail:1359239107@qq.com
============================
"""
""" 日志输出格式 """


import logging
from logging.handlers import RotatingFileHandler,TimedRotatingFileHandler

# 第一步：创建日志收集器
# 1. 定义一个日志收集器
my_log = logging.getLogger(name="xiaobai") # 如果不指定name,默认是 root
# 2. 设置日志收集器等级
my_log.setLevel("DEBUG") # 必须大写

# 第二步: 创建日志输出渠道: 控制台/文件

# 渠道一：输出到控制台
# 1. 创建一个输出到控制台的输出渠道
sh = logging.StreamHandler()
# 2. 设置输出到控制台的输出等级
sh.setLevel("DEBUG")

# 渠道二：输出到文件
# fh = logging.FileHandler(filename="xiaobai.log", mode="a", encoding="utf-8")
# fh.setLevel("INFO")

# -----根据文件大小进行轮转------
# fh = RotatingFileHandler(filename='py31.log', mode='a', maxBytes=10, backupCount=2, encoding='utf-8')
# fh.setLevel("DEBUG")

# =====根据时间进行轮转=========
fh = TimedRotatingFileHandler(filename='xiaobai31.log',
                         when='D',
                         interval=1,
                         backupCount=3,
                         encoding=None)
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
