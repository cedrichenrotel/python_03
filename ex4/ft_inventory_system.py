#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/03 18:09:10 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/04 15:01:15 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def total_item(list_inv: dict) -> int:
    total_item = 0
    for item in list_inv:
        total_item += list_inv[item]
    return (total_item)


def inventary(list_inv: dict) -> None:
    total = total_item(list_inv)
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(list_inv)}")


def current_inventory(list_inv: dict) -> None:
    total = total_item(list_inv)
    for item in list_inv:
        percentage = (list_inv[item] / total) * 100
        print(f"{item}: {list_inv[item]} units ({percentage:.1f}%)")


def stock_input(list_inpute: list) -> dict:
    list_items = {}

    if len(list_inpute) == 0:
        raise ValueError("empty entry list [KO]")

    for item in list_inpute:
        if ':' in item:
            name, nb = item.split(':', 1)
            try:
                list_items[name] = int(nb)
            except ValueError:
                raise ValueError("Error: incorrect value [KO]")
        else:
            raise ValueError("incorrect argument [KO]")
    return (list_items)


def inventory_statistics(list_inv: dict) -> tuple:
    value = next(iter(list_inv.items()))
    most_key, most_val = value
    least_key, least_val = value

    for key, val in list_inv.items():

        if (val > most_val):
            most_val = val
            most_key = key
        elif (val < least_val):
            least_val = val
            least_key = key

    return (most_val, most_key), (least_val, least_key)


def item_categories(list_inv: dict) -> tuple:
    moderate = {}
    scare = {}
    for name, value in list_inv.items():
        if value >= 4:
            moderate.update({name: value})
        else:
            scare.update({name: value})

    return (moderate), (scare)


def management_suggestions(list_inv: dict) -> None:
    restock = []
    for key, value in list_inv.items():
        if value < 2:
            restock.append(key)
    print(f"Restock needed: {', '.join(restock)}")


def main():
    list_items = {}
    try:
        if len(sys.argv) < 2:
            raise ValueError("no argument [KO]")
    except ValueError as e:
        print(f"Error: {e}")
        return

    try:
        list_items = stock_input(sys.argv[1:])
    except ValueError as e:
        print(f"Error: {e}")
        return
    most, least = inventory_statistics(list_items)
    mode, scare = item_categories(list_items)
    print("=== Inventory System Analysis ===")
    inventary(list_items)
    print("\n=== Current Inventory ===")
    current_inventory(list_items)
    print("\n=== Inventory Statistics ===")
    print(f"Most abundant:{most[0]} ({most[1]} units)")
    print(f"Least abundant: {least[0]} ({least[1]} unit)")
    print("\n=== Item Categories ===")
    print(f"Moderate: {mode}")
    print(f"Scarce: {scare}")
    print("\n=== Management Suggestions ===")
    management_suggestions(list_items)
    print("\n=== Dictionary Properties Demo ===")


if __name__ == "__main__":
    main()
