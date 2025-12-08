# coding=utf-8

# 定义一个列表
nums = [10, 20, 30, 40, 50]

# 测试正索引
# print(nums[0])
# print(nums[1])
# print(nums[2])
# print(nums[3])
# print(nums[4])

# 测试负索引
print(nums[-1])
print(nums[-2])
print(nums[-3])
print(nums[-4])
print(nums[-5])

# 测试错误的索引
# print(nums[5])
# print(nums[-6])
# 专业说法：下标越界！开发者在使用的是要注意不要让索引值超出范围！
# IndexError: list index out of range

# 定义嵌套列表
nums2 = [10, 20, ['你好啊', '尚硅谷'], 40, 50]
# 取出"尚硅谷"的字符串
print(nums2[2][1])
# 下标的概念不单单是列表中存在，后面的元祖，字符串也存在！
