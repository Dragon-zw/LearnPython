# coding=utf-8

# 0b 开头表示二进制
num1 = 0b11001
# 0o 开头表示八进制
num2 = 0o1034
# 0x 开头表示十六进制
num3 = 0x1cf

# 备注：Python 中所有的『非十进制』数字，只是代码层面的编写方式，只是给程序员看的
# Python 在进行：计算、打印等操作时，会自动将这些『非十进制』数字，转为『十进制』数字。
# print(num1, num2, num3)  # 25 540 463
# print(num1 + 1)  # 26
# print(str(num2), type(str(num2)))  # '540' (字符串)
# print(num3 > 400)  # True

# # 使用 bin() 将十进制转换为二进制
# result1 = bin(25) # 0b11001
# # 使用 oct() 将十进制转换为八进制
# result2 = oct(540) # 0o1034
# # 使用 hex() 将十进制转换为十六进制
# result3 = hex(463) # 0x1cf
#
# print(result1, result2, result3)
#
# # bin()，oct()，hex() 他们返回的值类型都是字符串
# print(type(result1), type(result2), type(result3)) # <class 'str'> <class 'str'> <class 'str'>

# 使用 int() 将指定其他的进制的数(传入字符串类型)，转换为十进制数字(输出整型)
value1 = int('0b11001', 2)
value2 = int('0o1034', 8)
value3 = int('0x1cf', 16)
print(value1, value2, value3)  # 25 540 463
print(type(value1), type(value2), type(value3))  # <class 'int'> <class 'int'> <class 'int'>
