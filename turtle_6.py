import matplotlib.pyplot as plt
import numpy as np

def draw_tangent_circles(radius):
    fig, ax = plt.subplots()

    # Центры кругов
    centers = [(0, 0), (2 * radius, 0), (radius, np.sqrt(3) * radius)]

    # Рисуем круги
    for center in centers:
        circle = plt.Circle(center, radius, color='b', fill=False)
        ax.add_artist(circle)

    # Устанавливаем пределы осей для красивого отображения
    ax.set_xlim(-radius, 3 * radius)
    ax.set_ylim(-0.5 * np.sqrt(3) * radius, 2 * radius)

    # Показываем рисунок
    ax.set_aspect('equal', adjustable='box')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Три круга, касающихся друг друга')
    plt.grid(True)
    plt.show()

radius = float(input("Введите радиус кругов: "))
draw_tangent_circles(radius)