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
for key in fruits:
    print(f'水果的名称：{key}, 价格是 {fruits[key]} 元/斤')

# 需求2: 找到最贵水果
# print(fruits.get('苹果')) # 4.5

# max 函数通过 key 参数指定比较规则，这里用 fruits.get 获取对应的价格进行比较
# max 函数进行比较的时候，先使用 fruits.get 获取 key 所对应的 values(预处理)，再进行比较
# 返回值是 values 值所对应的 key
key = max(fruits, key=fruits.get) # 比较水果价格
print(f'最贵的水果是 {key}，价格是 {fruits[key]} 元/斤')

# ------------------------------------------------------------------------
print('*' * 50)
# 练习二:学生成绩表
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
for stu in students:
    # 获取当前学生的成绩列表
    score_list = stu['scores'].values()
    # 计算平均分
    avg_score = sum(score_list) / len(score_list)
    # 打印结果
    print(f"{stu['name']} 的平均分是：{avg_score:.1f}")

# 需求2: 找到总分最高的学生
def find_best():
    # 变量：记录分数最高的学生
    best_students = []
    # 变量：记录分数最高的分数
    best_score = 0
    # 循环遍历
    for stu in students:
        # 获取当前学生的成绩列表
        score_list = stu['scores'].values()
        # 计算当前学生的总分
        total_score = sum(score_list)
        # 判断当前学生的总分是否比最高分高
        if total_score > best_score:
            # 如果当前学生的总分比最高分高，则更新最高分和最高学生的信息
            best_score = total_score
            best_students = [stu['name']]
        # 当前学生的成绩与最高分相同，就加入列表
        elif total_score == best_score:
            best_students.append(stu['name'])
    # 打印结果
    print(f"总分最高的学生是 {best_students}，总分是 {best_score}")

find_best()
# ------------------------------------------------------------------------
print('*' * 50)
# 练习三:评论内容

comment= '这家奶茶真好喝，环境也不错就是价格有点贵，好喝好喝好喝！强烈推荐！'

# 需求1: 统计“好喝”出现次数
result = comment.count('好喝')
print(f'“好喝”出现次数：{result}')

# 需求2: 将字符串中的“贵”替换为“略高”
result = comment.replace('贵', '略高')
print(f'替换后的字符串是：{result}')

# 需求3: 是否包含“推荐”两个字
result = '推荐' in comment
print(f'是否包含“推荐”两个字：{result}')