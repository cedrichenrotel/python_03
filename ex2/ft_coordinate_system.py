#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/02 13:26:09 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/02 14:45:19 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import math
import sys


def distance_formula(x1: int, y1: int, z1: int,
                     x2: int, y2: int, z2: int) -> float:

    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return (distance)


def ft_coordinate_system(input_value: list[str]) -> None:
    for i in range(1, len(input_value)):
        try:
            int(input_value[i])
        except ValueError:
            raise ValueError(f"Parsing invalid coordinates:{input_value}")





def main():
    try:
       ft_coordinate_system(sys.argv)
    except ValueError as e:
        print(f"rror details - Type: {e}")


if __name__ == "__main__":
    main()
