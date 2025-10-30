# 作业 3：极光凤凰 · 彩焰重生
# 创意图案：动态凤凰 + 极光翅膀 + 粒子尾迹
# 更多项目：Codewithcurious.com/projects

import turtle
import colorsys
import random
import math

# ------------------- 1. 设置画布 -------------------
s = turtle.Screen()
s.bgcolor("#000818")                    # 深空蓝背景
s.title("Cool")
s.setup(width=1000, height=700)
s.tracer(0, 0)                           # 开启手动动画

# ------------------- 2. 创建画笔 -------------------
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# ------------------- 3. 极光背景（流动） -------------------
def draw_aurora():
    t.penup()
    t.goto(-500, 150)
    for x in range(-500, 501, 20):
        y = 150 + 80 * math.sin(x * 0.02 + frame * 0.05)
        h = (x + frame) % 360 / 360
        c = colorsys.hsv_to_rgb(h, 0.8, 0.6)
        t.goto(x, y)
        t.pendown()
        t.color(c)
        t.width(40)
        t.goto(x, 300)
        t.penup()

# ------------------- 4. 绘制凤凰主体 -------------------
def draw_phoenix_body():
    # 身体（金色火焰）
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.color("#ffaa00")
    t.begin_fill()
    t.circle(40)
    t.end_fill()

    # 头部
    t.penup()
    t.goto(0, 10)
    t.pendown()
    t.color("#ff6600")
    t.begin_fill()
    t.goto(-15, 30)
    t.goto(15, 30)
    t.goto(0, 10)
    t.end_fill()

    # 眼睛
    t.penup()
    t.goto(-8, 25)
    t.pendown()
    t.color("white")
    t.dot(6)
    t.goto(8, 25)
    t.dot(6)

# ------------------- 5. 极光翅膀（彩虹流动） -------------------
def draw_wing(x, y, size, hue_offset):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(36):
        h = (i * 10 + frame + hue_offset) % 360 / 360
        c = colorsys.hsv_to_rgb(h, 1.0, 1.0)
        t.color(c)
        t.width(3)
        angle = i * 10
        dx = size * math.cos(math.radians(angle))
        dy = size * math.sin(math.radians(angle)) - 30
        t.goto(x + dx, y + dy)
        t.goto(x, y)

# ------------------- 6. 粒子尾迹 -------------------
particles = []
def create_particle():
    if random.random() < 0.6:
        particles.append({
            'x': random.randint(-30, 30),
            'y': -70,
            'vx': random.uniform(-2, 2),
            'vy': random.uniform(-5, -1),
            'life': random.randint(20, 40),
            'hue': random.random()
        })

def update_particles():
    for p in particles[:]:
        p['x'] += p['vx']
        p['y'] += p['vy']
        p['vy'] -= 0.1
        p['life'] -= 1
        if p['life'] <= 0:
            particles.remove(p)
        else:
            c = colorsys.hsv_to_rgb(p['hue'], 1.0, p['life']/40)
            t.penup()
            t.goto(p['x'], p['y'])
            t.pendown()
            t.color(c)
            t.dot(4 + p['life']/10)

# ------------------- 7. 主动画循环 -------------------
frame = 0
while True:
    t.clear()
    frame += 1

    # 1. 流动极光背景
    draw_aurora()

    # 2. 凤凰身体
    draw_phoenix_body()

    # 3. 左翅（极光）
    draw_wing(-60, -20, 120, 100)

    # 4. 右翅（极光）
    draw_wing(60, -20, 120, 200)

    # 5. 粒子尾迹
    create_particle()
    update_particles()

    # 6. 尾巴火焰
    t.penup()
    t.goto(0, -80)
    t.pendown()
    t.color("#ff3300")
    t.width(15)
    t.goto(0, -120)
    t.width(8)
    t.goto(0, -150)

    # 7. 刷新画面
    s.update()

    # 控制帧率
    s.ontimer(lambda: None, 50)