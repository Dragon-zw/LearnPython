# coding=utf-8

# 定义函数
def add(n1, n2):
    print(f"我收到了：{n1}，{n2}，他们的相加之和是{n1 + n2}")
    print('add 函数已经执行完毕了！')
#     # answer = n1 + n2
#     # return answer
    return n1 + n2
#    # return # None

# 调用函数
add(1, 2)
result = add(100, 200) # 没有 resturn 函数 'add' 不返回任何内容
print(result) # None

# print() 函数是没有返回值的
res = print('hello')
print(res) # 返回值是 None
