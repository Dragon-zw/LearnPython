# coding=utf-8

print('请输入学生成绩，输入"结束"停止录入：')
score_list = []

# 持续输入，让用户输入学生成绩！
while True:
    data = input('请输入成绩：')

    if data == '结束':
        break
    else:
        score_list.append(int(data))

# 如果 score_list 中有数据，则开始统计
# 无论使用哪一种数据容器，如果容器中一个元素都没有，那在判断中则为 False
if score_list: # 可以判断列表中是否有数据
    # 统计平均分
    avg = sum(score_list) / len(score_list)
    # 统计合格人数
    pass_count = 0
    # 统计优秀人数
    excellent_count = 0
    # 遍历列表，开始统计
    for item in score_list:
        # 判断学习成绩大于等于 60
        if item >= 60:
            pass_count += 1
        # 判断学习成绩大于等于 90
        if item >= 90:
            excellent_count += 1
    # 合格率
    pass_rate = pass_count / len(score_list) * 100
    # 优秀率
    excellent_rate = excellent_count / len(score_list) * 100
    print('********⬇️统计信息如下⬇️********')
    print(f'🧑‍🎓总人数为：{len(score_list)}')
    print(f'🔺最高分为：{max(score_list)}')
    print(f'🔻最低分为：{min(score_list)}')
    print(f'✅合格人数：{pass_count}人')
    print(f'📈合格率为：{pass_rate:.1f}%')
    print(f'🏆优秀人数：{excellent_count}人')
    print(f'📈优秀率为：{excellent_rate:.1f}%')
    print(f'📊平均分数：{avg:.1f}')

else:
    print('您没有输入任何成绩！')