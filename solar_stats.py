# coding: utf-8
# license: GPLv3

from typing import List
import numpy as np
from matplotlib import pyplot as plt

from solar_objects import SpaceObject


def check_system(space_objects) -> bool:
    """Проверяет, можно ли построить график для данной системы (определяет количество тел и их тип).

    Параметры:

    **space_objects** - список объектов.
    """
    planet = 0
    star = 0
    for obj in space_objects:
        if obj.type == "planet":
            planet += 1
        if obj.type == "star":
            star += 1
    if planet == 1 and star == 1:
        return True
    return False


def calculate_speed(space_objects: List[SpaceObject]) -> float:
    """Вычисляет модуль скорости планеты.

    Параметры:

    **space_objects** - список объектов.
    """
    for obj in space_objects:
        if obj.type == "planet":
            return (obj.Vx**2 + obj.Vy**2) ** 0.5
    return 0.0


def calculate_distance(space_objects: List[SpaceObject]) -> float:
    """Вычисляет расстояние между звездой и планетой

    Параметры:

    **space_objects** - список объектов.
    """
    star_pos = None
    planet_pos = None
    for obj in space_objects:
        if obj.type == "star":
            star_pos = (obj.x, obj.y)
        if obj.type == "planet":
            planet_pos = (obj.x, obj.y)
    if planet_pos and star_pos:
        return ((planet_pos[0] - star_pos[0]) ** 2 + (planet_pos[1] - star_pos[1]) ** 2) ** 0.5
    return 0.0


def show_graph(graph_time: np.array, graph_speed: np.array, graph_S: np.array) -> None:
    """Выводит графики, описывающие движения планет.

    Параметры:

    **graph_time** - массив со значениями физического времени от начала отсчёта.

    **graph_speed** - массив со значениями модуля скорсоти планеты.

    **graph_S** - массив со значениями расстояния между планетой и звездой.
    """
    f = plt.figure(figsize=(14, 10))
    ax1 = f.add_subplot(221)
    ax1.plot(graph_time, graph_speed)
    ax1.set_xlabel(r"t, c")
    ax1.set_ylabel(r"$V, \frac{m}{c}$")
    ax1.set_title("Скорость от времени")
    ax1.minorticks_on()
    ax1.grid(which="minor", alpha=0.2)
    ax1.grid(which="major", alpha=1)

    ax2 = f.add_subplot(222)
    ax2.plot(graph_time, graph_S)
    ax2.set_xlabel(r"t, c")
    ax2.set_ylabel(r"$S, m $")
    ax2.set_title("Расстояние от времени")
    ax2.minorticks_on()
    ax2.grid(which="minor", alpha=0.2)
    ax2.grid(which="major", alpha=1)

    ax3 = f.add_subplot(223)
    ax3.plot(graph_S, graph_speed)
    ax3.set_xlabel(r"S, m")
    ax3.set_ylabel(r"$V, \frac{m}{c} $")
    ax3.set_title("Скорость от расстояния")
    ax3.minorticks_on()
    ax3.grid(which="minor", alpha=0.2)
    ax3.grid(which="major", alpha=1)

    plt.show()


if __name__ == "__main__":
    print("This module is not for direct call!")
