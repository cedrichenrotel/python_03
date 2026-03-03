#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/03 07:29:23 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/03 14:54:11 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def print_player_and_achievement(list_player: dict) -> None:
    for player in list_player:
        print(f"Player {player} achievements:{list_player[player]}")


def print_nb_total_achievement(list_player: dict) -> None:
    achievement = set()

    for player in list_player:
        achievement = achievement.union(list_player[player])
    nb_achievement = len(achievement)
    print(f"All unique achievements: {achievement}")
    print(f"Total unique achievements: {nb_achievement}")


def print_rare_achivement(list_player: dict) -> None:
    achievement = set()
    rare = set()

    for player in list_player:
        achievement = achievement.union(list_player[player])

    for i in achievement:
        count = 0
        for j in list_player:
            if i in list_player[j]:
                count += 1
        if count == 1:
            rare.add(i)
    print(f"Rare achievements (1 player): {rare}")


def print_common_achivement(list_player: dict) -> None:
    common = set(next(iter(list_player.values())))

    for player in list_player:
        common = common.intersection(list_player[player])

    print(f"Common to all players: {common}")


def print_common_achi_alice(p1: dict, p2: dict) -> None:
    common = p1.intersection(p2)
    a_unique = p1.difference(p2)
    b_unique = p2.difference(p1)

    print(f"Alice vs Bob common: {common}")
    print(f"Alice unique: {a_unique}")
    print(f"Bob unique: {b_unique}")


def main():
    list_player = {
        "Alice": {'first_kill',
                  'level_10',
                  'treasure_hunter',
                  'speed_demon'},

        "Bob": {'first_kill',
                'level_10',
                'boss_slayer',
                'collector'},

        "Charlie": {'level_10',
                    'treasure_hunter',
                    'boss_slayer',
                    'speed_demon',
                    'perfectionist'}
    }

    print("=== Achievement Tracker System ===")
    print()
    print_player_and_achievement(list_player)
    print("\n=== Achievement Analytics ===")
    print_nb_total_achievement(list_player)
    print()
    print_common_achivement(list_player)
    print_rare_achivement(list_player)
    print()
    print_common_achi_alice(list_player["Alice"], list_player["Bob"])


if __name__ == "__main__":
    main()
