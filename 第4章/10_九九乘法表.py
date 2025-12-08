# coding=utf-8

# 前置知识
# print() 在打印完毕之后会自动输出一个换行。
# print('你好', end='!')
# print('', end='') 在 end 中定义什么，print 就以什么作为结尾！
# print('尚硅谷', end='@')

# for 循环实现九九乘法表
# 定义行
# for row in range(1, 10):
#     for col in range(1, row + 1):
#         # result = row * col
#         print(f'{col} * {row} = {row * col}', end='\t')
#     print()

# while 循环实现九九乘法表
row = 1
while row <= 9:
    item = 1
    temp = row + 1
    while item < temp:
        print(f'{item} * {row} = {row * item}', end='\t')
        item += 1
    row += 1
    print()
