# coding=utf-8

# 序列相加
# 列表相加
list1 = [10, 20, 30, 40, 50]
list2 = [60, 70, 80, 90, 100]
list3 = list1 + list2
print(list3)

# 元组相加
tuple1 = (10, 20, 30, 40, 50)
tuple2 = (60, 70, 80, 90, 100)
tuple3 = tuple1 + tuple2
print(tuple3)

# 字符串相加
str1 = 'hello'
str2 = 'atguigu'
str3 = str1 + str2
print(str3)

# 错误示例
# list1 = [10, 20, 30, 40, 50]
# str1 = 'hello'
# print(list1 + str1)

# 序列相乘（重复）
list1 = [10, 20, 30, 40]
list2 = list1 * 3
print(list2)  # [10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40]

tuple1 = (10, 20, 30, 40)
tuple2 = tuple1 * 3
print(tuple2)  # (10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40)

str1 = 'hello'
str2 = str1 * 6
print(str2)  # hellohellohellohellohellohello
