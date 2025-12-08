# coding=utf-8

# 使用input()获取用户的输入
name = input('请输入你的姓名：')
# print('请输入你的年龄：')
# age = input()
# 约等于
age = input('请输入你的年龄：')

# Python把决定数据类型的权利，交给了程序员自己
# input() 获取的内容是字符串类型
# input() 获取到的内容全都是字符串类型
print(type(age))

age = int(age)  # 将 age 进行类型转换整型
# 打印内容
print(f'姓名：{name}，你的年龄是：{age}')
# print(f'你的年龄是：{int(age) + 1}')  # 可以在 {} 中进行
print(f'姓名：{name}，你的年龄是：{age + 1}')
