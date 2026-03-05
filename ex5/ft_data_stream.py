#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/05 07:13:26 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/05 14:20:14 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import time
from random import choice
from typing import Generator


def generator_data(player: list, level: list, action: list) -> Generator:

    for _ in range(1000):
        event = {"player": choice(player), "level": choice(level),
                 "action": choice(action)}
        yield event


def print_generator(player: list, level: list, action: list) -> Generator:
    total = 0
    high_level = 0
    treasure = 0
    Level_up = 0

    flux = (generator_data(player, level, action))
    for event in flux:
        if total < 3:
            print(f"Event {total + 1}: {event['player']} "
                  f"(level {event['level']}) {event['action']}")
        if event["level"] >= 10:
            high_level += 1
        if event["action"] == "found treasure":
            treasure += 1
        if event["action"] == "leveled up":
            Level_up += 1
        total += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"high_level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {Level_up}")
    print()
    print("Memory usage: Constant (streaming)")


def generator_demonstration() -> None:
    n = 10
    a, b = 0, 1
    fibonacci = []

    for _ in range(n):
        fibonacci.append(str(a))
        a, b = b, a + b
    print(f"Fibonacci sequence (first 10): {', '.join(fibonacci)}")

    prime = []

    for i in range(2, 100):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime.append(str(i))
    print(f"Prime numbers (first {5}): {', '.join(prime[:5])}")


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
    start = time.time()
    print_generator(player, level, action)
    end = time.time()
    print(f"Processing time: {end - start:.3f} seconds")
    print("\n=== Generator Demonstration ===")
    generator_demonstration()


if __name__ == "__main__":
    main()
