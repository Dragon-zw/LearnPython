# coding=utf-8

# 使用 str() 将指定的数据类型转换成字符串
# result1 = str(18)
# result2 = str(75.6)
# result3 = str(1.8e3) # 1.8 乘以 10 的三次方
# result4 = str(12_000)
#
# print(type(result1), result1)
# print(type(result2), result2)
# print(type(result3), result3)
# print(type(result4), result4)

# 把指定数据转为整型: int()
# result1 = int(15.6)
# result2 = int('79')
# result3 = int('  79  ')
# result4 = int(48)
# 以下是错误的实例
# result5 = int('  7 9  ')
# result6 = int('你好')
# result7 = int('79个')
# result8 = int('15.6')

# print(type(result1), result1)
# print(type(result2), result2)
# print(type(result3), result3)
# print(type(result4), result4)

# 把指定数据转为浮点型:float()
result1 = float(18)
result2 = float('15.6')
result3 = float('  5.7  ')
result4 = float(14.8)
result5 = float('48')
# 以下是错误的实例
# float('  5. 7  ')
# float('你好')
# float('5.7元')
# float('5.23.12')

print(type(result1), result1)
print(type(result2), result2)
print(type(result3), result3)
print(type(result4), result4)
print(type(result5), result5)
