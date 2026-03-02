#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_command_quest.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/27 13:06:24 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/02 10:20:26 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def ft_command_quest(sys) -> None:
    print("=== Command Quest ===")
    if len(sys) < 2:
        print("No arguments provided!")
        print(f"Program name: {sys[0]}")
        print(f"Total arguments: {len(sys)}")
    else:
        print(f"Program name: {sys[0]}")
        print(f"Arguments received: {len(sys) - 1}")
        for i in range(1, len(sys)):
            print(f"Argument {i}: {sys[i]}")
        print(f"Total arguments: {len(sys)}")


def main():
    ft_command_quest(sys.argv)


if __name__ == "__main__":
    main()
