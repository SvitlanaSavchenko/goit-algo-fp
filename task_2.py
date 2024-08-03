import turtle
import math

def draw_tree(branch_length, angle, level, initial_thickness):
    """
    Рекурсивно малює дерево Піфагора.

    :param branch_length: Довжина початкової гілки.
    :param angle: Кут між гілками.
    :param level: Рівень рекурсії.
    """
    if level <= 0:
        return
    
    # Налаштовуємо товщину лінії
    turtle.pensize(initial_thickness * (level /20))

    # Малюємо основну гілку
    turtle.pencolor("darkred")
    turtle.forward(branch_length)
    
    # Малюємо праву гілку
    turtle.right(angle)
    draw_tree(branch_length * 0.8, angle, level - 1, initial_thickness) 

    # Повертаємося до основної гілки
    turtle.left(2 * angle)
    draw_tree(branch_length * 0.8, angle, level - 1, initial_thickness) 

    # Повертаємося до вихідного положення
    turtle.right(angle)
    turtle.backward(branch_length)

def main():
    """
    Основна функція для налаштування та запуску малювання дерева Піфагора.
    """
    try:
        level = int(input("Введіть рівень рекурсії: "))
        if level < 0:
            raise ValueError("Рівень рекурсії має бути невід'ємним числом.")
    except ValueError as e:
        print(f"Помилка вводу: {e}")
        return

    # Налаштовуємо екран turtle
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Налаштовуємо черепашку
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -screen.window_height() // 2)
    turtle.pendown()
    turtle.speed(0)

    # Малюємо дерево
    draw_tree(180, 30, level, 15)

    # Завершуємо малювання
    turtle.done()

if __name__ == "__main__":
    main()
