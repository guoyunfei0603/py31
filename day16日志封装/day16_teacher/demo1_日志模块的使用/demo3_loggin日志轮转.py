"""
============================
Author:柠檬班-木森
Time:2020/8/1   11:23
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

"""
日志轮转：


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
# 根据文件大小进行轮转

# fh = RotatingFileHandler(filename="lemon.log",
#                          mode='a',
#                          maxBytes=512,
#                          backupCount=5,
#                          encoding="utf-8", )

# 根据时间进行轮转
fh = TimedRotatingFileHandler(encoding="utf-8",
                              filename="py31.log",
                              backupCount=7,
                              when='s',
                              interval=2,
                              )

fh.setLevel("INFO")
my_log.addHandler(fh)

# 第三步：设置日志输出格式
formats = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
mat = logging.Formatter(formats)

fh.setFormatter(mat)
sh.setFormatter(mat)

my_log.debug("----debug-----日志")
my_log.info("----info-----日志")
my_log.warning("----warning-----日志")
my_log.error("----error-----日志")
my_log.critical("---critical-----日志")
