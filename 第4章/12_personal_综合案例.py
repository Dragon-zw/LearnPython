# coding =utf-8

print('🏆欢迎来到：答题闯关挑战赛（输入q可随时退出）\n', end='\n')

# 题目与答案
ques1, ans1 = 'Python中用于输出的函数是？', 'print'
ques2, ans2 = 'Python中用于表示逻辑“并且”的关键字是？', 'and'
ques3, ans3 = 'Python属于编译型还是解释型？', '解释型'
# print(f'{ques1}\n{ques2}\n{ques3}\n{ans1}\n{ans2}\n{ans3}')

# 设置游戏问题的尝试最高次数
game_max_tries = 3
# 设置游戏的总关卡
total_level = 3
# 判断游戏是否可玩
playability = True

for level in range(1, total_level + 1):
    print(f'🎯********第{level}关********')
    # 将题目和答案进行环境变量设置
    if level == 1:
        question, answer = ques1, ans1
    elif level == 2:
        question, answer = ques2, ans2
    else:
        question, answer = ques3, ans3
    # print(f'question: {question}\nanswer: {answer}')

    # 设置用户的游戏回答机会
    user_trics = 1
    while user_trics <= game_max_tries:
        print(question)
        user_input = input('请输入你回答问题的答案：')
        if user_input == answer:
            print('✅你的回答正确！\n')
            break
        elif user_input == '':
            print('❎你没有正确的输入内容，请重试！\n')
            continue
        elif user_input == 'q':
            print('⚔️退出游戏！')
            playability = False
            break
        # 判断用户的输入错误配置
        else:
            if user_trics < game_max_tries:
                print('❎你的回答的问题有误，请重新回答！')
                print(f'⏰目前游戏机会是：{game_max_tries - user_trics}\n')
                user_trics += 1
                continue
            else:
                print(f'🎁目前该题目答案：{answer}，需要好好学习！！！\n')
                playability = False
                break
        # 每次进入下一关之前，都要看一下is_playing，如果is_playing为False就要结束游戏！
    if not playability:
        break
# 如果到了这里，is_playing的值依然为True，那就意味着用户已经通关了！
if playability:
    print('🎉🎉🎉恭喜您！全部通关！🎉🎉🎉')