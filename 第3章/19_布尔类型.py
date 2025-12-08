# coding=utf-8

# 自己定义的布尔值
a = True
b = False

# 靠程序执行得到的布尔值
c = 5 > 3
d = 7 < 2

# print(type(a), a)
# print(type(b), b)
# print(type(c), c)
# print(type(d), d)

# 布尔类型是int类型的子类型，底层的本质是用1表示True，用0表示False
a1 = int(True)
b1 = int(False)
# print(type(a1), a1)
# print(type(b1), b1)
print(type(int(True)), int(True))
print(type(int(False)), int(False))

# print(4 + True)   # 5
# print(8 - False)  # 8

# print(True + True)  # 2
# print(True + False)  # 1

# print(7 > True)  # True
# print(False <= 0)  # True

# 使用bool()将指定内容转为布尔类型
print(bool(1))  # True
print(bool(0))  # False

# Python中除0以外的任何数，转为布尔值后都为True（Python 完全不关心正负）
# print(bool(300))  	# True
# print(bool(25.6))  	# True
# print(bool(1.8e3))  # True
# print(bool(12_000)) # True
# print(bool(-10))  	# True
# print(bool(0))  # False

# Python 中除空字符串以外的任何字符串，转为布尔值都是 True
print(bool('Hello'))  # True
print(bool('0'))  # True
print(bool('  '))  # True
print(bool('18.5'))  # True
print(bool('-9'))  # True
print(bool(''))  # False
