# coding=utf-8

# 使用递归求阶乘！！！
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

result = factorial(5)
print(result)