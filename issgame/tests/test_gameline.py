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
        test_string = ['CJ', 'CK', 'CT', 'H7', 'HA',
                       'HJ', 'HQ', 'SA', 'SK', 'ST']
        self.assertEqual(test_game.get_hand1(), test_string)

    def test_load_line_1_hand_2(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        test_game = issgame.GameLine(line)
        test_string = ['C7', 'C8', 'CA', 'D9', 'DQ',
                       'DT', 'HK', 'HT', 'S9', 'SQ']
        self.assertEqual(test_game.get_hand2(), test_string)

    def test_load_line_1_hand_3(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        test_game = issgame.GameLine(line)
        test_string = ['CQ', 'D7', 'D8', 'DJ', 'DK',
                       'H8', 'H9', 'S7', 'S8', 'SJ']
        self.assertEqual(test_game.get_hand3(), test_string)

    def test_load_line_1_skat(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        test_game = issgame.GameLine(line)
        test_string = ['C9', 'DA']
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
        test_string = ['C8', 'CK', 'CQ', 'D9', 'DA',
                       'HK', 'S9', 'SJ', 'SQ', 'ST']
        self.assertEqual(test_game.get_hand1(), test_string)

    def test_load_line_2_hand_2(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        line = games.readline()
        test_game = issgame.GameLine(line)
        test_string = ['C7', 'CJ', 'D7', 'D8', 'DT',
                       'H8', 'H9', 'HQ', 'HT', 'S8']
        self.assertEqual(test_game.get_hand2(), test_string)

    def test_load_line_2_hand_3(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        line = games.readline()
        test_game = issgame.GameLine(line)
        test_string = ['C9', 'CA', 'CT', 'DJ', 'DK',
                       'H7', 'HA', 'HJ', 'S7', 'SA']
        self.assertEqual(test_game.get_hand3(), test_string)

    def test_load_line_2_skat(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        line = games.readline()
        test_game = issgame.GameLine(line)
        test_string = ['DQ', 'SK']
        self.assertEqual(test_game.get_skat(), test_string)

    def test_load_line_2_id(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        line = games.readline()
        test_game = issgame.GameLine(line)
        test_string = '6997011' + "_2021-04-30/01:12:24/UTC"
        self.assertEqual(test_game.get_id(), test_string)

    def test_load_line_12_id(self):
        games = open('issgame/tests/data/test_games.sgf')
        for __i in range(12):
            line = games.readline()
        test_game = issgame.GameLine(line)
        test_string = '110012' + "_2016-08-24/18:14:31/UTC"
        self.assertEqual(test_game.get_id(), test_string)

    def test_cards_are_strings_length_2(self):
        games = open('issgame/tests/data/test_games.sgf')
        for line in games:
            test_game = issgame.GameLine(line)
            for card in test_game.get_hand1():
                self.assertEqual(type(card), type(''))
                self.assertEqual(len(card), 2)
            for card in test_game.get_hand2():
                self.assertEqual(type(card), type(''))
                self.assertEqual(len(card), 2)
            for card in test_game.get_hand3():
                self.assertEqual(type(card), type(''))
                self.assertEqual(len(card), 2)
            for card in test_game.get_skat():
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

    def test_get_hand_by_player(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        test_game = issgame.GameLine(line)
        test_name = 'zoot'
        test_string = ['CQ', 'D7', 'D8', 'DJ',
                       'DK', 'H8', 'H9', 'S7', 'S8', 'SJ']
        self.assertEqual(test_game.get_hand(test_name), test_string)

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
        # test_string = ['CJ', 'CK', 'CT', 'H7', 'HA',
        #                'HJ', 'HQ', 'SA', 'SK', 'ST']
        # 5 trumps (hearts and jacks, 2 jacks, ace of hearts, ten of clubs
        # and ace and ten of spades, no diamonds) OR grand 2 jacks 2 aces and 2 tens
        # test_score = 5 + 2 + 1 + 3 + 0.5 = 11.5 OR (2 + 4) / 3 * 5 = 10
        test_score = 11.5
        self.assertEqual(test_game.getScore(1), test_score)

    def test_score_line_2_hand_1(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        line = games.readline()
        test_game = issgame.GameLine(line)
        # test_string = ['C8', 'CK', 'CQ', 'D9', 'DA',
        #                'HK', 'S9', 'SJ', 'SQ', 'ST']
        # 4 trumps (spades and a jack, 1 jack, 10 of spades and ace of diamonds)
        # OR grand 1 jack 1 ten
        # test_score = 4 + 1 + 2 = 7 OR (1 + 1)/3 * 5 = 3.33
        test_score = 7.0
        self.assertEqual(test_game.getScore(1), test_score)

    def test_score_line_1_hand_2(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        test_game = issgame.GameLine(line)
        # test_string = ['C7', 'C8', 'CA', 'D9', 'DQ',
        #                'DT', 'HK', 'HT', 'S9', 'SQ']
        # 3 trumps (clubs, no jcks, ace of clubs, ten of hearts and diamonds,
        # all suits present) OR grand no jacks 1 ace 2 tens
        # test_score = 3 + 0 + 1 + 2 = 6 OR grand 0 + 3 = 3 / 3 * 5 = 5
        test_score = 6.0
        self.assertEqual(test_game.getScore(2), test_score)

    def test_score_line_1_hand_3(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        test_game = issgame.GameLine(line)
        # test_string = ['CQ', 'D7', 'D8', 'DJ', 'DK',
        #                'H8', 'H9', 'S7', 'S8', 'SJ']
        # 5 trumps diamonds and jacks, 2 jacks, no aces or tens, no missing suit
        # OR grand 2 jacks, no 10s or aces
        # test_score = 5 + 2 = 7  OR 2 / 3 * 5 = 3.33
        test_score = 7.0
        self.assertEqual(test_game.getScore(3), test_score)

    def test_score_line_7_hand_1(self):
        games = open('issgame/tests/data/test_games.sgf')
        for __i in range(7):
            line = games.readline()

        test_game = issgame.GameLine(line)
        # test_string = ['CT', 'DJ', 'H7', 'H8', 'HA',
        #                'HJ', 'HT', 'S7', 'S9', 'SJ']
        # 7 trumps (hearts and jacks, 3 jacks, ace and ten of hearts, 10 of clubs,
        # lower 3 jacks, diamonds missing suits) OR grand 3 jacks, ace and 10 of hearts
        # and 10 of clubs
        # test_score = 7 + 3 + 2 + 1 + 0.5 + 0.5 = 14 OR grand 3 + 3 = 6 / 3 * 5 = 10
        test_score = 14.0
        self.assertEqual(test_game.getScore(1), test_score)

    def test_score_line_15_hand_1(self):
        games = open('issgame/tests/data/test_games.sgf')
        for __i in range(15):
            line = games.readline()

        test_game = issgame.GameLine(line)
        # test_string = ['C8', 'CJ', 'CT', 'D8', 'DA',
        #                'HA', 'HJ', 'HT', 'SA', 'ST']
        # 4 trumps (hearts and jacks, 2 jacks, ace and ten of hearts, ace and ten of spades
        # and ten of clubs and ace of diamonds, no missing suits
        # OR grand 2 jacks 3 aces and 3 tens
        # test_score = 4 + 2 + 2 + 4 = 12 OR grand 2 + 6 = 8 / 3 * 5 = 13.33
        test_score = 8/3*5
        self.assertEqual(test_game.getScore(1), test_score)

    def test_save_score_line_1_hand_1(self):
        games = open('issgame/tests/data/test_games.sgf')
        line = games.readline()
        test_game = issgame.GameLine(line)
        test_game.saveScore("test_output1-1.csv", 1, append=False)
        outfile = open('test_output1-1.csv')
        test_line = \
            "6997010_2021-04-30/01:07:29/UTC,2021-04-30-blkkjk-theCount-zoot,theCount,1,11.5\n"
        lines = []
        for line in outfile:
            lines.append(line)

        os.remove('test_output1-1.csv')

        index = 0
        for line in lines:
            self.assertEqual(lines[index], test_line)
            index += 1

    def test_save_score_line_1_and_2_hand_1(self):
        with open('issgame/tests/data/test_games.sgf') as games:
            line = games.readline()
            test_game = issgame.GameLine(line)
            test_game.saveScore("test_output1-1.csv", 1, append=False)
            line = games.readline()
            test_game = issgame.GameLine(line)
            test_game.saveScore("test_output1-1.csv", 1, append=True)

        test_lines = [
            "6997010_2021-04-30/01:07:29/UTC,2021-04-30-blkkjk-theCount-zoot,theCount,1,11.5\n",
            "6997011_2021-04-30/01:12:24/UTC,2021-04-30-blkkjk-theCount-zoot,blkkjk,1,7.0\n"
        ]
        lines = []

        with open('test_output1-1.csv') as outfile:
            for line in outfile:
                lines.append(line)
        os.remove('test_output1-1.csv')

        self.assertEqual(len(lines), 2)
        index = 0
        for line in lines:
            self.assertEqual(lines[index], test_lines[index])
            index += 1


if __name__ == "__main__":
    unittest.main()
