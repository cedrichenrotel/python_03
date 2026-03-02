#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/02 10:23:07 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/02 13:24:01 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def ft_score_analytics(argvs: list[str]) -> None:

    if len(argvs) < 2:
        raise ValueError("invalid argument count")

    total_score = 0
    scores_processed = []

    for i in range(1, len(argvs)):
        try:
            int(argvs[i])
        except ValueError:
            raise ValueError("The input is not a value")
        scores_processed.append(argvs[i])
        total_score += int(argvs[i])

    total_player = i
    average_score = total_score / total_player
    low_score = min_value(scores_processed)
    hight_score = max_value(scores_processed)
    score_range = hight_score - low_score

    print(f"Scores_processed: {scores_processed}")
    print(f"Total players: {total_player}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score:.1f}")
    print(f"High score: {hight_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


def min_value(tab_val: list[int]) -> int:
    nb_min = int(tab_val[1])
    for i in range(len(tab_val)):
        if int(tab_val[i]) < nb_min:
            nb_min = int(tab_val[i])
    return nb_min


def max_value(tab_val: list[int]) -> int:
    nb_max = int(tab_val[1])
    for i in range(len(tab_val)):
        if int(tab_val[i]) > nb_max:
            nb_max = int(tab_val[i])
    return nb_max


def main():
    print("=== Player Score Analytics ===")
    try:
        ft_score_analytics(sys.argv)
    except ValueError as e:
        print(f"No scores provided. Usage: {e}")


if __name__ == "__main__":
    main()
