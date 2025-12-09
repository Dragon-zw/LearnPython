import turtle as tt

tt.bgcolor("black") # 设置背景色
tt.speed(0) # 设置画笔速度为最快
colors = ['orange', 'white']

for i in range(122):
    tt.goto(0.0) # 来到画布中心位置
    tt.pencolor(colors[i%2]) # 画笔颜色
    tt.forward(130) # 向前走130个像素
    tt.left(3) # 向左转3度
    tt.circle(40) # 画一个半径为40的圆
    tt.forward(130) # 向前走130个像素
    tt.right(180) # 向右转180度
tt.exitonclick() # 点击窗口关闭