# coding=utf-8

# /前面只能用『位置参数』，*后面只能用『关键字参数』
# 定义函数（使用 / 和 * 限制传参方式）
def greet(name, /, gender, *, age, height):
    print(f'姓名{name}，性别是{gender}，年龄是{age}，身高是{height}')


# 调用函数
# 正确的示例
greet('张三', '男', age='18', height='172')
greet('张三', gender='男', age='18', height='172')

# 错误的示例
# greet(name='张三', gender='男', age='18', height='172')
# TypeError: greet() got some positional-only arguments passed as keyword arguments: 'name'
# greet('张三', '男', '18', height='172')
# TypeError: greet() takes 2 positional arguments but 3 positional arguments (and 1 keyword-only argument) were given

# def greet(name, *, gender, /, age, height):
#     print(f'姓名{name}，性别是{gender}，年龄是{age}，身高是{height}')
#     def greet(name, *, gender, /, age, height):
#                                ^
# SyntaxError: / must be ahead of *