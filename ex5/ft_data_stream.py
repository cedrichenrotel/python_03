#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/05 07:13:26 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/05 09:50:33 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from random import choice
from typing import Generator


def game_data_stream(player: list, level: list, action: list) -> Generator:

    for i in range(1000):
        if i < 3:
            event = {"player": choice(player), "level": choice(level),
                     "action": choice(action)}
            yield (f"Event{i}: {event['player']} ({event['level']})"
                   f" {event['action']}")


def print_generator(player: list, level: list, action: list) -> None:
    flux = (game_data_stream(player, level, action))
    for event in flux:
        print(event)


def main():
    player = ["alice", "bob", "charlie"]
    level = range(20)
    action = [
        "killed monster",
        "found treasure",
        "leveled up"
    ]

    print("=== Game Data Stream Processor ===")
    print("\nProcessing 1000 game events...")
    print()
    print_generator(player, level, action)


if __name__ == "__main__":
    main()
