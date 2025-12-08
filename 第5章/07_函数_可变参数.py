# coding=utf-8

# 定义函数（使用 *args 去接收：可变位置参数）
def test1(*args):
    print(args)
    # 此处args的值，是一种新的数据类型，叫：元组，我们下一章就去讲元组
    print(type(args))


# 调用函数
test1('张三', '男', 18, 172)


# 错误的示例：不能将关键字参数交给 args 可变位置参数
# test1('张三', '男', age=18, height=172)
# TypeError: test1() got an unexpected keyword argument 'age'

# 定义函数（使用 *kwargs 去接收：可变关键字参数）
def test2(**kwargs):
    print(kwargs)
    # 此处kwargs的值，是一种新的数据类型，叫：字典，我们下一章就去讲字典
    print(type(kwargs))


# 调用含糊
test2(name='张三', gender='男', age='18', height='172')


# 错误的示例：不能将位置参数交给 kwargs 可变关键字参数
# test2('张三', gender='男', age='18', height='172')
# TypeError: test2() takes 0 positional arguments but 1 was given

# 定义函数（同时使用：可变位置参数、可变关键字参数）
def test3(a, b, *args, c='尚硅谷', **kwargs):
    print('@@@@@@@@@@')
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


# 调用函数
# test3('张三', '男', '抽烟', '喝酒', c='atguigu', age=18, height=172)
test3('张三', '男', '抽烟', '喝酒', age=18, height=172, c='atguigu')
