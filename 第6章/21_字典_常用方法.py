# coding=utf-8

# keys() 方法：用于获取字典中所有的键
# d1 = {'张三': 72, '李四': 60, '王五': 85}
# result = d1.keys()
# print(result)
# # keys方法的返回值不是list，而是一种叫做dict_keys的类型
# print(type(result))

# dict_keys和列表类似，可以被遍历，但要注意的是：它不能通过下标访问元素
# for item in result:
#     print(item)
# 张三
# 李四
# 王五
# print(result[0])  # TypeError：“dict_keys”对象不可下标

# 借助内置的list函数，可以将dict_keys转换成list
# l1 = list(result)
# print(type(l1), l1)  # <class 'list'> ['张三', '李四', '王五']
# for item in l1:
#     print(item)

# values() 方法：用于获取字典中所有的值
# d1 = {'张三': 72, '李四': 60, '王五': 85}
# result = d1.values()
# # values方法的返回值类型是：dict_values，它的特点和dict_keys一样
# print(result)  # dict_values([72, 60, 85])
# print(type(result))
#
# # dict_values和列表类似，可以被遍历，但要注意的是：它不能通过下标访问元素
# for item in result:
#     print(item)

# items方法：获取字典中所有的键值对（每组键值对以元组的形式呈现）
d1 = {'张三': 72, '李四': 60, '王五': 85}

# items方法返回的类型是：dict_items，它的特点也和dict_keys一样
result = d1.items()
print(result)  # dict_items([('张三', 72), ('李四', 60), ('王五', 85)])
print(type(result))

# dict_items和列表类似，可以被遍历，但要注意的是：它不能通过下标访问元素
for item in result:
    print(item)
    print(type(item))
    for content_item in item:
        print(content_item)
