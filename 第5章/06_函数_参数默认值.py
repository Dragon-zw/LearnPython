# coding=utf-8

# 定义函数（设置参数默认值，可选参数）
def greet(name, gender, age, height, msg='你好'):
    print(f'姓名{name}，性别{gender}，年龄是{age}，身高是{height}cm')
    print(f'我想说的是：{msg}')


# 正确的示例：
# greet('张三', '性别', age='18', height='172')
greet('张三', '性别', '18', '172', 'hello')
greet('张三', '性别', '18', '172', msg='hello')


# 错误的示例：
# def greet(name, gender, age, msg='你好', height):
#     print(f'姓名{name}，性别{gender}，年龄是{age}，身高是{height}cm')
#     print(f'我想说的是：{msg}')

# 参数默认值的应用场景
# print() 函数底层给 end 参数设置了默认值(\n)
print('尚硅谷')
print('尚硅谷',end='!!!')