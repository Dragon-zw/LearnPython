"""这是一个标识符命名规则的 Python 文件"""

# 只能包含：数字、字母、下划线，且不能以数字开头，不能包含空格。
name2 = '张三'
age_2 = 18
_weight_ = 60.2
# Error:
# 3_height_ = 60.2
# _ height_ = 60.2

# 区分大小写，即Name和name是两个不同的标识符。
name = "熊大"
Name = '熊二'
# print(name, Name)

# 不能使用关键字。
# Error:
# if = 89
# as = 100
# pass = 102

# 标识符尽量不要与内置函数同名。
print = "你好啊"
print(100)

# 标识符虽然没有长度限制，但应追求：简洁清晰，具有描述性。
# 1. 大驼峰（UpperCamelCase）: 每个单词的首字母大写，例如：UserName
# 2. 小驼峰（lowerCamelCase）: 首词的首字母小写，后面单词首字母大写，例如：userName
# 3. 蛇形（snake_case）：单词间用下划线连接，例如：user_name
userName = '小强'
UserName = '小强'
user_name = '小强'
