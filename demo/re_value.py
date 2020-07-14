# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 19:30
# @Author  : guoyunfei.0603
# @File    : re_value.py
import re

str = "name='csrfmiddlewaretoken' value='UG7RgpptMSUz1S7q3plrzhr0PgWAifrPnPsPvWscIafGiKJOo4SI49Pt2VgvzFA9'"
a = re.findall("name='csrfmiddlewaretoken' value='(.+?)'",str)
print(a[0])