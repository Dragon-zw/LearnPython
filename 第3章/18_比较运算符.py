# coding=utf-8

# 使用==判断左右两侧是否相等（左右两边的数据类型要一致）
# a = 5
# b = 7
# c = '5'
# result = a == c
# # print(a == b)
# print(result)

# 使用!=判断左右两侧是否不等
# a = 5
# b = 7
# c = '5'
# result = a != c
# print(result)

# 使用>判断左侧是否大于右侧（左右两边的数据类型要一致）
# a = 9
# b = 7
# c = '5'
# result = a > b
# print(result)

# 使用<判断左侧是否小于右侧（左右两边的数据类型要一致）
# a = 3
# b = 7
# c = '5'
# result = a < b
# print(result)

# 使用>=判断左侧是否大于等于右侧（左右两边的数据类型要一致）
# a = 6
# b = 7
# c = '5'
# result = a >= b
# print(result)

# 使用<=判断左侧是否小于等于右 侧（左右两边的数据类型要一致）
# a = 9
# b = 7
# c = '5'
# result = a <= b
# print(result)

# 以上这些比较运算符，同样适用于字符串
# msg1 = 'abc'
# msg2 = 'abc666'
# print(msg1 == msg2)

# msg1 = 'abc'
# msg2 = 'abc666'
# print(msg1 != msg2)

msg1 = 'abc'
msg2 = 'xyz'
msg3 = '我爱你'  # 我 Unicode = 25105
msg4 = '中国'   # 中 Unicode = 20013

# Python 解释器在比较 Unicode 编码的大小发现 msg5 和 msg6 前三位一样，并且 msg5 已经没有多余的字符进行比较了之后
# Python 解释器会比较 msg5 和 msg6 的长度
msg5 = 'abc'  # 长度 3
msg6 = 'abcdef'  # 长度 6
print(msg1 > msg2)  # False
print(msg3 > msg4)  # True
print(msg5 > msg6)  # False

# 查看 Unicode 编码（ 使用ord()查看指定字符的Unicode编码 ）
print(ord('a'))
print(ord('中'))

# 将 Unicode 解码（ 使用chr()将Unicode编码转为字符 ）
print(chr(97))
print(chr(25105))
