#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

import issgame


class TestLoadSessions(unittest.TestCase):
    def test_loads_expected(self):
        input_filename = 'issgame/tests/data/test_converted_games_known_zoot_known.csv'
        player = 'zoot'
        # zoot,2021-04-30-blkkjk-theCount-zoot,7.0,8.0,7.0,9.0,10.0,9.0,8.0,8.0,5.0,6.0
        # zoot,2017-02-27-@9WScnU3-theCount-zoot,4.0
        expected_dict = {'zoot': {
            '2021-04-30-blkkjk-theCount-zoot': [7.0, 8.0, 7.0, 9.0, 10.0, 9.0, 8.0, 8.0, 5.0, 6.0],
            '2017-02-27-@9WScnU3-theCount-zoot': [4.0]}
        }
        out_dict = issgame.load_sessions(input_filename, player)
        self.assertDictEqual(expected_dict, out_dict)


if __name__ == "__main__":
    unittest.main()
