# Plan 1
# def calc_total(nums):
#     """
#     计算总运动量（个）
#     :param nums: 每一天的运动量（可变参数）
#     :return: 总运动量（个）
#     """
#     # 此时传入的 nums 是列表
#     return sum(nums) # 可以对列表进行求和

# Plan 2
# *num 则需要打包参数，此时 nums 类型是元组了
def calc_total(*nums):
    """
    计算总运动量（个）
    :param nums: 每一天的运动量（可变参数）
    :return: 总运动量（个）
    """
    # 备注：nums的类型是元组（下一章马上就讲了），sum是内置函数，可以对元组中的数据求和
    return sum(nums) # 可以对列表 | 元组进行求和

def calc_avg(total, days=7):
    """
    计算平均值
    :param total: 总运动量（个）
    :param days: 天数（默认值是7天）
    :return: 平均值
    """
    return total / days


def check_success(total, goal=120):
    """
    判断本次挑战是否成功
    :param total: 总运动量
    :param goal: 运动成功数量（默认值为120）
    :return: 成功或失败的具体信息
    """
    if total >= goal:
        return '✅恭喜！挑战成功！'
    else:
        return '❌抱歉！挑战失败！'


def main(title, duration, goal):
    """
    主函数，用于开始一场挑战赛
    :param title: 比赛标题
    :param duration: 比赛持续天数
    :param goal: 目标运动量
    :return: None
    """
    print(f'【{title}】【{duration}天】✊️挑战赛（请输入每天的数量）')
    # 定义一个 num 列表，用来存储每天的健身数据
    nums = list()

    # 根据duration的值，循环让用户输入
    for index in range(duration):
        nums.append(int(input(f'请输入第{index + 1}天的数据：')))
        index += 1

    # 计算总数
    # Plan 1，传入列表
    # total = calc_total(nums) # 传入的列表
    # Plan 2，解包传参！
    total = calc_total(*nums) # 传入的列表解包，将参数一个个传入到 calc_total 函数

    # 计算平均值
    avg = calc_avg(total, duration)
    # 判断挑战是否成功
    result = check_success(total, goal)
    # 打印相关信息
    print(f'【{title}】【{duration}天】健身总结')
    print(f'总数：{total}，平均值：{avg:.1f}')
    print(result)


main('俯卧撑', 6, 40)
