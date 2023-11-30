# coding: utf-8
# license: GPLv3

import yaml
from typing import List
from solar_objects import SpaceObject
from solar_vis import DrawableObject


def read_space_objects_data_from_yaml(input_filename) -> List[SpaceObject]:
    """Функция считывает словарь параметров из файла и передает их в объект"""
    with open(input_filename, "r") as input_file:
        configs = yaml.safe_load(input_file)
        list_spaceobjects = []
        for config in configs:
            list_spaceobjects.append(SpaceObject(**config))
    return list_spaceobjects


def write_space_objects_data_to_yaml(output_filename, space_objects: List[SpaceObject]) -> None:
    """Функция преобразует объекты в список словарей и записывает в файл"""
    with open(output_filename, "w") as output_file:
        for space_object in space_objects:
            yaml.safe_dump(space_object.__dict__, output_file)


if __name__ == "__main__":
    print("This module is not for direct call!")
