#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import os

import issgame


class TestExtractSessions(unittest.TestCase):
    def test_creates_expected_file(self):
        input_filename = 'issgame/tests/data/test_converted_games_known.csv'
        expected_file = 'issgame/tests/data/test_converted_games_known_zoot.csv'
        if os.path.exists(expected_file):
            os.remove(expected_file)
        issgame.extract_sessions(input_filename, 'zoot')
        self.assertTrue(os.path.isfile(expected_file))

    def test_writes_first_session_to_file(self):
        input_filename = 'issgame/tests/data/test_converted_games_known.csv'
        expected_file = 'issgame/tests/data/test_converted_games_known_zoot.csv'
        if os.path.exists(expected_file):
            os.remove(expected_file)
        issgame.extract_sessions(input_filename, 'zoot')
        expected_line = 'zoot,2021-04-30-blkkjk-theCount-zoot,7.0,8.0,7.0,9.0,10.0,9.0,8.0,8.0,5.0,6.0\n'

        self.assertEqual(open(expected_file).readline(), expected_line)


if __name__ == "__main__":
    unittest.main()
