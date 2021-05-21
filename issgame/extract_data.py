#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import issgame


def extract_data(raw_file, converted_file):
    with open(raw_file) as in_file:
        for line in in_file:
            game = issgame.GameLine(line)
            game.saveScoreAllHands(converted_file)
