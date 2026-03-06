#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_analytics_dashboard.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/05 14:22:31 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/06 16:35:38 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def List_Comprehension_Examples(player: dict) -> None:
    High_scorers = [i['name'] for i in player
                    if i['score'] > 2000]
    Scores_doubled = [i['score']*2 for i in player]
    Active_players = [i['name'] for i in player
                      if i['active'] is True]

    print(f"High scorers (>2000): {High_scorers}")
    print(f"Scores doubled: {Scores_doubled}")
    print(f"Active players: {Active_players}")


def Dict_Comprehension_Examples(player: list, lst_achivement: dict) -> None:

    Player_scores = {i["name"]: i["score"] for i in player}

    categories = {
        cat: len([p for p in player if (
            p['score'] > 2000 if cat == 'high' else
            p['score'] >= 1500 if cat == 'medium' else
            p['score'] < 1500
        )])
        for cat in ['high', 'medium', 'low']
    }

    Achievement = {ach for player in lst_achivement
                   for ach in lst_achivement[player]}

    regions = {p['region'] for p in player}

    print(f"Player scores: {Player_scores}")
    print(f"Score categories: {categories}")
    print(f"Unique achievements: {Achievement}")
    print(f"Active regions: {regions}")


def Combined_Analysis(player: list, lst_achivement: dict) -> None:

    achivement = len(set((ach for player in lst_achivement
                     for ach in lst_achivement[player])))

    Average_score = (sum(p['score'] for p in player) / len(player))

    print(f"Total players: {len(player)}")
    print(f"Total unique achievements: {achivement}")
    print(f"Average score: {Average_score}")
    print(f"Top performer: ")


def main():
    list_player = [
       {'name': 'alice',   'score': 2300, 'region': 'north', 'active': True},
       {'name': 'bob',     'score': 1800, 'region': 'east', 'active': True},
       {'name': 'charlie', 'score': 2150, 'region': 'central', 'active': True},
       {'name': 'diana',   'score': 2050, 'region': 'north', 'active': False}
    ]

    list_achivement = {
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

    print("=== Game Analytics Dashboard ===")
    List_Comprehension_Examples(list_player)
    print("\n=== Dict Comprehension Examples ===")
    Dict_Comprehension_Examples(list_player, list_achivement)
    print("\n=== Combined Analysis ===")
    Combined_Analysis(list_player, list_achivement)


if __name__ == "__main__":
    main()
