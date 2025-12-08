# coding=utf-8
# 新增操作
## 方式一：通过列表的 append 方法，在列表的尾部追加一个元素！
# nums = [10, 20, 30, 40]
# nums.append(50)
# print(nums)

## 方式二：通过列表的 insert 方法，在列表的指定的下标处添加一个元素！
# nums = [10, 20, 30, 40]
# nums.insert(2, 666)
# print(nums)

## 方式三：通过列表的 extend 的方法，将可迭代对象的内容依次取出，追加到列表尾部
# nums = [10, 20, 30, 40]
# nums.extend('尚硅谷')
# nums.extend(range(1, 4))  # [1,4)
# nums.extend([70, 80, 90])
# print(nums)

# 删除操作
## 方式一：通过列表的 pop 方法，删除指定位置的元素，并返回该元素
# nums = [10, 20, 30, 40, 50]
# result = nums.pop(1)
# print(nums)
# print(result)
# 目前只有 pop 方法是有返回值的，其他的方法目前没有返回值！

## 方式二：通过列表的 remove 方法，删除列表中第一次出现的指定值
# nums = [10, 20, 10, 40, 50]
# nums.remove(10) # 删除第一次出现的 10
# print(nums)

## 方式三：通过列表的 clear 方法，删除列表中所有的元素（即清空列表）！
# nums = [10, 20, 10, 40, 50]
# nums.clear()
# print(nums)

## 方式四：通过 del 关键字，删除列表中指定的元素(通过下标[索引值]删除)
# nums = [10, 20, 10, 40, 50]
# del nums[3]
# print(nums)

# 修改操作
## 主要是通过下标进行修改，语法为：列表[下标] = 值
nums = [10, 20, 30, 40, 50]
nums[2] = 66
print(nums)

# 查询操作
## 通过下标进行读取元素，语法为：列表[下标]
nums = [10, 20, 30, 40, 50]
print(nums[2]) # 查询下标为 2 的值

# 新增操作 nums.append(value), nums.insert(index, value), nums.extend(value)
# 删除操作 nums.pop(index), nums.clear(), nums.remove(index), del nums[1]
# 查询操作 nums[index]
# 修改操作 nums[index]=10