# coding=utf-8

# 定义一个临时变量（计算用户的总运动量）
total_num = 0


# 一个健身挑战赛程序
# 定义 calc_total 函数，用于统计总运动量（参数：多天的运动数量）
def calc_total(*exercise):
    """
    定义 calc_total 函数，用于统计总运动量（参数：多天的运动数量）
    :param exercise: 表示运动的每天的目标量
    :return: 返回运动的总量
    """
    total = sum(exercise)
    # print(f'总天数的运动量：{total}')
    return total


# 定义 calc_avg 函数，用于统计平均运动量（参数：总运动量和天数）
def calc_avg(exercise_total, day=7):
    """
    定义 calc_avg 函数，用于统计平均运动量（参数：总运动量和天数）
    :param exercise_total: 表示总运动量
    :param day: 表示天数，默认值为 7
    :return: 返回平均运动量
    """
    return exercise_total / day


# 定义 check_success 函数，用于反馈挑战是否成功（参数：总运动量 和 目标运动量）
def check_success(calc_avg, target=120):
    """
    定义 check_success 函数，用于反馈挑战是否成功（参数：总运动量 和 目标运动量）
    :param calc_avg: 表示用户总运动量
    :param target: 表示用户目标运动量，默认值为 120
    :return: 返回用户反馈挑战是否成功
    """
    if int(calc_avg) < target:
        # print('❎你的健身挑战赛失败了！')
        return False
    else:
        # print('✅你的健身挑战赛成功了！')
        return True


# 定义 main 函数，用于启动一场挑战赛（参数:比赛标题 和 比赛持续天数）
def main(title, day, target):
    """
    定义健身挑战赛程序的入口
    :param title: 表示运动的项目
    :param day: 表示运动的天数
    :param target: 表示运动的每天目标量
    :return: None
    """
    print(f'[运动项：{title}][天：{day}]🏋挑战赛（请输入每天的运动量）')
    print(f'[每天的运动目标]：{target}\n')

    # num1 = int(input('第一天的运动量:'))
    # num2 = int(input('第二天的运动量:'))
    # num3 = int(input('第三天的运动量:'))

    # 定义一个全局变量的累计总数，一个局部变量，每次循环做累加就可以了
    global total_num
    for item in range(1, day + 1):
        user_num = int(input(f'第{item}天的运动量：'))
        total_num = total_num + user_num
        # 测试打印
        # print(temp, user_num)

    # 定义用户总运动量
    # user_exercise_total = calc_total(num1, num2, num3)
    user_exercise_total = calc_total(total_num)
    # print(f'⛳️总天数的运动量：{user_exercise_total}')

    # 定义用户统计平均运动量
    user_calc_avg = calc_avg(user_exercise_total, day)
    # info = '用户的平均运动量：%-3.1f' % user_calc_avg

    # 定义用户挑战是否正常
    user_check_success = check_success(user_calc_avg, target)

    # print(user_check_success)
    print("*************************************")
    print(f'[运动项：{title}][天：{day}]🏖健身总结')
    # 格式化浮点数
    # 方式一：
    # print('总数：%d，平均运动量：%.1f' % (user_exercise_total, user_calc_avg))
    # 方式二：
    print(f'总数：{user_exercise_total}，平均运动量：{user_calc_avg:.1f}')
    # 方式三：
    # print(f'健身锻炼的总数：{user_exercise_total}')
    # print(info)
    if not user_check_success:
        print('❎遗憾！你的健身挑战赛失败了！')
    else:
        print('✅恭喜！你的健身挑战赛成功了！')


main('仰卧起坐', 5, 40)
