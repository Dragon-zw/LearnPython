# coding=utf-8

# 以下这五个函数:既能定义对应的【空容器】，又能将【其他类型】转换为对应的数据类型

# 1.1ist 函数:1.定义空列表。2.将【可迭代对象】转换为列表
# # 定义空列表
# l1 = list()
# print(type(l1), l1)
# # 将【可迭代对象】转换为列表
# res1 = list(range(8))
# res2 = list('欢迎来到尚硅谷')
# res3 = list({10, 20, 30, 40, 50})
# res4 = list({'张三': 75, '李四': 60, '王五': 85})
# res5 = list({'张三': 75, '李四': 60, '王五': 85}.keys())
# res6 = list({'张三': 75, '李四': 60, '王五': 85}.values()) # 使用字典的 values() 方法
# res7 = list({'张三': 75, '李四': 60, '王五': 85}.items()) # 使用字典的 items() 方法
# print(type(res1), res1)
# print(type(res2), res2)
# print(type(res3), res3)
# print(type(res4), res4) # 字典是讲所有的 key 键转换到 List 列表
# print(type(res5), res5) # 字典是讲所有的 key 键转换到 List 列表
# print(type(res6), res6) # 字典是讲所有的 value 键转换到 List 列表
# print(type(res7), res7) # 字典是讲所有的 键值对 转换到 List 列表
# 打印效果
# <class 'list'> [('张三', 75), ('李四', 60), ('王五', 85)]

# 2.tuple 函数:1.定义空元组。2.将【可迭代对象】转换为元组
# 定义空元组
# t1 = tuple()
# print(type(t1), t1)
# 将【可迭代对象】转换为元组
# res1 = tuple(range(8))
# res2 = tuple('欢迎来到尚硅谷')
# res3 = tuple({10, 20, 30, 40, 50})
# res4 = tuple({'张三': 75, '李四': 60, '王五': 85})
# res5 = tuple({'张三': 75, '李四': 60, '王五': 85}.keys())
# res6 = tuple({'张三': 75, '李四': 60, '王五': 85}.values()) # 使用字典的 values() 方法
# res7 = tuple({'张三': 75, '李四': 60, '王五': 85}.items()) # 使用字典的 items() 方法
# print(type(res1), res1)
# print(type(res2), res2)
# print(type(res3), res3)
# print(type(res4), res4) # 字典是讲所有的 key 键转换到 Tuple 元组
# print(type(res5), res5) # 字典是讲所有的 key 键转换到 Tuple 元组
# print(type(res6), res6) # 字典是讲所有的 value 键转换到 Tuple 元组
# print(type(res7), res7) # 字典是讲所有的 键值对 转换到 Tuple 元组
# 打印效果
# <class 'tuple'> (('张三', 75), ('李四', 60), ('王五', 85))

# 3.set 函数:1.定义空集合。2.将【可迭代对象】转换为集合
# 定义空集合
# s1 = set()
# print(type(s1), s1)

# 将【可迭代对象】转换为集合，集合是【无序】的，所以输出结果可能与代码中不同
# res1 = set(range(8))
# res2 = set('欢迎来到尚硅谷')
# res3 = set({10, 20, 30, 40, 50})
# res4 = set({'张三': 75, '李四': 60, '王五': 85})
# res5 = set({'张三': 75, '李四': 60, '王五': 85}.keys())
# res6 = set({'张三': 75, '李四': 60, '王五': 85}.values()) # 使用字典的 values() 方法
# res7 = set({'张三': 75, '李四': 60, '王五': 85}.items()) # 使用字典的 items() 方法
# print(type(res1), res1)
# print(type(res2), res2)
# print(type(res3), res3)
# print(type(res4), res4) # 字典是讲所有的 key 键转换到 Set 集合
# print(type(res5), res5) # 字典是讲所有的 key 键转换到 Set 集合
# print(type(res6), res6) # 字典是讲所有的 value 键转换到 Set 集合
# print(type(res7), res7) # 字典是讲所有的 键值对 转换到 Set 集合

