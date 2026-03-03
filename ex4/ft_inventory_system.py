#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/03 18:09:10 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/03 19:44:50 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def inventary(list: dict) -> None:
    total_item = 0
    for item in list:
        total_item += list[item]

    print(f"Total items in inventory: {total_item}")
    print(f"Unique item types: {len(list)}")


def current_inventory(list: dict) -> None:
    inventary = list.items()
    print(inventary)


def stock_input(list_inpute: list) -> dict:
    list_items = {}

    if len(list_inpute) < 2:
        raise ValueError("no argument [KO]")

    for i in list_inpute:
        list_items.add(i)
    return (list_items)


def main():
    list_items = {}
    try:
        list_items = stock_input(sys.argv)
    except ValueError as e:
        print(f"Error: {e}")

    print("=== Inventory System Analysis ===")
    inventary(list_items)
    print("\n=== Current Inventory ===")
    current_inventory(list_items)


if __name__ == "__main__":
    main()
