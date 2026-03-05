#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_analytics_dashboard.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/05 14:22:31 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/05 19:09:18 by cehenrot        ###   ########.fr        #
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
    
    print(f"Player scores: {Player_scores}")
    print(f"Score categories: {categories}")
    print(f"Unique achievements: {Achievement}")


def main():
    list_player = [
       {'name': 'alice',   'score': 2300, 'active': True},
       {'name': 'bob',     'score': 1800, 'active': True},
       {'name': 'charlie', 'score': 2150, 'active': True},
       {'name': 'diana',   'score': 2050, 'active': False}
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


if __name__ == "__main__":
    main()
