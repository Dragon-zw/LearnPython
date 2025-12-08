# coding=utf-8
name = '张三'
gender = '男'
weight = 65.2
age = 12

msg1 = '北京'
msg2 = '欢迎你'
msg3 = msg1 + msg2
print(msg3)

# 表示一个人的完整信息
# 写法一：直接使用 + 加号进行拼接，写起来很麻烦（而且代码可读性很差），而且只能是字符串之间拼接。
info1 = '我叫 ' + name + '，我是 ' + gender + ' 生'
print(info1)

# 写法二：使用占位符
info2 = '我叫%s，我是%s生，我体重是%f，年龄是%i' % (name, gender, weight, age)
print(info2)

# Python 解释器为了尽量不让代码报错，所以就会将浮点数和整数进行转换为字符串进行输出
info2 = '我叫%s，我是%s生，我体重是%s，年龄是%s' % (name, gender, weight, age)
print(info2)

# 原则一句话：
# 占位符要的数据如果和我们给的数据是一样的类型，那 Python 解释器就直接使用
# 占位符要的数据如果和我们给的数据是不一样的类型，那 Python 解释器就会尝试对我们给的数据进行类型转换
info2 = '我叫%s，我是%s生，我体重是%i，年龄是%i  ' % (name, gender, weight, age)
print(info2) # 这种转换并不会四舍五入，Python 解释器会直接丢弃小数位

# 写法三：使用 f-string （Python 的推荐写法）
info3 = f'我是{name}，我是{gender}生，我体重是{weight}，年龄是{age}'
# info3 这个变量中包含一些要嵌入的内容，需要使用标记语法！
print(info3)
