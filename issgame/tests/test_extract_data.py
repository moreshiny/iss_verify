#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import os

import issgame


class TestExtractData(unittest.TestCase):
    def test_creates_the_expected_cvs_output_file(self):
        raw_data = ['issgame/tests/data/test_games.sgf']
        converted_data = 'issgame/tests/data/test_converted_games.tsv'
        if os.path.isfile(converted_data):
            os.remove(converted_data)
        issgame.extract_svg_hands(raw_data, converted_data)
        self.assertTrue(os.path.isfile(converted_data))

    def test_output_file_contains_expected_number_of_fields(self):
        raw_data = ['issgame/tests/data/test_games.sgf']
        converted_data = 'issgame/tests/data/test_converted_games.tsv'
        if os.path.isfile(converted_data):
            os.remove(converted_data)
        issgame.extract_svg_hands(raw_data, converted_data)
        with open(converted_data) as data_file:
            fields = data_file.readline().split('\t')
        self.assertEqual(len(fields), 5)

    def test_output_file_contains_3_lines_per_game(self):
        raw_data = ['issgame/tests/data/test_games.sgf']
        converted_data = 'issgame/tests/data/test_converted_games.tsv'
        if os.path.isfile(converted_data):
            os.remove(converted_data)
        issgame.extract_svg_hands(raw_data, converted_data)
        expected_len = 1
        for data_file in raw_data:
            expected_len += 3*(len(list(open(data_file))))
        self.assertEqual(len(list(open(converted_data))), expected_len)

    def test_output_file_contains_3_lines_per_game_2_files(self):
        raw_data = ['issgame/tests/data/test_games.sgf',
                    'issgame/tests/data/test_games2.sgf']
        converted_data = 'issgame/tests/data/test_converted_games.tsv'
        if os.path.isfile(converted_data):
            os.remove(converted_data)
        issgame.extract_svg_hands(raw_data, converted_data)
        expected_len = 1
        for data_file in raw_data:
            expected_len += 3*(len(list(open(data_file))))
        self.assertEqual(len(list(open(converted_data))), expected_len)

    def test_output_file_line_1_contains_expected_fields(self):
        raw_data = ['issgame/tests/data/test_games.sgf',
                    'issgame/tests/data/test_games2.sgf']
        converted_data = 'issgame/tests/data/test_converted_games.tsv'
        known_good_data = 'issgame/tests/data/test_converted_games_known.tsv'
        if os.path.isfile(converted_data):
            os.remove(converted_data)
        issgame.extract_svg_hands(raw_data, converted_data)
        self.assertListEqual(list(open(converted_data)),
                             list(open(known_good_data)))


if __name__ == "__main__":
    unittest.main()
