#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/02 13:26:09 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/09 08:29:19 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import math
import sys


def parsing(input_value: list[str]) -> list[int]:
    num = []
    if len(input_value) < 2:
        raise ValueError("no argument input [KO]")
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

    num = parsing(input_value)

    p1 = (num[0], num[1], num[2])
    p2 = (0, 0, 0)
    coordinate = distance_formula(p1, p2)

    x, y, z = p1
    print(f"Parsed position: {p1}")
    print(f"Distance between: {p1} and {p2}: {coordinate:.2f}")
    print("\nUnpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def main():
    print("=== Game Coordinate System ===")
    try:
        ft_coordinate_system(sys.argv)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")


if __name__ == "__main__":
    main()
