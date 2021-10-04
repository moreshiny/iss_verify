#!/usr/bin/env python3

from typing import Dict, List

import pandas


def get_score(hand):
    score = 0.0
    suitscores = {}
    suitcount = {'C': 0, 'S': 0, 'H': 0, 'D': 0, 'J': 0, 'T': 0, 'A': 0}
    suits_not_found = 0

    for card in hand.split('_'):
        # record quantity of each suit except jacks
        if not card[1] == 'J':
            try:
                suitcount[card[0]] += 1
            except KeyError:
                suitcount[card[0]] = 1

        # record quantity of jacks, aces, and tens
        if card[1] in 'JAT':
            try:
                suitcount[card[1]] += 1
            except KeyError:
                suitcount[card[1]] = 1

    for suit in ['C', 'S', 'H', 'D']:
        suitscores[suit] = 0.0
        suitscores[suit] += suitcount[suit] + \
            2*suitcount['J'] + suitcount['A'] + suitcount['T']
        if suitcount[suit] == 0:
            suits_not_found += 1

    score += max(suitscores.values())

    if 'CJ' in hand and 'SJ' in hand:
        if 'HJ' in hand:
            if 'DJ' in hand:
                score += 2
            else:
                score += 1.5
        else:
            score += 0.5
    elif 'SJ' in hand and 'HJ' in hand and 'DJ' in hand:
        score += 0.5

    score += suits_not_found/2

    grand_score = (5/3)*(suitcount['J'] + suitcount['A'] + suitcount['T'])

    return round(max([score, grand_score]), 3)


class GameLine():
    def __init__(self, line):
        # self._line = line
        self._date = line.split(']DT[')[1].split('/')[0]
        self._id = line.split(']ID[')[1].split(']')[0] + "_" + \
            line.split(']DT[')[1].split(']')[0]

        self._player1 = self._read_player(line, 1)
        self._player2 = self._read_player(line, 2)
        self._player3 = self._read_player(line, 3)

        self._hands = {}
        self._hands[1] = self._read_hand(line, 1)
        self._hands[2] = self._read_hand(line, 2)
        self._hands[3] = self._read_hand(line, 3)
        self._hands[4] = self._read_hand(line, 4)

    def _read_hand(self, line, player):
        # player 4 is the skat
        if player == 4:
            length = 2
        else:
            length = 10
        start = (2+(player-1)*30)
        end = start + length*3-1
        return '_'.join(line.split(']MV[')[1][start:end].split('.'))

    def _read_player(self, line, player):
        return line.split(']P' + str(player-1) + '[')[1].split(']')[0]

    def get_player(self, player):
        if player == 1:
            return self.get_player1()
        if player == 2:
            return self.get_player2()
        if player == 3:
            return self.get_player3()

    def get_player1(self):
        return self._player1

    def get_player2(self):
        return self._player2

    def get_player3(self):
        return self._player3

    def get_hand(self, player):
        try:
            return self._hands[player]
        except KeyError:
            self._hands[player] = self._read_hand(player)
            return self._hands[player]

    def get_hand1(self):
        return self._hands[1]

    def get_hand2(self):
        return self._hands[2]

    def get_hand3(self):
        return self._hands[3]

    def get_skat(self):
        return self._hands[4]

    def get_all(self):
        return self.get_hand1() + self.get_hand2() + self.get_hand3() + self.get_skat()

    def get_date(self):
        return self._date

    def get_id(self):
        return self._id

    def get_score(self, player):
        hand = self.get_hand(player)
        return get_score(hand)

    def get_session(self):
        file_string = self.get_date()
        for player in sorted([self.get_player1(), self.get_player2(), self.get_player3()]):
            file_string += '-' + player
        return file_string

    def get_hands(self) -> pandas.DataFrame:
        """
        Provides a pandas DataFrame containing the main information for each
        player.

        Returns:
            pandas.DataFrame: Main information for each player.
        """
        return_dict = {'id': [], 'session': [],
                       'player': [], 'position': [], 'hand': []}

        for playerpos in range(1, 4):
            return_dict['id'].append(self.get_id())
            return_dict['session'].append(self.get_session())
            return_dict['player'].append(self.get_player(playerpos))
            return_dict['position'].append(playerpos)
            return_dict['hand'].append(self.get_hand(playerpos))

        return pandas.DataFrame(return_dict)

    def __str__(self):
        return str(self.get_hand1()) + str(self.get_hand2()) + \
            str(self.get_hand3()) + str(self.get_skat())
