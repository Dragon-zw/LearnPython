# coding=utf-8
# 所谓整型就是没有小数点的数字， Python 中的整型，可以是任意大小的整数，包括负整数，也可以是 0.
import sys

age = 18
temp = -15
score = 0

print(type(age))
print(type(temp))
print(type(score))

# 当数很大时，我们可以使用下划线将数字进行分组，来让数字变得更易读。
# 每 3 位一组进行分组，每组使用 _ 下划线分割
salary = 300_000
house_price = 3_200_000
gradutate = 12_000_000
print(salary, house_price, gradutate)

# Python中整数的上限值（Python 的整数的上限并不是固定值），取决于执行代码的计算机的内存和处理能力。
a = 99999999999999999999999999999999999999999999999999999999999999999999999999999999
print(a)
a = 3 ** 2
print(a)

print('******************************************************')
a = 9 ** 9999
sys.set_int_max_str_digits(0)
print(a)
# 打印数字时，print() 函数内部会把数字转换成字符串，再打印
# Traceback (most recent call last):
#   File "/Users/georgezhong/Documents/07 PyCharm-Project/Atguigu-Code-2025/第3章/08_整型.py", line 25, in <module>
#     print(a)
#     ~~~~~^^^
# ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
# Python中数字在转换字符串的过程中，默认的限制是:数字不能超过4300位。
b = a + 100
