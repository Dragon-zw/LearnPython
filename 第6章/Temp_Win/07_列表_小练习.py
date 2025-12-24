# coding=utf-8

print('📋成绩统计程序，可以对多名学生的成绩，进行统计和分析，用户输入“结束”字符串。')
# 定义全局的列表
score_list = []

while True:
    score = input('请输入学生成绩：')
    if score == '结束':
        break
    else:
        score_list.append(int(score))

# 判断 score_list 中是否有数据
# 如果 score_list 中有数据，则开始统计
# 无论使用哪一种数据容器，如果容器中一个元素都没有，那在判断中则为 False
if score_list:
    print('✅学生成绩列表：', score_list)
    # 判断合格人数
    standard_people = 0
    for item in score_list:
        if item >= 60:
            standard_people += 1

    # 判断优秀人数
    excellent_people = 0
    for item in score_list:
        if item >= 90:
            excellent_people += 1

    # 开始进行统计和分析
    print('💁总人数: ', len(score_list), '名')
    print('🔺最高分: ', max(score_list), '分')
    print('🔻最低分: ', min(score_list), '分')
    print('✅合格人数: ', standard_people, '名')
    print(f'📈合格率: {standard_people / len(score_list) * 100:.1f} %')
    print('🏆优秀人数: ', excellent_people, '名')
    print(f'📈优秀率: {excellent_people / len(score_list) * 100:.1f} %')
    print(f'🎨平均分: {sum(score_list) / len(score_list):.1f} 分')

else:
    print('❎没有输入任何成绩！')
