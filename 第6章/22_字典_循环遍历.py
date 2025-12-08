# 字典不能使用while循环遍历，但可以使用for循环遍历
d1 = {'张三': 72, '李四': 60, '王五': 85}

# # 使用 for 循环遍历字典（keys）
# for data in d1:
#     print(data)
#     print(f'{data} 的成绩是 {d1[data]}')

for data in d1.keys():
    print(f'{data} 的成绩是 {d1[data]}')

# # 只遍历字典中的值
for data in d1.values():
    print(data)
