# coding: utf-8
# license: GPLv3
import random
from typing import List
from solar_objects import SpaceObject
from solar_world import World

gravitational_constant = 6.67408e-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body: SpaceObject, space_objects: List[SpaceObject], scale_factor) -> None:
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """
    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        r = ((body.x - obj.x) ** 2 + (body.y - obj.y) ** 2) ** 0.5
        #tga = (body.y-obj.y)/(body.x-obj.x)
        #if tga == 0: tga+=0.001
        #body.F=gravitational_constant*body.m*obj.m/r**2
        r = ((body.x - obj.x) ** 2 + (body.y - obj.y) ** 2) ** 0.5
        body.Fx=gravitational_constant*body.m*obj.m*(obj.x-body.x)/r**3
        body.Fy=gravitational_constant*body.m*obj.m*(obj.y-body.y)/r**3
        #body.Fx = (abs((body.F/tga)**2-1))**0.5
        #body.Fy = (abs(body.F**2-body.Fx**2))**0.5
        pass  
    hit_test_space_objects(body, space_objects, scale_factor)

def move_space_object(body: SpaceObject, dt: int) -> None:
    """Перемещает тело в соответствии с действующей на него силой. В случае столкновения скорости тел изменяются

    Параметры:

    **body** — тело, которое нужно переместить.

    **space_objects** - список объектов.

    **scale_factor** - масштабный коэффициент.

    **dt** - шаг по времени.
    """
    
    body.Vx += body.Fx / body.m * dt
    body.Vy += body.Fy/body.m *dt
    body.x += body.Vx * dt
    body.y += body.Vy *dt


def hit_test_space_objects(body: SpaceObject, space_objects: List[SpaceObject], scale_factor: float) -> None:
    """
    Проверяет столкнулись ли объекты или нет

    При столкновении удаляет один из столкнувшихся объектов и изменяет второй, как-будто эти два объекта слиплись в один

    Параметры:

    **body** - основной объект, для которого проверяется столкнулся ли он с другими объектами

    **space_objects** - список всех объектов

    **scale_factor** - Масштабирование экранных координат по отношению к физическим. Мера: количество пикселей на один метр.
    """
    for obj in space_objects:
        if body == obj:
            continue
        x = obj.x - body.x
        y = obj.y - body.y
        r_obj = obj.R / scale_factor
        r_body = body.R / scale_factor
        if (obj.alive == 1) and (float((x**2 + y**2)) <= float((r_obj + r_body) ** 2)):
            body.Vx = (body.m * body.Vx + obj.m * obj.Vx) / (body.m + obj.m)
            body.Vy = (body.m * body.Vy + obj.m * obj.Vy) / (body.m + obj.m)
            body.Fx = body.Fy = 0
            body.x = (body.m * body.x + obj.m * obj.x) / (body.m + obj.m)
            body.y = (body.m * body.y + obj.m * obj.y) / (body.m + obj.m)
            body.R = (2 * (body.m + obj.m) / (body.m / body.R**3 + obj.m / obj.R**3)) ** (1 / 3)
            body.m = body.m + obj.m
            body.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
            obj.alive = 0
            space_objects.remove(obj)


def recalculate_space_objects_positions(space_objects: List[SpaceObject], scale_factor: float, dt: int) -> None:
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список объектов, для которых нужно пересчитать координаты.

    **scale_factor** - масштабный коэффициент.

    **dt** — шаг по времени.
    """
    for body in space_objects:
        calculate_force(body, space_objects, scale_factor)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
