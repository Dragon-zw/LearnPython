# coding=utf-8

# 定义函数（接收位置参数）
def greet(name, gender, age, height):
    print(f'我叫{name}, 性别{gender}, 年龄是{age}, 身高当前是{height}cm')
    print(f'我的身高{height}cm, 今年是{age}, 我叫{name}')

# 调用函数
greet('张三','男','18','172')

# 错误的示例
# greet('张三','18','172')
# TypeError: greet() missing 1 required positional argument: 'height'
# greet('男', '张三', '172', '18')
# 我叫男, 性别张三, 年龄是172, 身高当前是18cm
