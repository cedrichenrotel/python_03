#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_analytics_dashboard.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/05 14:22:31 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/07 11:19:42 by cehenrot        ###   ########.fr        #
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

    Achievement_counts = {p: len(n_ach) for p, n_ach in lst_achivement.items()}

    print(f"Player scores: {Player_scores}")
    print(f"Score categories: {categories}")
    print(f"Achievement counts: {Achievement_counts}")


def Set_Comprehension_Examples(player: list, lst_achivement: dict) -> None:

    Unique_players = set(p["name"] for p in player)

    Achievement = set(ach for player in lst_achivement
                      for ach in lst_achivement[player])

    regions = set(p['region'] for p in player)

    print(f"Unique players: {Unique_players}")
    print(f"Unique achievement: {Achievement}")
    print(f"Active regions: {regions}")


def Combined_Analysis(player: list, lst_achivement: dict) -> None:

    achivement = len({ach for player in lst_achivement
                     for ach in lst_achivement[player]})

    Average_score = (sum(p['score'] for p in player) / len(player))

    player_sc = [(p['score'], p['name']) for p in player]
    score, name = sorted(player_sc, reverse=True)[0]
    nb_ach = len(lst_achivement.get(name, []))

    print(f"Total players: {len(player)}")
    print(f"Total unique achievements: {achivement}")
    print(f"Average score: {Average_score}")
    print(f"Top performer: {name} ({score} points, {nb_ach} achievements)")


def main():
    list_player = [
       {'name': 'Alice',   'score': 2300, 'region': 'north', 'active': True},
       {'name': 'Bob',     'score': 1800, 'region': 'east', 'active': True},
       {'name': 'Charlie', 'score': 2150, 'region': 'central', 'active': True},
       {'name': 'Diana',   'score': 2050, 'region': 'north', 'active': False}
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
    print("\n=== Set Comprehension Examples ===")
    Set_Comprehension_Examples(list_player, list_achivement)
    print("\n=== Combined Analysis ===")
    Combined_Analysis(list_player, list_achivement)


if __name__ == "__main__":
    main()
