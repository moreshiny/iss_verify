#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas
import issgame


def load_hands(filename, player_pos):
    games = pandas.read_csv(filename, sep='\t')
    return_list = []
    for __i, line in games.iterrows():
        if line.loc['position'] == player_pos:
            # TODO: should not be calculated here and in extract_sessions
            return_list.append(float(issgame.hand_score(line.loc['hand'])))
    return return_list
