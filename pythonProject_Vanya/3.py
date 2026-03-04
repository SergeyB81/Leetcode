import turtle

# Настройка
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Нажми на кнопки!")

# Создаем черепашку
pen = turtle.Turtle()
pen.shape("turtle")
pen.pensize(3)

# Функции для управления
def move_forward():
    pen.forward(20)

def move_backward():
    pen.backward(20)

def turn_left():
    pen.left(15)

def turn_right():
    pen.right(15)

def change_color():
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    pen.color(random.choice(colors))

def clear_screen():
    pen.clear()

def pen_up():
    pen.penup()

def pen_down():
    pen.pendown()

# Привязываем клавиши
screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear_screen, "c")
screen.onkey(pen_up, "u")
screen.onkey(pen_down, "d")

print("Управление:")
print("Стрелки - движение")
print("C - очистить экран")
print("U - поднять ручку")
print("D - опустить ручку")

turtle.done()