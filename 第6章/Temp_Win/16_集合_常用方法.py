# coding=utf-8

# 集合A.difference(集合B)：
# 作用：找出集合A中，不同于集合B的元素（集合A 与 集合B 都不变，返回的是一个新的集合）
# s1 = {10, 20, 30, 40, 50}
# s2 = {30, 40, 50, 60, 70}
# s1 中不同于 s2 中的元素
# result = s1.difference(s2)
# print(s1)
# print(s2)
# print(result)  # {10, 20}

# 集合A.difference_update(集合B)：
# 作用：从集合A中，删除集合B中存在的元素（集合A会被修改，集合B不会）
# s1 = {10, 20, 30, 40, 50}
# s2 = {30, 40, 50, 60, 70}
# s1 中不同于 s2 中的元素，删除 s1 中 s2 中存在的元素
# s1.difference_update(s2)
# print(s1)
# print(s2)

# 集合A.union(集合B)：
# 作用：合并两个集合，集合A 和 集合B 都不变，返回的是一个新的集合
# s1 = {10, 20, 30, 40, 50}
# s2 = {30, 40, 50, 60, 70}
# result = s1.union(s2)
# print(s1)
# print(s2)
# print(result)  # {70, 40, 10, 50, 20, 60, 30}

# 集合A.issubset(集合B)：
# 作用：判断集合A是否为集合B的子集
# 如果 集合A的所有元素都在集合B中，那就返回True，否则返回False
# s1 = {10, 20, 30, 40, 50}
# s2 = {30, 40, 50, 60, 70}
# s3 = {30, 40, 50}
# result = s3.issubset(s1)
# print(result)  # True
# result = s1.issubset(s2)
# print(result)  # False

# 集合A.issuperset(集合B)：
# 作用：判断集合A是否是集合B的超集
# 如果集合A中，包含了集合B中的所有元素，那就返回True，否则返回False
# s1 = {10, 20, 30, 40, 50}
# s2 = {30, 40, 50, 60, 70}
# s3 = {30, 40, 50}
# result = s1.issuperset(s3)
# print(result)  # True
# result = s1.issuperset(s2)
# print(result)  # False

# 集合A.isdisjoint(集合B)：
# 作用：判断集合A和集合B是否没有交集
# 如果没有交集，返回True；只要有一个公共元素，就返回False
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}
s3 = {80, 90}
result = s1.isdisjoint(s3)
print(result)  # True
result = s1.isdisjoint(s2)
print(result)  # False
