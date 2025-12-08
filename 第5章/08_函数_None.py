# coding=utf-8

# 0. None 是一个特殊的字面量，用来表示：空值、无值、无意义。None 可以认为是万能类型！
msg = None

# 1. None的类型是NoneType。
print(msg)
print(type(msg))

# 2. None出现在布尔判断中(if判断条件、while循环条件)，会被当作False来处理。
# bool(msg)
print(bool(msg))
if msg:
    print('你好~~~')
if not msg:
    print('你好！！！')

# 3. None不能参与任何数学运算，也不能与字符串拼接。
# result1 = msg + 1 # 应为类型 'int'，但实际为 'None'
# print(result1)
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
# result2 = msg + 'hello' # 类 'None' 未定义 '__add__'，所以不能对其实例使用 '+' 运算符
# print(result2)
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
