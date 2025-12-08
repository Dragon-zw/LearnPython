# coding=utf-8

# 全局作用域 与 局部作用域 和 global 的使用
# a = 100
# b = 200
#
#
# def test():
#     c = '尚硅谷'
#     d = '你好啊'
#     global a
#     a = 300
#     print(f'函数中的打印(a): {a}')
#     print(f'函数中的打印(b): {b}')
#     print(f'函数中的打印(c): {c}')
#     print(f'函数中的打印(d): {d}')
#
#
# test()
# print('************')
# print(f'全局中的打印(a): {a}')
# print(f'全局中的打印(b): {b}')
# print(f'全局中的打印(c): {c}') # 未解析的引用 'c'

# 局部作用域 和 局部变量，会在函数调用时创建，在函数执行结束后自动销毁！
def test2():
    m = 100
    m += 1
    print('我是 test2() 函数中定义的 m: ', m)

# 调用函数
test2()
test2()

print('********************')
# 全局作用域 与 全局变量，会在程序开始时创建，在程序结束后销毁！
n = 100

def test3():
    global n
    n += 1
    print('我是 test3() 函数中定义的 n: ', n)

# 调用函数
test3()
test3()
print(n)
