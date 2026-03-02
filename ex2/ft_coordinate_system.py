#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/02 13:26:09 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/02 21:02:13 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import math
import sys


def parsing(input_value: list[str]) -> list[int]:
    num = []
    if len(input_value) < 2:
        raise ValueError("no argument [KO]")
    for i in range(1, len(input_value)):
        temp = input_value[i].split(',')
        for j in range(len(temp)):
            num.append(int(temp[j]))
    if len(num) < 3:
        raise ValueError(f"insufficient number of arguments: {len(num)} "
                         "[KO]")
    elif len(num) > 3:
        raise ValueError(f"limit of argument to exceed: {len(num)} [KO]")
    return num


def distance_formula(p1: tuple, p2: tuple) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return (distance)


def ft_coordinate_system(input_value: list[str]) -> None:
    try:
        num = parsing(input_value)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        raise ValueError(f"ValueError, Args: (\"{e}\")")

    p1 = (num[0], num[1], num[2])
    p2 = (0, 0, 0)
    coordinate = distance_formula(p1, p2)

    print("=== Game Coordinate System ===")
    print(f"Position created: {p1}")
    print(f"Distance between {p1} and {p2}: {coordinate:.2f}")
    print("\nUnpacking demonstration:")
    print(f"Player at x={p1[0]}, y={p1[1]}, z={p1[2]}")
    print(f"Coordinates: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")


def main():
    try:
        ft_coordinate_system(sys.argv)
    except ValueError as e:
        print(f"Error details - Type: {e}")


if __name__ == "__main__":
    main()
