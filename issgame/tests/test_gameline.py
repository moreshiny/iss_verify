#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import os

import issgame


class TestGameLine(unittest.TestCase):
    def test_load_line_1_hand_1(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        test_game = issgame.GameLine(line)
        test_string = 'HQ_HA_H7_CT_ST_SK_SA_HJ_CJ_CK'
        self.assertEqual(test_game.get_hand1(), test_string)

    def test_load_line_1_hand_2(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        test_game = issgame.GameLine(line)
        test_string = 'C8_DQ_S9_SQ_D9_C7_HK_DT_HT_CA'
        self.assertEqual(test_game.get_hand2(), test_string)

    def test_load_line_1_hand_3(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        test_game = issgame.GameLine(line)
        test_string = 'CQ_D7_DK_H9_SJ_DJ_H8_S7_D8_S8'
        self.assertEqual(test_game.get_hand3(), test_string)

    def test_load_line_1_skat(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        test_game = issgame.GameLine(line)
        test_string = 'DA_C9'
        self.assertEqual(test_game.get_skat(), test_string)

    def test_load_line_1_id(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        test_game = issgame.GameLine(line)
        test_string = '6997010' + "_2021-04-30/01:07:29/UTC"
        self.assertEqual(test_game.get_id(), test_string)

    def test_load_line_2_hand_1(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        line = games.readline()
        test_game = issgame.GameLine(line)
        test_string = 'ST_D9_SQ_CQ_S9_DA_C8_SJ_CK_HK'
        self.assertEqual(test_game.get_hand1(), test_string)

    def test_load_line_2_hand_2(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        line = games.readline()
        test_game = issgame.GameLine(line)
        test_string = 'D8_CJ_S8_H9_DT_C7_HQ_H8_HT_D7'
        self.assertEqual(test_game.get_hand2(), test_string)

    def test_load_line_2_hand_3(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        line = games.readline()
        test_game = issgame.GameLine(line)
        test_string = 'HA_DK_S7_DJ_H7_HJ_CA_SA_C9_CT'
        self.assertEqual(test_game.get_hand3(), test_string)

    def test_load_line_2_skat(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        line = games.readline()
        test_game = issgame.GameLine(line)
        test_string = 'DQ_SK'
        self.assertEqual(test_game.get_skat(), test_string)

    def test_load_line_2_id(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        line = games.readline()
        test_game = issgame.GameLine(line)
        test_string = '6997011' + "_2021-04-30/01:12:24/UTC"
        self.assertEqual(test_game.get_id(), test_string)

    def test_load_file2_line_4_id(self):
        games = open('issgame/tests/data/test_games2.sgf')
        for __i in range(4):
            line = games.readline()
        test_game = issgame.GameLine(line)
        test_string = '110012' + "_2016-08-24/18:14:31/UTC"
        self.assertEqual(test_game.get_id(), test_string)

    def test_cards_are_strings_length_2(self):
        games = open('issgame/tests/data/test_games.sgf')
        for line in games:
            test_game = issgame.GameLine(line)
            for card in test_game.get_hand1().split('_'):
                self.assertEqual(type(card), type(''))
                self.assertEqual(len(card), 2)
            for card in test_game.get_hand2().split('_'):
                self.assertEqual(type(card), type(''))
                self.assertEqual(len(card), 2)
            for card in test_game.get_hand3().split('_'):
                self.assertEqual(type(card), type(''))
                self.assertEqual(len(card), 2)
            for card in test_game.get_skat().split('_'):
                self.assertEqual(type(card), type(''))
                self.assertEqual(len(card), 2)

    def test_get_first_player(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        test_game = issgame.GameLine(line)
        test_string = 'theCount'
        self.assertEqual(test_game.get_player1(), test_string)

    def test_get_second_player(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        test_game = issgame.GameLine(line)
        test_string = 'blkkjk'
        self.assertEqual(test_game.get_player2(), test_string)

    def test_get_third_player(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        test_game = issgame.GameLine(line)
        test_string = 'zoot'
        self.assertEqual(test_game.get_player3(), test_string)

    def test_get_day_of_game(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        test_game = issgame.GameLine(line)
        test_string = '2021-04-30'
        self.assertEqual(test_game.get_date(), test_string)

    def test_score_line_1_hand_1(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        test_game = issgame.GameLine(line)
        # test_string = ['CJ'_'CK'_'CT'_'H7'_'HA',
        #                'HJ'_'HQ'_'SA'_'SK'_'ST']
        # 5 trumps (hearts and jacks_2 jacks_ace of hearts_ten of clubs
        # and ace and ten of spades_no diamonds) OR grand 2 jacks 2 aces and 2 tens
        # test_score = 5 + 2 + 1 + 3 + 0.5 = 11.5 OR (2 + 4) / 3 * 5 = 10
        test_score = 11.5
        self.assertEqual(test_game.get_score(1), test_score)

    def test_score_line_2_hand_1(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        line = games.readline()
        test_game = issgame.GameLine(line)
        # test_string = ['C8'_'CK'_'CQ'_'D9'_'DA',
        #                'HK'_'S9'_'SJ'_'SQ'_'ST']
        # 4 trumps (spades and a jack_1 jack_10 of spades and ace of diamonds)
        # OR grand 1 jack 1 ten
        # test_score = 4 + 1 + 2 = 7 OR (1 + 1)/3 * 5 = 3.33
        test_score = 7.0
        self.assertEqual(test_game.get_score(1), test_score)

    def test_score_line_1_hand_2(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        test_game = issgame.GameLine(line)
        # test_string = ['C7'_'C8'_'CA'_'D9'_'DQ',
        #                'DT'_'HK'_'HT'_'S9'_'SQ']
        # 3 trumps (clubs_no jcks_ace of clubs_ten of hearts and diamonds,
        # all suits present) OR grand no jacks 1 ace 2 tens
        # test_score = 3 + 0 + 1 + 2 = 6 OR grand 0 + 3 = 3 / 3 * 5 = 5
        test_score = 6.0
        self.assertEqual(test_game.get_score(2), test_score)

    def test_score_line_1_hand_3(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        test_game = issgame.GameLine(line)
        # test_string = ['CQ'_'D7'_'D8'_'DJ'_'DK',
        #                'H8'_'H9'_'S7'_'S8'_'SJ']
        # 5 trumps diamonds and jacks_2 jacks_no aces or tens_no missing suit
        # OR grand 2 jacks_no 10s or aces
        # test_score = 5 + 2 = 7  OR 2 / 3 * 5 = 3.33
        test_score = 7.0
        self.assertEqual(test_game.get_score(3), test_score)

    def test_score_line_7_hand_1(self):
        games = open('issgame/tests/data/test_games.sgf')
        for __i in range(7):
            line = games.readline()

        test_game = issgame.GameLine(line)
        # test_string = ['CT'_'DJ'_'H7'_'H8'_'HA',
        #                'HJ'_'HT'_'S7'_'S9'_'SJ']
        # 7 trumps (hearts and jacks_3 jacks_ace and ten of hearts_10 of clubs,
        # lower 3 jacks_diamonds missing suits) OR grand 3 jacks_ace and 10 of hearts
        # and 10 of clubs
        # test_score = 7 + 3 + 2 + 1 + 0.5 + 0.5 = 14 OR grand 3 + 3 = 6 / 3 * 5 = 10
        test_score = 14.0
        self.assertEqual(test_game.get_score(1), test_score)

    def test_score_line_15_hand_1(self):
        games = open('issgame/tests/data/test_games2.sgf')
        for __i in range(7):
            line = games.readline()

        test_game = issgame.GameLine(line)
        # test_string = ['C8'_'CJ'_'CT'_'D8'_'DA',
        #                'HA'_'HJ'_'HT'_'SA'_'ST']
        # 4 trumps (hearts and jacks_2 jacks_ace and ten of hearts_ace and ten of spades
        # and ten of clubs and ace of diamonds_no missing suits
        # OR grand 2 jacks 3 aces and 3 tens
        # test_score = 4 + 2 + 2 + 4 = 12 OR grand 2 + 6 = 8 / 3 * 5 = 13.33
        test_score = 13.333
        self.assertAlmostEqual(test_game.get_score(1), test_score)

    def test_hand_as_list_raises_assert_error(self):
        test_hand = ['C8', 'CJ', 'CT', 'D8',
                     'DA', 'HA', 'HJ', 'HT', 'SA', 'ST']
        self.assertRaises(AssertionError, issgame.hand_score, test_hand)

    def test_hand_too_short_raises_assert_error(self):
        test_hand = 'HA_DK_S7_DJ_H7'
        self.assertRaises(AssertionError, issgame.hand_score, test_hand)

    def test_hand_too_long_raises_assert_error(self):
        test_hand = 'HA_DK_S7_DJ_H7_HJ_CA_SA_C9_CT_S7'
        self.assertRaises(AssertionError, issgame.hand_score, test_hand)

    def test_hand_wrong_separator_raises_assert_error(self):
        test_hand = 'HA DK S7 DJ H7 HJ CA SA C9 CT'
        self.assertRaises(AssertionError, issgame.hand_score, test_hand)

    def test_hand_invalid_suit_raises_assert_error(self):
        test_hand = 'HA_KK_S7_DJ_H7_HJ_CA_SA_C9_CT'
        self.assertRaises(AssertionError, issgame.hand_score, test_hand)

    def test_hand_invalid_value_raises_assert_error(self):
        test_hand = 'HA_DD_S7_DJ_H7_HJ_CA_SA_C9_CT'
        self.assertRaises(AssertionError, issgame.hand_score, test_hand)

if __name__ == "__main__":
    unittest.main()
