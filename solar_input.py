# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet
import matplotlib.pyplot as plt

def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    list_of_data = line.split()
    star.R = float(list_of_data[1])
    star.color = list_of_data[2]
    star.m = float(list_of_data[3])
    star.x = float(list_of_data[4])
    star.y = float(list_of_data[5])
    star.Vx = float(list_of_data[6])
    star.Vy = float(list_of_data[7])
    print(star.Vx, star.Vy)


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """

    list_of_data = line.split()

    planet.R = float(list_of_data[1])
    planet.color = list_of_data[2]
    planet.m = float(list_of_data[3])
    planet.x = float(list_of_data[4])
    planet.y = float(list_of_data[5])
    planet.Vx = float(list_of_data[6])
    planet.Vy = float(list_of_data[7])


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print(out_file, "%s %d %s %f %d %d %f %f" % (obj.type, obj.R, obj.color, obj.m, obj.x, obj.y, obj.Vx, obj.Vy))



def save_statistics(space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Параметры:
    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open("stats.txt", 'a') as out_file:
        for obj in space_objects:
            #print(out_file, "%s %d %s %f" % ('1', 2, '3', 4.5))
            if obj.type == 'star':
                out_file.write('Star %d %s %s %f %f %f %f \n' % (obj.R,
                                                              obj.color,
                                                              obj.m,
                                                              obj.x,
                                                              obj.y,
                                                              obj.Vx,
                                                              obj.Vy))
            else:
                out_file.write('Planet %d %s %s %f %f %f %f \n' % (obj.R,
                                                              obj.color,
                                                              obj.m,
                                                              obj.x,
                                                              obj.y,
                                                              obj.Vx,
                                                              obj.Vy))
        out_file.write("\n")


def clear_statistics():
    with open("stats.txt", 'w') as out_file:
        out_file.write("")

def make_point(obj, t, ax_v, ax_r, ax_vr):
    r = (obj.x**2 + obj.y**2)**0.5
    v =  (obj.Vx**2 + obj.Vy**2)**0.5
    ax_r.scatter(t, r, color="red", s=1)
    ax_v.scatter(t,v, color="red", s=1)
    ax_vr.scatter(r,v, color="red", s=1)
    ax_vr.scatter(r,v, color="red", s=1)

if __name__ == "__main__":
    print("This module is not for direct call!")
