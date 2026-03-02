#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/02 13:26:09 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/02 15:19:42 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import math
import sys


def distance_formula(p1: tuple, p2: tuple) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return (distance)


def ft_coordinate_system(input_value: list[str]) -> None:
    if len(input_value) != 7:
        raise ValueError("incorrect number of values")
    num = []
    for i in range(1, len(input_value)):
        try:
            int(input_value[i])
        except ValueError:
            raise ValueError(f"Parsing invalid coordinates:{input_value}")
        float(num.append(input_value[i]))

        p1 = (num[0], num[1], num[2])
        p2 = (num[3], num[4], num[5])
        return p1, p2

def main():
    try:
       ft_coordinate_system(sys.argv)
    except ValueError as e:
        print(f"rror details - Type: {e}")


if __name__ == "__main__":
    main()
