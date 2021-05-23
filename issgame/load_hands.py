#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import issgame


def load_hands(filename, player_pos):
    with open(filename) as games_file:
        games = games_file.readlines()
    return_list = []
    for line in games:
        if int(line.split(',')[3]) == player_pos:
            return_list.append(float(line.split(',')[-1]))
    return return_list
