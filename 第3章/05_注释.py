# coding=utf-8
"""这是一个注释的 Python 文件"""

# name 是张三的名字
name = '张三'
# age 是张三的年龄
age = 18
# weight 是张三的体重(单位：kg)
weight = 65.2
# 打印语句
print(name, age, weight)  # 注释内容
'''
这是一些常量的设置，多行注释本质是字符串，起到了注释一样的作用
ADULT_AGE 是成人法定的年龄
MOUNTS_IN_YEAR 是一年中的几个月
MAX_USERS 是最大同时在线的人数
'''
"""
依旧是多行注释的内容，使用双引号引起来。
"""
ADULT_AGE = 18
MOUNTS_IN_YEAR = 12
MAX_USERS = 20

# 字符串没有起到和注释一样的作用，而是作为值赋值给 message
message = '''
这是一些常量的设置
ADULT_AGE 是成人法定的年龄
MOUNTS_IN_YEAR 是一年中的几个月
MAX_USERS 是最大同时在线的人数
'''
print(message)
