# coding=utf-8

# 1.提示用户输入密码，若密码不正确就反复提示，直到密码正确。
# 定义应用程序密码
# password = '123456'
# while True:
#     input_password = input('请输入应用程序密码：')
#     if password == input_password:
#         print('✅你输入的密码正确，可以正常使用应用程序！')
#         break
#     else:
#         print('❎你输入的密码错误，请重新输入密码！')

# 2.遍历字符串'Python'，逐个输出每个字符。
# for i in 'Python':
#     print(f'--> 遍历字符串的每个字符：{i}')

# 3.让用户不断输入数字，直到输入的是一个偶数为止。
# print(8 % 3)
# while True:
#     num = int(input('请输入随机的数字：'))
#     if num % 2 == 0:
#         print(f'✅你输入的数字是{num}，是偶数可以退出程序！')
#         break
#     elif num % 2 != 0:
#         print(f'❎你输入的数字是{num}，需要重新输入数字！')
#     else:
#         print('❎你输入的数字有误，请重新输入！')

# 4.让用户依次输入5个名字，最终把5个名字拼接到一起。
name = ''
all_name = ''
for n in range(1, 6):
    name = input(f'请依次输入5个名字，请输入第{n}个名字：')
    all_name += name
print(all_name)
