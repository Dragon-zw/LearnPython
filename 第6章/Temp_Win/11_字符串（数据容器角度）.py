# coding=utf-8

# 字符串的下标
# msg = 'welcome to atguigu'
# print(msg[3])
# print(msg[-1])

# 字符串中的字符是不可修改
# msg = 'welcome to atguigu'
# msg[0] = 'a'

# 字符串不能嵌套
# msg = 'welcome to'hello' atguigu'
# msg = 'welcome to"hello" atguigu'
# msg = 'welcome to\'hello\' atguigu'
# 转义字符不会有下标！
# print(msg[11])

# 字符串的常用方法
# index 方法：获取指定字符，在字符串中第一次出现的下标
# msg = 'welcome to atguigu'
# result = msg.index('t')
# print(result)

# split 方法：将字符串按照指定字符进行分隔，并将分隔后的内容存入一个列表
# msg = 'welcome@to@atguigu'
# result = msg.split('@')
# print(msg)
# print(result)
# 如果是使用其他的不存在的分隔符，不会报错。

# msg = 'welcome to atguigu'
# result = msg.split(' ')
# print(msg)
# print(result)

# replace 方法：将字符串中的某个字符片段，替换成目标字符串（不修改原字符串，返回新字符串）
# msg = 'welcome to atguigu'
# result = msg.replace('g', 'G')
# print(msg)
# print(result)
# result = msg.replace('atguigu', '尚硅谷')
# print(result)

# count 方法：统计指定字符，在字符串中出现的次数
# msg = 'welcome to atguigu'
# result = msg.count('g')
# print(result)

# strip 方法：从某个字符串中删除：指定字符串中的任意字符
# 规则：从字符串两端开始删除，直到遇到第一个不在字符串中的字符就停下
# msg = '666尚6硅6谷666'
# result =  msg.strip('6')
# print(result)

# msg = '1234尚12硅34谷4321'
# result = msg.strip('1324')
# print(result)
#
# msg = '34215尚12硅34谷4132'
# result = msg.strip('5432')
# print(result)
#
# msg = '  尚硅谷  '
# result = msg.strip()
# # 相当于：result = msg.strip(' ')
# print(result)

# 字符串的常用函数
# len 函数：统计字符串中字符的个数（字符串长度）
# msg = 'welcome to atguigu'
# result = len(msg)
# print(result)

# 字符串的循环遍历
msg = 'welcome to atguigu'

# 使用 while 循环
index = 0
while index < len(msg):
    print(msg[index])
    index += 1

# 使用 for 循环
for item in msg:
    print(item)