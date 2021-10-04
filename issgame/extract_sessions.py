#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas
import issgame


def extract_sessions(filename, player_name):
    player_hands = {}

    games = pandas.read_csv(filename, sep='\t')
    # TODO: should not be calculated here and in load_hands
    games.loc[:, 'score'] =\
        [issgame.get_score(hand) for hand in games.loc[:, 'hand']]

    for __i, line in games.iterrows():
        if player_name == line.loc['player']:
            session = line.loc['session']
            player = line.loc['player']
            score = line.loc['score']

            if session not in player_hands.keys():
                player_hands[session] = []
            player_hands[session].append(score)

    out_lines = []
    for session in player_hands.keys():
        out_string = player + ',' + session
        for score in player_hands[session]:
            out_string += ',' + str(score)
        out_string += '\n'
        out_lines.append(out_string)

    with open(filename[:-4] + '_' + player_name + '.csv', 'w') as out_file:
        out_file.writelines(out_lines)
