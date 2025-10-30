# 作业 2：彩虹曼陀罗 + 动态旋转光环
# 创意图案：梦幻对称花朵 + 旋转光环动画
# 更多项目：Codewithcurious.com/projects

import turtle
import colorsys
import math

# ------------------- 1. 设置画布 -------------------
s = turtle.Screen()
s.bgcolor("#0a1a3a")           # 深蓝宇宙背景
s.title("彩虹曼陀罗 & 旋转光环")
s.setup(width=900, height=900)
s.tracer(0, 0)                  # 关闭自动刷新，手动控制动画

# ------------------- 2. 创建画笔 -------------------
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

# ------------------- 3. 绘制彩虹曼陀罗 -------------------
def draw_mandala():
    h = 0.0
    n = 180
    for i in range(n):
        c = colorsys.hsv_to_rgb(h, 1.0, 1.0)
        t.color(c)
        t.circle(80 + i * 0.5, 60)   # 画弧
        t.left(95)
        t.circle(60 + i * 0.4, 50)
        t.left(125)
        h += 1 / n

# 画中心曼陀罗
t.penup()
t.goto(0, 0)
t.pendown()
draw_mandala()

# ------------------- 4. 绘制旋转光环（动画） -------------------
rings = []  # 存储每圈的半径、颜色、角度

# 创建 6 圈光环数据
for r in range(120, 421, 50):  # 半径从 120 到 400
    rings.append({
        'radius': r,
        'hue': 0.0,
        'speed': 0.5 + r * 0.001,   # 越大越慢
        'width': max(1, 6 - len(rings))  # 外圈更细
    })

# 动画主循环
angle = 0
while True:
    s.update()        # 手动刷新画面
    t.clear()         # 清除上一帧（保留背景）

    # 重新画曼陀罗（静止）
    draw_mandala()

    # 画每一圈光环
    for ring in rings:
        t.width(ring['width'])
        t.penup()
        t.goto(0, -ring['radius'])
        t.pendown()

        # 计算当前颜色
        c = colorsys.hsv_to_rgb(ring['hue'], 0.8, 1.0)
        t.color(c)

        # 画圆（带轻微透明感效果）
        t.circle(ring['radius'])

        # 更新色相（彩虹流动）
        ring['hue'] = (ring['hue'] + 0.005) % 1.0

        # 模拟“旋转”：通过偏移画虚线圆
        steps = 60
        for i in range(steps):
            if i % 3 == int(angle + ring['radius'] * 0.1) % 3:
                t.pendown()
            else:
                t.penup()
            t.circle(ring['radius'], 360/steps)

    angle += 1
    if angle >= 360:
        angle = 0

    # 控制帧率（不卡顿）
    s.ontimer(lambda: None, 30)