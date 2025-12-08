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
# for item in fruits:
#     print(f'水果的名称：{item}, 价格是 {fruits[item]} 元/斤')

# 需求2: 找到最贵水果
# print(fruits.get('苹果')) # 得到 key 所对应的 values

# 方式 1：
# 在进行比较的时候，先使用 fruits.get 获取 key 所对应的 values，再进行比较
# 返回值是 values 值所对应的 key
# 以后在实际开发工作中，使用非常多该格式！
# fruits_max = max(fruits, key=fruits.get)
# print(f'最贵水果是 {fruits_max},价格是 {fruits[fruits_max]} 元/斤')

# 方式 2：
# print(max(fruits.values()))  # 12.0
# for key, value in fruits.items():
#     if value == max(fruits.values()):
#         print(f'最贵水果是 {key},价格是 {value} 元/斤')

# ------------------------------------------------------------------------

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
# 方式 1：

# 方式 2：
# for student in students:
#     # 打印学生的名字
#     print(student['name'], end=',')
#     # 打印学生的平均分
#     print(f'你的平均分是：{sum(student['scores'].values()) / len(student['scores']):.1f}')

# 需求2: 找到总分最高的学生
# 方式 1：
# 这段代码的作用是找到总分最高的学生并打印其信息
# 使用max函数配合lambda表达式找出总分最高的学生
# lambda student: sum(student['scores'].values()) 计算每个学生的总分
max_student = max(students, key=lambda student: sum(student['scores'].values()))
print(f"总分最高的学生是：{max_student['name']}，总分：{sum(max_student['scores'].values())}")

# 方式 2：


# ------------------------------------------------------------------------

# 练习三:评论内容

# comment = '这家奶茶真好喝，环境也不错就是价格有点贵，好喝好喝好喝！强烈推荐！'

# 需求1: 统计“好喝”出现次数
# result = comment.count('好喝')
# print(f'“好喝”出现次数：{result}')

# 需求2: 将字符串中的“贵”替换为“略高”
# 将字符串中的“贵”替换为“略高”
# print(comment.replace('贵', '略高'))

# 需求3: 是否包含“推荐”两个字
# result = '推荐' in comment
# print(f'是否包含“推荐”两个字：{result}')
