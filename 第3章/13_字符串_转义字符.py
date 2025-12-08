# coding=utf-8
# print('在 Python 中，可以使用单引号包裹一个字符串')

# \' Python 解释器是要输出的单引号，而不是结束的单引号
# print('在 Python 中，可以使用\'\'包裹一个字符串')

# \" Python 解释器是要输出的双引号，而不是结束的双引号
# print("在 Python 中，可以使用\"\"包裹一个字符串")

# 使用 \n 实现换行
# print("注册会员需要以下的信息：\n姓名\n年龄\n手机号")

# 使用 \\ 打印 \
# print("文件路径: C:\\next")

# 使用 \b 删除前一个字符
# print('helloo\b')
# 会有一定的应用程序的场景，例如打字机效果

# 使用 \r 使光标回到本行开头，覆盖输出
# print('67%\r68%')
# 会有一定的应用程序的场景，例如进度加载效果

# 使用 \t 表示水平制表符（让光标跳转到下一个制表位）
# 一个制表位到底是几位，是不确定的，但我们可以通过在字符串后面加.expandtabs()来指定位数。
# print('1234123412341234')
# print('ab\tcd'.expandtabs(4))
# print('abc\td'.expandtabs(4))
# print('abcd\ta'.expandtabs(4))
# print('我是\t中文'.expandtabs(4))

print('1234123412341234')
print('姓名\t性别\t年龄')
print('张三\t男\t18')
print('李四\t女\t25')
print('王五\t男\t32')