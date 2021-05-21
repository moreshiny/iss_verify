#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import issgame


def extract_data(raw_files, converted_file, testing=False):
    game_strings = []
    lines = []
    for raw_file in raw_files:
        with open(raw_file) as in_file:
            if testing == True:
                lines += in_file.readlines(2**21)
            else:
                lines += in_file.readlines()
    for line_index in range(len(lines)):
        game_strings += issgame.GameLine(
            lines[line_index]).get_all_file_strings()
        # if line_index % 100 == 0 and testing == True:
        #     print(line_index)
        if line_index > 5000 and testing == True:
            break

    with open(converted_file, 'w') as out_file:
        out_file.writelines(game_strings)
