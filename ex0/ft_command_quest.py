#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_command_quest.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/27 13:06:24 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/09 07:26:57 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def ft_command_quest(argv) -> None:
    print("=== Command Quest ===")
    if len(argv) < 2:
        print("No arguments provided!")
        print(f"Program name: {argv[0]}")
        print(f"Total arguments: {len(argv)}")
    else:
        print(f"Program name: {argv[0]}")
        print(f"Arguments received: {len(argv) - 1}")
        for i in range(1, len(argv)):
            print(f"Argument {i}: {argv[i]}")
        print(f"Total arguments: {len(argv)}")


def main():
    ft_command_quest(sys.argv)


if __name__ == "__main__":
    main()