# 4.str 函数:1.定义空字符串。2.将【任意类型】转换为字符串
# 定义空字符串
# s1 = str()
# print(type(s1), s1)

# 将【任意类型】转换为字符串
# res1 = str(range(8))
# res2 = str('欢迎来到尚硅谷')
# res3 = str({10, 20, 30, 40, 50})
# res4 = str({'张三': 75, '李四': 60, '王五': 85})
# res5 = str({'张三': 75, '李四': 60, '王五': 85}.keys())
# res6 = str({'张三': 75, '李四': 60, '王五': 85}.values())  # 使用字典的 values() 方法
# res7 = str({'张三': 75, '李四': 60, '王五': 85}.items())  # 使用字典的 items() 方法
# res8 = str(False)
# res9 = str(None)
# res10 = str(100)
# print(type(res1), res1)
# print(type(res2), res2)
# print(type(res3), res3)
# print(type(res4), res4)  # 字典是讲所有的 键值对 转换到 Str 字符串
# print(type(res5), res5)  # 字典是讲所有的 key 键转换到 Str 字符串
# print(type(res6), res6)  # 字典是讲所有的 value 键转换到 Str 字符串
# print(type(res7), res7)  # 字典是讲所有的 键值对 转换到 Str 字符串
# 打印效果
# # <class 'str'> {'张三': 75, '李四': 60, '王五': 85}
# # <class 'str'> dict_keys(['张三', '李四', '王五'])
# # <class 'str'> dict_values([75, 60, 85])
# # <class 'str'> dict_items([('张三', 75), ('李四', 60), ('王五', 85)])
# # for item in res7:
# #     print(item)
# print(type(res8), res8)  # <class 'str'> False
# print(type(res9), res9)  # <class 'str'> None
# print(type(res10), res10)  # <class 'str'> 100

# 5.dict 函数:1.定义空字典。2.将【可迭代对象】转换为字典
# 定义空字典
# d1 = dict()
# print(type(d1), d1)

# 将【可迭代对象】转换为字典
# 备注: 交给dict函数的内容必须是键值对才可以，否则就会报错
# res1 = dict(range(8)) # Cannot convert dictionary update sequence element #0 to a sequence
# res1 = dict({'张三': 75, '李四': 60, '王五': 85})
# res2 = dict([('张三', 75), ('李四', 60), ('王五', 85)])
# res3 = dict((('张三', 75), ('李四', 60), ('王五', 85)))
# res4 = dict({('张三', 75), ('李四', 60), ('王五', 85)})
# print(type(res1), res1)
# print(type(res2), res2)
# print(type(res3), res3)
# print(type(res4), res4)
# 打印效果
# <class 'dict'> {'张三': 75, '李四': 60, '王五': 85}
# <class 'dict'> {'张三': 75, '李四': 60, '王五': 85}
# <class 'dict'> {'张三': 75, '李四': 60, '王五': 85}
# <class 'dict'> {'王五': 85, '张三': 75, '李四': 60}

# 所有的数据容器，都支持成员运算符: in / not in 作用:判断某个“元素”是否在于容器中
hobby = ['打羽毛球', '抽烟', '喝酒', '烫头']
numbers = (10, 20, 30, 40, 50)
message = 'hello,atguigu'
citys = {'北京', '上海', '深圳', '重庆'}
scores = {
    '张三': 75,
    '李四': 60,
    '王五': 85
}

print('抽烟' in hobby)
print(20 in numbers)
print('hel' in message)
print('上海' in citys)
print('李华' in scores)
# 打印效果
# True
# False
# True
# True
# False
print('抽烟' not in hobby)
print(20 not in numbers)
print('hel' not in message)
print('上海' not in citys)
print('李华' not in scores)
# 打印效果
# False
# False
# False
# False
# True