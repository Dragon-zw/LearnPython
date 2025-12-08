"""这是一个常量的 Python 文件"""
# 常量是软限制，Golang 中的常量就是硬限制

ABC = 16

# Python 中一般约定使用全大写变量名来表示常量，涉及到多个单词时，用下划线做分隔。
ADULT_AGE = 18  # Shift + Command + U
MOUNTS_IN_YEAR = 12
MAX_USERS = 20
PASSWORD_SCORE = 60

print(ADULT_AGE, MOUNTS_IN_YEAR, MAX_USERS, PASSWORD_SCORE)

# 当强制对常量进行修改时，最终也能改掉，但要自觉不改，这是 Python 程序员之间的约定。
MAX_USERS = 1000
print(MAX_USERS)
