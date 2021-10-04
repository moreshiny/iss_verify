#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

import issgame


class TestLoadHands(unittest.TestCase):
    def test_creates_the_expected_dict_pos_1(self):
        input_filename = 'issgame/tests/data/test_converted_games_known.tsv'
        player_position = 1
        expected_output = [11.5, 7.0, 7.0, 13.0, 7.0, 9.0, 14.0, 6.0,
                           5.0, 11.5, 10.0, 5.0, 6.0, 6.0, 13.333]

        result = issgame.load_hands(input_filename, player_position)
        self.assertListEqual(result, expected_output)

    def test_creates_the_expected_dict_pos_2(self):
        input_filename = 'issgame/tests/data/test_converted_games_known.tsv'
        player_position = 2
        expected_output = [6.0, 8.0, 10.5, 7.0, 10.0, 8.0, 4.0, 8.0,
                           13.0, 9.0, 9.5, 7.0, 7.0, 7.0, 8.0]

        result = issgame.load_hands(input_filename, player_position)
        self.assertListEqual(result, expected_output)

    def test_creates_the_expected_dict_pos_3(self):
        input_filename = 'issgame/tests/data/test_converted_games_known.tsv'
        player_position = 3
        expected_output = [7.0, 11.0, 10.0, 9.0, 8.0, 8.0, 8.0, 9.0,
                           10.0, 6.0, 7.0, 11.0, 10.5, 10.5, 4.0]

        result = issgame.load_hands(input_filename, player_position)
        self.assertListEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
