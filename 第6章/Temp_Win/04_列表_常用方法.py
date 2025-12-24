# coding=utf-8

# 1.使用 index 方法，查找指定元素在列表中第一次出现的下标，返回值是：元素下标。
furist = ['香蕉', '苹果', '橙子', '香蕉', ['草莓', '香蕉']]
result = furist.index('香蕉')
print(result)

# result = furist.index('桑葚')
# print(result)
# ValueError: list.index(x): x not in list

# result = furist.index('草莓')
# print(result)
# furist 层面是没有 草莓 的元素的！

# （1）index 方法中检索其他的字段，如果不在该字段里则会报错！
# （2）index 方法不会进入嵌套列表中去查询元素的！

# 2.使用 count 方法，统计某个元素在列表中出现的次数，返回值是:元素出现的次数。
nums = [10, 20, 10, 30, 10, 40, [10, 10, 10]]
result = nums.count(10)
print(result)
# （1）如果 count 检索是不存在的元素，那么就会返回 0！
# （2）count 方法不会进入嵌套列表中去查询元素的！

# 3.使用 reverse 方法，对列表进行反转(会改变原列表)
nums = [23, 11, 32, 20, 17]
nums.reverse()  # reverse 方法是没有返回值的！不会深入到里面嵌套的列表的！
print(nums)

# 4.使用 sort 方法，对列表排序(默认从小到大)，若想从大到小，可以将 reverse 参数设为True。
# 4.1 若列表中的元素：都是数字，则按照数字的大小顺序进行排序。
nums = [23, 11, 32, 30, 17]
nums.sort()
print('排序（从小到大）：', nums)

nums.sort(reverse=True)
print('排序（从大到小）：', nums)

# 4.2 若列表中的元素：既有数字，又有字符串，那就会报错。
# nums = [23, 11, 32, 30, 17, '尚硅谷']
# nums.sort()
# print(nums)
# TypeError: '<' not supported between instances of 'str' and 'int'

# 4.3 若列表中的元素：都是字符串，则按照字符串的 Unicode 编码大小进行排序
msg_list = ['北京', '尚硅谷', '你好']
msg_list.sort()
print(msg_list)
# 打印 Unicode 编码值
print(ord('你'), ord('北'), ord('尚'))
# 解码 Unicode 值
print(chr(20320), chr(21271), chr(23578))

# 备注：所有的列表方法，都只作用于“当前层”的元素（浅层操作），不会自动进入嵌套的“里层”结构中。 