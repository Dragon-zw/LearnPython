# coding=utf-8

# 定义有内容的列表
# 不能使用 list 的名称，因为 list 是 Python 的内置函数！
list1 = [34, 56, 21, 56, 11]
list2 = ['北京', '尚硅谷', '你好啊']
list3 = [23, '尚硅谷', True, None]
# 嵌套列表并不需要写在最后的位置
list4 = [23, '尚硅谷', True, None, [100, 200, 300]]

# 打印列表
print(list1, type(list1))
print(list2, type(list2))
print(list3, type(list3))
print(list4, type(list4))

# 定义空列表（列表中的数据，可以通过后期的特定写法进行填充！）
list5 = []
list6 = list() # list() 是 Python 的内置函数！
print(list5, type(list5))
print(list6, type(list6))
