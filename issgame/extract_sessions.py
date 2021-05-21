#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import issgame


def extract_sessions(filename, player_name):
    player_hands = {}
    games = open(filename)
    lines = games.readlines()

    for line in lines:
        if player_name in line.split(',')[2]:
            id_tag, session, player, position, score = line.split(',')
            position = int(position)
            score = float(score[:-1])

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
