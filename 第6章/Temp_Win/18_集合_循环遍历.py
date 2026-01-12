# coding=utf-8

# 定义集合
s1 = {10, 20, 30, 40, 50, 60}

# 集合不能使用while循环遍历（以下是错误示例）
# index = 0
# while index < len(s1):
#     print(s1[index])
#     index += 1

# 集合可以使用for循环遍历
for item in s1: # item 是临时变量，每次循环都会将集合中的元素取出来，赋给 item
    print(item)