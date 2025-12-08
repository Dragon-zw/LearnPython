# coding=utf-8
name = '张三'
gender = '男'
weight = 65.45
age = 12

# %1s 设置字符串展示的最小宽度（精度处理）
# %.1s 设置展示字符串的一位，不会补位，%.0 则不会有任何的展示
# %4.1s Python 解释器会先处理精度的问题
# %.1f 设置浮点数的精度，小数点后 1 位（需要四舍五入）
info = '我叫%-4.1s，我是%3.2s生，我体重是%-9.3f，年龄是%-6.4d' % (name, gender, weight, age)
info = '我叫%-4.1s，性别是%3.2s，体重是%-9.3f，年龄是%-6.4d' % (name, gender, weight, age)
print(info)