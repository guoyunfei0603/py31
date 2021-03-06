"""
============================
Author:柠檬班-木森
Time:2020/8/4   21:17
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
需求：在执行用例的过程，记录日志(把日志记录到文件)
    日志收集器

封装一个创建日志收集器的方法


"""

import logging
from logging.handlers import TimedRotatingFileHandler


def create_logger():
    """创建日志收集器"""
    # 1、创建一个收集器
    log = logging.getLogger("lemon")
    log.setLevel("DEBUG")  # 设置收集日志的等级

    # 2、创建一个输出到文件的输出渠道(按时间轮转),
    fh = TimedRotatingFileHandler("log.log", when='d',
                                  interval=1, backupCount=7,
                                  encoding="utf-8")
    fh.setLevel("DEBUG")  # 设置输出等级
    log.addHandler(fh)  # 添加到收集器中

    # 3、创建一个输出到控制台的输出渠道
    sh = logging.StreamHandler()
    sh.setLevel("DEBUG")  # 设置输出等级
    log.addHandler(sh)  # 添加到收集器中

    # 4、设置日志输出格式
    formatter = "%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s"
    mate = logging.Formatter(formatter)

    fh.setFormatter(mate)
    sh.setFormatter(mate)

    return log


if __name__ == '__main__':
    log = create_logger()
    log.debug("python666")

