# coding=utf-8

# 练习1:水果清单
fruits = {
    '苹果': 4.5,
    '香蕉': 3.2,
    '橙子': 5.8,
    '草莓': 12.0,
    '哈密瓜': 8.8
}

# 需求1: 打印所有的水果
for key, value in fruits.items():
    print(f'水果的名称: {key}, 价格是 {value} 元/斤')
    
# 需求2: 找到最贵水果
max_fruit_price = max(fruits.values())
# print(max_fruit_price)

for key, value in fruits.items():
    if value == max_fruit_price:
        print(f'最贵的苹果是 {key}, 其价格是 {value} 元/斤')

# -----------------------------------------------------------------------
print('*' * 50)
# 练习二:学生成绩表
# students 是列表
students = [
    {
        'name': '张三',
        'scores': {'语文': 88, '数学': 92, '英语': 95}
    },
    {
        'name': '李四',
        'scores': {'语文': 75, '数学': 83, '英语': 80}
    },
    {
        'name': '王五',
        'scores': {'语文': 92, '数学': 95, '英语': 88}
    }
]

# 需求1: 计算每位学生的平均分
# 列表信息：遍历 Students 列表
# for item in students:
#     print(item)
#     # 打印学生姓名
#     print(item['name'])
#     # 打印学生成绩
#     print(item['scores'].values())

# 计算每位学生的平均分
for stu in students:
    # 打印学生的成绩
    stu_scores = stu['scores'].values()
    # 计算学生的平均分
    stu_avg_score = sum(stu_scores) / len(stu_scores)
    # 打印学生的平均分
    print(f'{stu['name']} 的平均分是 {stu_avg_score:.1f}')

# 需求2: 找到总分最高的学生（考虑同分和特殊情况）
if not students:
    print("没有学生信息。")
else:
    max_total_score = None
    top_students = []

    # 先计算每个学生的总分，并找到最高分
    for stu in students:
        total_score = sum(stu['scores'].values())
        if (max_total_score is None) or (total_score > max_total_score):
            max_total_score = total_score
            top_students = [stu['name']]
        elif total_score == max_total_score:
            top_students.append(stu['name'])

    if len(top_students) == 1:
        print(f'总分最高的学生是 {top_students[0]}, 总分为 {max_total_score}')
    else:
        print(f'总分最高的学生有: {", ".join(top_students)}, 总分为 {max_total_score}')

# ------------------------------------------------------------------------
print('*' * 50)
# 练习三:评论内容

comment = '这家奶茶真好喝，环境也不错就是价格有点贵，好喝好喝好喝！强烈推荐！'

# 需求1: 统计“好喝”出现次数
result = comment.count('好喝')
print(f'"好喝"字数出现了 {result} 次')

# 需求2: 将字符串中的“贵”替换为“略高”
new_str = comment.replace('贵','略高')
print(new_str)

# 需求3: 是否包含“推荐”两个字
result = '推荐' in comment
print(f'包含"推荐"两个字: {result}')