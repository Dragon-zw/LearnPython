# coding=utf-8

# 1.使用 index 方法，查找指定元素在列表中第一次出现的下标，返回值是：元素下标。
fruits = ['香蕉', '苹果', '橙子', '香蕉', ['草莓', '香蕉']]
result = fruits.index('苹果')
print(result)
# （1）index 方法中检索其他的字段，如果不在该字段里则会报错！
# （2）index 方法不会进入嵌套列表中去查询元素的！

# 2.使用 count 方法，统计某个元素在列表中出现的次数，返回值是：元素出现的次数。
nums = [10, 20, 10, 30, 10, 40, [10, 30, 10, 40]]
result = nums.count(10)
print(result)
# （1）如果 count 检索是不存在的元素，那么就会返回 0！
# （2）count 方法不会进入嵌套列表中去查询元素的！

# 3.使用 reverse 万法，对列表进行反转（会改变原列表）。
nums = [23, 11, 32, 20, 17, [6, 7, 8, 9]]
print(nums)
nums.reverse()
print(nums)

# 4.使用 sort 方法，对列表排序（默认从小到大），若想从大到小，可以将 reverse 参数设为True。
## 4.1 若列表中的元素：都是数字，则按照数字的大小进行排序（默认是从大到小）
nums = [23, 11, 32, 30, 17]
nums.sort()  # sort 方法是没有返回值的！
print('排序（从小到大）：', nums)
nums.sort(reverse=True)
print('排序（从大到小）：', nums)

## 4.2 若列表中的元素：既有数字，又有字符串，那就会报错！
# nums = [23, 11, 32, 30, 17, '尚硅谷']
# TypeError: '<' not supported between instances of 'str' and 'int'
# nums.sort()
# print(nums)

## 4.3 若列表中的元素：都是字符串，则按照字符串的 Unicode 编码大小进行排序
# 按照字符串的第一个字符的 Unicode 编码大小进行排序
msg_list = ['北京', '尚硅谷', '你好']
msg_list.sort()
print(msg_list)
# print(ord('你'), ord('北'), ord('尚'))
print(ord(msg_list[0][0]), ord(msg_list[1][0]), ord(msg_list[2][0]))
msg_list.sort(reverse=True)
print(msg_list)
