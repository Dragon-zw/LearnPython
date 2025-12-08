# coding=utf-8

# 定义一个空列表
score_list = []
# 定义合格人数和优秀人数
standard_people = 0
excellent_people = 0
# 定义总分数
total_score = 0
# 定义平均分数
avg_score = 0


def print_score(score_list, standard_people, excellent_people, avg_score):
    """
    用于打印成绩结果
    :param score_list: 学生成绩列表
    :param standard_people: 合格的学生人数
    :param excellent_people: 优秀的学生人数
    :return: None
    """
    print('********⬇️统计信息如下⬇️********')
    print('👨‍🎓总人数：', len(score_list))
    print(f'🥇最高分：{max(score_list)}\n🥉最低分：{min(score_list)}')
    print(f'✅合格人数：{standard_people}人')
    print(f'📈合格率：{standard_rate:.1f}%')
    print(f'🏆优秀人数：{excellent_people}人')
    print(f'📈优秀率：{excellent_rate:.1f}%')
    print(f'📊平均分数：{avg_score:.1f}')


print('请输入学生的成绩，输入"结束"则结束输入学习成绩并会总结')
# 持续输入，让用户输入学生成绩！
while True:
    study_score = input('⛳️请输入学生成绩：')
    if study_score == '结束':
        break
    else:
        # 不断地追加列表
        score_list.append(int(study_score))
        # 每个成绩被多次统计：第n次输入时，前n - 1个成绩会被重复遍历

if score_list:
    # 该逻辑不能放到 while 语句中，否则最终 standard_people和 excellent_people的值会是实际合格人数的平方级增长
    for nums in score_list:
        # 合格人数（成绩分数大于等于 60）的逻辑
        if nums >= 60:
            standard_people = standard_people + 1
        # 优秀人数（成绩分数大于等于 90）的逻辑
        if nums >= 90:
            excellent_people = excellent_people + 1
        # 平均分数的逻辑
        total_score = total_score + int(nums)
    # 合格率的逻辑
    standard_rate = standard_people / len(score_list) * 100
    # 优秀率的逻辑
    excellent_rate = excellent_people / len(score_list) * 100
    # 平均分数的逻辑
    avg_score = total_score / len(score_list)

    print_score(score_list, standard_people, excellent_people, avg_score)
else:
    print('您没有输入任何成绩！')
