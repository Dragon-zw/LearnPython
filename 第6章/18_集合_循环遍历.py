# coding=utf-8

s1 = {10, 20, 30, 40, 50}
# 集合不能使用 while 循环遍历，因为集合是无序的（错误的示例）
# index = 0
# while index < len(s1):
#     print(s1[index])
#     index += 1
# TypeError: 'set' object is not subscriptable

# 使用while的话可以使用pop进行遍历，不过就不是原集合了，需要先赋值一个新集合

# 使用 for 循环
for item in s1: # 集合的元素是无序的，不能通过索引来获取元素
    print(item)
