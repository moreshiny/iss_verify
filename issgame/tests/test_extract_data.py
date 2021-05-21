#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import os

import issgame


class TestExtractData(unittest.TestCase):
    def test_creates_the_expected_cvs_output_file(self):
        raw_data = 'issgame/tests/data/test_games.sgf'
        converted_data = 'issgame/tests/data/test_converted_games.csv'
        if os.path.isfile(converted_data):
            os.remove(converted_data)
        issgame.extract_data(raw_data, converted_data)
        self.assertTrue(os.path.isfile(converted_data))

    def test_output_file_contains_expected_number_of_fields(self):
        raw_data = 'issgame/tests/data/test_games.sgf'
        converted_data = 'issgame/tests/data/test_converted_games.csv'
        if os.path.isfile(converted_data):
            os.remove(converted_data)
        issgame.extract_data(raw_data, converted_data)
        with open(converted_data) as data_file:
            fields = data_file.readline().split(',')
        self.assertEqual(len(fields), 5)

    def test_output_file_contains_3_lines_per_game(self):
        raw_data = 'issgame/tests/data/test_games.sgf'
        converted_data = 'issgame/tests/data/test_converted_games.csv'
        if os.path.isfile(converted_data):
            os.remove(converted_data)
        issgame.extract_data(raw_data, converted_data)
        self.assertEqual(len(list(open(converted_data))),
                         3*len(list((open(raw_data)))))

        def test_output_file_line_1_contains_expected_fields(self):
            raw_data = 'issgame/tests/data/test_games.sgf'
            converted_data = 'issgame/tests/data/test_converted_games.csv'
            known_good_data = 'issgame/tests/data/test_converted_games_known.csv'
            if os.path.isfile(converted_data):
                os.remove(converted_data)
                issgame.extract_data(raw_data, converted_data)
                self.assertListEqual(list(open(converted_data)),
                                     list(open(known_good_data)))


if __name__ == "__main__":
    unittest.main()
