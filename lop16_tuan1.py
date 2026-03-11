print("hello")
print("nam dep zai") 
import turtle

# Thiết lập màn hình và bút vẽ
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(3) # Tốc độ vẽ (1-10)

# Chọn màu sắc
t.color("yellow")
t.begin_fill() # Bắt đầu tô màu

# Thuật toán vẽ sao 5 cánh
for i in range(5):
    t.forward(200)   # Đi thẳng 200 đơn vị
    t.right(144)     # Xoay phải 144 độ

t.end_fill() # Kết thúc tô màu

# Giữ cửa sổ mở cho đến khi bạn click vào
screen.exitonclick()
import turtle
import math

# Thiết lập cửa sổ vẽ
window = turtle.Screen()
window.bgcolor('black') # Nền đen để nổi bật
window.title('Trái tim Barca của Fan!')

# Khởi tạo rùa (bút vẽ)
t = turtle.Turtle()
t.speed(3) # Tốc độ vẽ trung bình
t.pensize(2)
t.hideturtle() # Ẩn rùa

# Màu sắc chính của Barca
BLUE = '#004170'
RED = '#DB002C'
YELLOW = '#FFC107'
WHITE = '#FFFFFF'
BLACK = '#000000'

# Hàm vẽ hình trái tim
def draw_heart(color_fill):
    t.penup()
    t.goto(0, -100) # Điểm đáy trái tim
    t.pendown()
    t.color(color_fill)
    t.begin_fill()
    t.left(140)
    t.forward(111.65)
    
    # Vẽ cung tròn bên trái
    for _ in range(200):
        t.right(1)
        t.forward(1)
        
    t.left(120)
    
    # Vẽ cung tròn bên phải
    for _ in range(200):
        t.right(1)
        t.forward(1)
        
    t.forward(111.65)
    t.end_fill()
    t.setheading(0) # Đặt lại hướng

# Hàm vẽ logo Barca đơn giản hóa bên trong
def draw_barca_logo():
    # Di chuyển vào trung tâm trái tim
    t.penup()
    t.goto(0, 50)
    t.pendown()
    
    # Vẽ khiên
    t.color(WHITE)
    t.begin_fill()
    t.setheading(-90)
    t.forward(100)
    t.circle(50, 180)
    t.forward(100)
    t.setheading(180)
    t.forward(100)
    t.end_fill()
    
    # --- Vẽ phần trên (Cờ Catalan) ---
    # Chữ thập St. George (Chữ thập đỏ trên nền trắng)
    t.penup()
    t.goto(-40, 40)
    t.pendown()
    t.color(RED)
    t.setheading(0)
    t.begin_fill()
    # Vẽ chữ thập
    t.forward(30)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.end_fill()

    # Cờ Senyera (Sọc vàng đỏ)
    t.penup()
    t.goto(10, 40)
    t.pendown()
    t.color(YELLOW)
    t.begin_fill()
    # Vẽ nền vàng
    t.setheading(0)
    t.forward(30)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(40)
    t.end_fill()
    
    # Vẽ sọc đỏ
    t.color(RED)
    t.penup()
    t.goto(15, 40)
    t.pendown()
    t.setheading(-90)
    for _ in range(4):
        t.begin_fill()
        t.forward(40)
        t.left(90)
        t.forward(2)
        t.left(90)
        t.forward(40)
        t.right(90)
        t.forward(2)
        t.end_fill()
        t.