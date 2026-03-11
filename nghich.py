import turtle
import math

# Thiết lập màn hình
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0) # Tắt vẽ từng nét để hiệu ứng mượt hơn

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Công thức toán học cho hình trái tim (Parametric Equation)
# x = 16 * sin(t)^3
# y = 13 * cos(t) - 5 * cos(2t) - 2 * cos(3t) - cos(4t)

def draw_heart(scale):
    t.penup()
    for i in range(0, 360):
        angle = math.radians(i)
        x = 16 * math.sin(angle)**3
        y = 13 * math.cos(angle) - 5 * math.cos(2*angle) - 2 * math.cos(3*angle) - math.cos(4*angle)
        
        t.goto(x * scale, y * scale)
        if i == 0:
            t.pendown()
            t.color("red")
            t.begin_fill()
    t.end_fill()

# Thuật toán tạo nhịp đập
scale = 10
direction = 0.2

while True:
    t.clear()
    draw_heart(scale)
    screen.update()
    
    # Thay đổi kích thước để tạo hiệu ứng đập
    scale += direction
    if scale > 15 or scale < 10:
        direction *= -1 # Đảo ngược hướng tăng/giảm

screen.mainloop()