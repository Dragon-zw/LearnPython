# coding=utf-8

# and 运算符：用于判断其两侧的值，是否都为True
# print(True and True)  # True
# print(True and False)  # False
# print(False and True)  # False
# print(False and False)  # False

# print(8 > 7 and 8 > 7)  # True
# print(8 > 7 and 2 > 3)  # False
# print(2 > 3 and 8 > 7)  # False
# print(2 > 3 and 2 > 3)  # False

# and 具备“逻辑短路”能力
# print(3 / 0)  # ZeroDivisionError: divi sion by zero
# print(False and 3 / 0)  # False
# # print(True and 3 / 0)  # ZeroDivisionError: divi sion by zero
# print(3 > 9 and 3 / 0)  # False

# and返回的不一定是布尔值，它返回的是某个参与计算的值本身
# 规则：and会先看左边，如果左边是“假”（Python 底层逻辑会将程序执行的结果转换为布尔值，并不会改变程序的计算结果 ），就直接返回左边，否则返回右边
# 备注：若参与and运算的值不是布尔值，那 Python 会自动转为布尔值，然后再进行逻辑操作。
# print(2 - 2 and True)  # 0
# print('' and True)  # ''
# print(True and 8 / 2)  # 4.0
# print(3 + 3 and 3 * 4)  # 12

# or 运算符：用于判断其两侧，是否至少有一个为True（只要有一个是True，那就返回True）
# print(True or True)  # True
# print(True or False)  # True
# print(False or True)  # True
# print(False or False)  # False
#
# print(9 > 2 or 9 > 2)  # True
# print(9 > 2 or 3 < 1)  # True
# print(3 < 1 or 9 > 2)  # True
# print(3 < 1 or 3 < 1)  # False

# or同样具备“逻辑短路”的能力
# print(True or 3 / 0)  # True
# # print(False or 3 / 0)  # ZeroDivisionError: division by zero
# print(9 > 3 or 3 / 0)  # True

# or返回的也不一定是布尔值，它返回的是参与计算的值本身，
# 规则：or会先看左边，如果左边为“真”，就直接返回左边，否则返回右边；
# 备注：若参与or运算的值不是布尔值，那 Python 会自动转为布尔值，然后再进行逻辑操作。
# print(7 - 2 or False)  # 5
# print('你好' or '尚硅谷')  # 你好
# print(False or 8 / 2)  # 4.0
# print(2 - 2 or 3 * 4)  # 12

# not 运算符：
# not 用于取反，不过要注意：如果参与not运算的值不是布尔值，那 Python 会自动将其转为布尔值，然后再进行逻辑操作。
print(not True)  # False
print(not False)  # True
print(not 3 > 2)  # False
print(not 3 < 2)  # True

# not返回的值，一定是布尔值!
print(not 0)  # True
print(not 3 > 2)  # False
print(not 9 // 4)  # False
print(not 'abc')  # False
