# coding=utf-8

# 以下这五个函数:既能定义对应的【空容器】，又能将【其他类型】转换为对应的数据类型

# 1.list 函数：1.定义空列表。2.将【可迭代对象】转换为列表
# ## 1.定义空列表。
# l1 = list()
# print(type(l1), l1)  # <class 'list'> []
#
# ## 2.将【可迭代对象】转换为列表
# res1 = list(range(8))
# res2 = list('欢迎来到尚硅谷')
# res3 = list({10, 20, 30, 40, 50})
# # 获取字典中所有的 keys
# res4 = list({'张三': 75, '李四': 60, '王五': 85})
# res5 = list({'张三': 75, '李四': 60, '王五': 85}.keys())
# # 获取字典中所有的 values
# res6 = list({'张三': 75, '李四': 60, '王五': 85}.values())
# # 获取字典中所有的键值对
# res7 = list({'张三': 75, '李四': 60, '王五': 85}.items())
# print(type(res1), res1)  # <class 'list'> [0, 1, 2, 3, 4, 5, 6, 7]
# print(type(res2), res2)  # <class 'list'> ['欢', '迎', '来', '到', '尚', '硅', '谷']
# print(type(res3), res3)  # <class 'list'> [10, 20, 30, 40, 50]
# print(type(res4), res4)  # <class 'list'> ['张三', '李四', '王五']
# print(type(res5), res5)  # <class 'list'> ['张三', '李四', '王五']
# print(type(res6), res6)  # <class 'list'> [75, 60, 85]
# print(type(res7), res7)  # <class 'list'> [('张三', 75), ('李四', 60), ('王五', 85)]

# 2.tuple 函数：1.定义空元组。2.将【可迭代对象】转换为元组
# ## 1.定义空元组。
# t1 = tuple()
# print(type(t1), t1)  # <class 'tuple'> ()
#
# ## 2.将【可迭代对象】转换为元组
# res1 = tuple(range(8))
# res2 = tuple('欢迎来到尚硅谷')
# res3 = tuple({10, 20, 30, 40, 50})
# # 获取字典中所有的 keys
# res4 = tuple({'张三': 75, '李四': 60, '王五': 85})
# res5 = tuple({'张三': 75, '李四': 60, '王五': 85}.keys())
# # 获取字典中所有的 values
# res6 = tuple({'张三': 75, '李四': 60, '王五': 85}.values())
# # 获取字典中所有的键值对
# res7 = tuple({'张三': 75, '李四': 60, '王五': 85}.items())
# print(type(res1), res1)  # <class 'tuple'> (0, 1, 2, 3, 4, 5, 6, 7)
# print(type(res2), res2)  # <class 'tuple'> ('欢', '迎', '来', '到', '尚', '硅', '谷')
# print(type(res3), res3)  # <class 'tuple'> (50, 20, 40, 10, 30)
# print(type(res4), res4)  # <class 'tuple'> ('张三', '李四', '王五')
# print(type(res5), res5)  # <class 'tuple'> ('张三', '李四', '王五')
# print(type(res6), res6)  # <class 'tuple'> (75, 60, 85)
# print(type(res7), res7)  # <class 'tuple'> (('张三', 75), ('李四', 60), ('王五', 85))

# 3.set 函数：1.定义空集合。2.将【可迭代对象】转换为集合
# ## 1.定义空集合。
# s1 = set()
# print(type(s1), s1)  # <class 'set'> set()
#
# ## 2.将【可迭代对象】转换为集合
# res1 = set(range(8))
# res2 = set('欢迎来到尚硅谷')
# res3 = set({10, 20, 30, 40, 50})
# # 获取字典中所有的 keys
# res4 = set({'张三': 75, '李四': 60, '王五': 85})
# res5 = set({'张三': 75, '李四': 60, '王五': 85}.keys())
# # 获取字典中所有的 values
# res6 = set({'张三': 75, '李四': 60, '王五': 85}.values())
# # 获取字典中所有的键值对
# res7 = set({'张三': 75, '李四': 60, '王五': 85}.items())
# print(type(res1), res1)  # <class 'set'> {0, 1, 2, 3, 4, 5, 6, 7}
# print(type(res2), res2)  # <class 'set'> {'谷', '硅', '来', '尚', '迎', '到', '欢'}
# print(type(res3), res3)  # <class 'set'> {50, 20, 40, 10, 30}
# print(type(res4), res4)  # <class 'set'> {'李四', '张三', '王五'}
# print(type(res5), res5)  # <class 'set'> {'李四', '张三', '王五'}
# print(type(res6), res6)  # <class 'set'> {75, 60, 85}
# print(type(res7), res7)  # <class 'set'> {('李四', 60), ('王五', 85), ('张三', 75)}
# # for item in res7:
# #     print(item)

