import turtle
import random

# Настройка экрана
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Волшебный художник 🎨")
screen.setup(800, 600)

# Создание черепашки-художника
artist = turtle.Turtle()
artist.speed(0)  # Максимальная скорость
artist.width(2)  # Толщина линии

# Список ярких цветов
colors = ["red", "yellow", "blue", "green", "orange", "purple",
          "pink", "cyan", "magenta", "lime"]

# Рисуем волшебный цветок!
for i in range(36):  # 36 лепестков
    # Выбираем случайный цвет
    artist.color(random.choice(colors))

    # Рисуем один лепесток
    artist.circle(100)  # Круг - лепесток

    # Поворачиваемся для следующего лепестка
    artist.right(10)

# Рисуем серединку
artist.penup()
artist.goto(0, 0)
artist.pendown()
artist.color("gold")
artist.begin_fill()
artist.circle(30)
artist.end_fill()

# Пишем поздравление
artist.penup()
artist.goto(0, -250)
artist.color("white")
artist.write("Волшебный цветок!", align="center", font=("Arial", 24, "bold"))

# Прячем черепашку
artist.hideturtle()

# Чтобы окно не закрывалось
screen.exitonclick()