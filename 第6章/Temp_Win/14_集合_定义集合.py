# coding=utf-8

# 定义有内容【可变集合】
# s1 = {10, 20, 20, 30, 40, 40, 50, 60, 60, 70, 80, 90, 100}
# s2 = {'你好', 'hello', '你好', 'atguigu', '北京'}
# s3 = {10, '你好', True, 1, 12.4}
#
# print(type(s1), s1)
# print(type(s2), s2)
# print(type(s3), s3)

"""
当我们打印集合的时候，打印出来的元素顺序，它每次都有可能会不一样！
偶尔会出现打印的顺序似乎比较稳定，比较简单的解释：如果集合中的元素都是数字的话，那么由于 Python 底层的存储机制的原因会导致每次打印的数字顺序都会稳定在一个固定的顺序上！但是我们千万不要依赖这个顺序！
"""
# 可变集合中添加元素
# s2.add("尚硅谷")
# print(s2)

# 定义有内容的【不可变集合】
# fs1 = frozenset({10, 20, 20, 30, 40, 40, 50, 60, 60, 70, 80, 90, 100})
# fs2 = frozenset(['你好', 'hello', '你好', 'atguigu', '北京'])
# fs3 = frozenset({10, '你好', True, 1, 12.4})
#
# print(type(fs1), fs1)
# print(type(fs2), fs2)
# print(type(fs3), fs3)

# 不可变集合中添加元素
# fs1.add("尚硅谷") # 类 'frozenset' 的未解析的特性引用 'add'

# frozenset 接收的参数，可以是任意可迭代对象，但最终返回的一定是【不可变集合】
# s1 = frozenset([10, 20, 30, 40, 50])
# s2 = frozenset((10, 20, 30, 40, 50))
# s3 = frozenset('hello')
# print(type(s1), s1)
# print(type(s2), s2)
# print(type(s3), s3)

# 定义空集合【可变集合】
# s1 = set()
# print(type(s1), s1)

# 不能直接写{}来定义空集合，因为直接写{}定义的是：空字典
# s2 = {}
# print(type(s2), s2)

# 定义空集合（不可变集合）使用场景很少！
# s3 = frozenset()
# print(type(s3), s3)

# 集合中不能嵌套【可变集合】，但可以嵌套【不可变集合】
# 通俗理解：只有“不可变”的东西，才能安全的放进集合里
s1 = {10, 20, 30, 40, 50}
s2 = frozenset([100, 200, 300, 400, 500])
l1 = [666, 777, 888]
t1 = ('hello', 'atguigu', '北京')
str1 = 'hello,world'

# s3 = {10, 20, 30, 40, s1} # TypeError: cannot use 'set' as a set element (unhashable type: 'set')
# print(s3)

# s3 = {10, 20, 30, 40, s2}
# print(s3) # {40, 10, frozenset({100, 200, 300, 400, 500}), 20, 30}

# s3 = {10, 20, 30, 40, l1} # TypeError: cannot use 'list' as a set element (unhashable type: 'list')
# print(s3)

s3 = {10, 20, 30, 40, t1}
print(s3) # {40, 10, ('hello', 'atguigu', '北京'), 20, 30}

s3 = {10, 20, 30, 40, str1}
print(s3) # {'hello,world', 40, 10, 20, 30}