# 4.str 函数：1.定义空字符串。2.将【任意类型】转换为字符串
# ## 1.定义空字符串。
# s1 = str()
# print(type(s1), s1)  # <class 'str'>
#
# ## 2.将【任意类型】转换为字符串
# res1 = str(range(8))
# res2 = str('欢迎来到尚硅谷')
# res3 = str({10, 20, 30, 40, 50})
# # 获取字典中所有的 keys
# res4 = str({'张三': 75, '李四': 60, '王五': 85})
# res5 = str({'张三': 75, '李四': 60, '王五': 85}.keys())
# # 获取字典中所有的 values
# res6 = str({'张三': 75, '李四': 60, '王五': 85}.values())
# # 获取字典中所有的键值对
# res7 = str({'张三': 75, '李四': 60, '王五': 85}.items())
# res8 = str(False)
# res9 = str(None)
# res10 = str(100)
# print(type(res1), res1)  # <class 'str'> range(0, 8)
# print(type(res2), res2)  # <class 'str'> 欢迎来到尚硅谷
# print(type(res3), res3)  # <class 'str'> {50, 20, 40, 10, 30}
# print(type(res4), res4)  # <class 'str'> {'张三': 75, '李四': 60, '王五': 85}
# print(type(res5), res5)  # <class 'str'> dict_keys(['张三', '李四', '王五'])
# print(type(res6), res6)  # <class 'str'> dict_values([75, 60, 85])
# print(type(res7), res7)  # <class 'str'> dict_items([('张三', 75), ('李四', 60), ('王五', 85)])
# print(type(res8), res8)  # <class 'str'> False
# print(type(res9), res9)  # <class 'str'> None
# print(type(res10), res10)  # <class 'str'> 100

# 5.dict 函数：1.定义空字典。2.将【可迭代对象】转换为字典
# ## 1.定义空字典
# d1 = dict()
# print(type(d1), d1)  # <class 'dict'> {}
#
# ## 2.将【可迭代对象】转换为字典
# # 备注：交给dict函数的内容必须是键值对才可以，否则就会报错
# # res1 = dict(range(0, 8))
# # TypeError: object is not iterable
# # Cannot convert dictionary update sequence element #0 to a sequence
# res2 = dict({'张三': 75, '李四': 60, '王五': 85})
# print(type(res2), res2)  # <class 'dict'> {'张三': 75, '李四': 60, '王五': 85}
# res3 = dict([('张三', 75), ('李四', 60), ('王五', 85)])
# res4 = dict((('张三', 75), ('李四', 60), ('王五', 85)))
# res5 = dict({('张三', 75), ('李四', 60), ('王五', 85)})
# print(type(res3), res3)  # <class 'dict'> {'张三': 75, '李四': 60, '王五': 85}
# print(type(res4), res4)  # <class 'dict'> {'张三': 75, '李四': 60, '王五': 85}
# print(type(res5), res5)  # <class 'dict'> {'张三': 75, '李四': 60, '王五': 85}

# 所有的数据容器，都支持成员运算符：in / not in 作用：判断某个“元素”是否在于容器中。
hobby = ['抽烟', '喝酒', '烫头']
nums = (10, 20, 30, 40, 50)
msg = 'hello,atguigu'
citys = {'北京', '天津', '上海', '重庆'}
score = {'张三': 75, '李四': 60, '王五': 85}

result = '喝酒' in hobby
print(result)  # True
print(20 in nums)  # True
print('hel' in msg)  # True
print('北京' in citys)  # True
print('李华' in score)  # False

print('喝酒' not in hobby)  # False
print(20 not in nums)  # False
print('hel' not in msg)  # False
print('北京' not in citys)  # False
print('李华' not in score)  # True
