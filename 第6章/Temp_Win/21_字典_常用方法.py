# coding=utf-8

# keys 方法：用于获取字典中所有的键
d1 = {'张三': 72, '李四': 85, '王五': 65}

# keys方法的返回值不是list，而是一种叫做dict_keys的类型
# print(type(result), result)  # <class 'dict_keys'> dict_keys(['张三', '李四', '王五'])

# keys方法的返回值不是list，而是一种叫做dict_keys的类型
result = d1.keys()
print(result)
print(type(result))  # <class 'dict_keys'>

# dict_keys和列表类似，可以被遍历，但要注意的是：它不能通过下标访问元素
for item in result:
    print(item)
# dict_keys 不能通过下标访问元素
# print(result[0])

# 借助内置的list函数，可以将dict_keys转换成list
l1 = list(result)
print(l1)
print(type(l1))

# 打印分隔符
print('*' * 50)

# values方法：获取字典中所有的值
d1 = {'张三': 72, '李四': 85, '王五': 65}
# values方法的返回值类型是：dict_values，它的特点和dict_keys一样
result = d1.values()
print(result)  # dict_values([72, 85, 65])
print(type(result))  # <class 'dict_values'>

# 打印分隔符
print('*' * 50)

# items方法：获取字典中所有的键值对（每组键值对以元组的形式呈现）
d1 = {'张三': 72, '李四': 85, '王五': 65}

# items方法返回的类型是：dict_items，它的特点也和dict_keys一样
result = d1.items()
print(result)  # dict_items([('张三', 72), ('李四', 85), ('王五', 65)])
print(type(result))  # <class 'dict_items'>

# 借助内置的tuple函数，可以将dict_items转换成tuple
t1 = tuple(result)
print(t1)
print(type(t1))
# 借助内置的list函数，可以将dict_items转换成list
l1 = list(result)
print(l1)
print(type(l1))
