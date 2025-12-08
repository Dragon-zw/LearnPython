# coding=utf-8

# 定义有内容的【可变集合】
# s1 = {10, 20, 20, 30, 40, 40, 50, 60, 60, 70, 80, 90, 100}
# s2 = {'你好', 'hello', '你好', 'atguigu', '北京'}
# s3 = {10, '你好', True, 1, 12.4}
# print(type(s1), s1)
# print(type(s2), s2)
# print(type(s3), s3)

# 向集合中添加一个元素
# s2.add('尚硅谷')
# print(s2)

# 定义有内容的【不可变集合】
# s1 = frozenset({10, 20, 20, 30, 40, 40, 50, 60, 60, 70, 80, 90, 100})
# s2 = frozenset({'你好', 'hello', '你好', 'atguigu', '北京'})
# s3 = frozenset({10, '你好', True, 1, 12.4})
# print(type(s1), s1)
# print(type(s2), s2)
# print(type(s3), s3)

# 向不可变集合中添加一个元素
# s2.add('尚硅谷')  # AttributeError: 'frozenset' object has no attribute 'add'

# frozenset() 函数接收的参数，可以是任意可迭代对象，但最终返回的一定是【不可变集合】
# s1 = frozenset([10, 20, 30, 40, 50])
# s2 = frozenset((10, 20, 30, 40, 50))
# s3 = frozenset('hello')
#
# print(type(s1), s1)
# print(type(s2), s2)
# print(type(s3), s3)

# 定义空集合【可变集合】
# s1 = set()
# print(type(s1), s1)
# s1.add(1)
# print(type(s1), s1)

# 不能直接写{}来定义空集合，因为直接写{}定义的是：空字典
# s2 = {}
# print(type(s2), s2)

# 定义空集合【不可变集合】
# s3 = frozenset()
# print(type(s3), s3)

# 集合中不能嵌套【可变集合】，但可以嵌套【不可变集合】
# 通俗理解：只有“不可变”的东西，才能安全的放进集合里
s1 = {10, 20, 30, 40, 50} # 可变集合
s2 = frozenset({100, 200, 300, 400, 500}) # 不可变集合
l1 = [666, 777, 888] # 列表
t1 = ('hello', 'atguigu', '北京') # 元组

# 定义集合
# s3 = {11, 22, 33, s1} # 报错
# print(s3)  # TypeError: cannot use 'set' as a set element (unhashable type: 'set')
s3 = {11, 22, 33, s2}
print(s3)  # {frozenset({400, 100, 500, 200, 300}), 33, 11, 22}
# s3 = {11, 22, 33, l1} # 报错
# print(s3)  # TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s3 = {11, 22, 33, t1}
print(s3)  # {33, 11, ('hello', 'atguigu', '北京'), 22}
