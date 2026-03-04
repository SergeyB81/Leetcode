import turtle

# Создаем черепашку
t = turtle.Turtle()
t.speed(5)

# Рисуем разноцветные квадраты
colors = ["red", "blue", "green", "yellow", "purple", "orange"]

for i in range(6):
    t.color(colors[i])
    t.pensize(3)

    # Рисуем квадрат
    for _ in range(4):
        t.forward(100)
        t.right(90)

    # Поворачиваемся перед следующим квадратом
    t.right(60)

turtle.done()