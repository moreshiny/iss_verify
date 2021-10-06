#!/usr/bin/env python3

from typing import Dict, List

import pandas


def hand_score(hand: str) -> float:
    '''
    Calculates a score for the provided hand indicating the value of the hand
    for winning a skat game.

    Args:
        hand (str): Represents a hand of 10 cards represented as two characters
        as returned by GameLine._read_hand()

    Returns:
        float: A score according to Stegen Model for bidding in skat games:
        https://www.skatfuchs.eu/SB-Kapitel3.pdf
    '''

    assert type(hand) is str, 'Hand should be a string'
    assert len(hand) == 29, 'Lenght of hand should be 10 cards'

    for suit in range(0, 27, 3):
        assert hand[suit] in 'HCSD', 'Incorrect hand format'
        assert hand[suit+1] in 'AKQJT987', 'Incorrect hand format'
        assert hand[suit+2] == '_', 'Incorrect hand format'

    score = 0.0
    suitscores = {}
    suitcount = {'C': 0, 'S': 0, 'H': 0, 'D': 0, 'J': 0, 'T': 0, 'A': 0}
    suits_not_found = 0

    for card in hand.split('_'):
        # quantity of each suit except jacks
        if not card[1] == 'J':
            try:
                suitcount[card[0]] += 1
            except KeyError:
                suitcount[card[0]] = 1

        # quantity of jacks, aces, and tens
        if card[1] in 'JAT':
            try:
                suitcount[card[1]] += 1
            except KeyError:
                suitcount[card[1]] = 1

    # the score for each suit
    for suit in ['C', 'S', 'H', 'D']:
        suitscores[suit] = 0.0
        suitscores[suit] += suitcount[suit]\
                         + 2*suitcount['J']\
                         + suitcount['A']\
                         + suitcount['T']
        if suitcount[suit] == 0:
            suits_not_found += 1

    # the highest scoring suit score
    score += max(suitscores.values())

    # additional score factor for jack combinations
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

    # additional score factor for missing suits
    score += suits_not_found/2

    # alternative score for a grand game
    grand_score = (5/3)*(suitcount['J'] + suitcount['A'] + suitcount['T'])

    return round(max([score, grand_score]), 3)


class GameLine():
    """
    A data processing class that makes the elements of a .svg line available
    through function calls.
    """

    def __init__(self, line: str):
        """
        Initiates a GameLine class by extracting the following from the
        provided .svg 'line':
        _date: str Session date
        _id: str Session ID
        _player1: str Name of player 1
        _player2: str Name of player 2
        _player3: str Name of player 3
        _hands: Dict[int, str] Maps players to hands

        Args:
            line (str): A .svg file line.
        """
        self._date = line.split(']DT[')[1].split('/')[0]
        self._id = line.split(']ID[')[1].split(']')[0] + '_' + \
            line.split(']DT[')[1].split(']')[0]

        self._player1 = self._read_player(line, 1)
        self._player2 = self._read_player(line, 2)
        self._player3 = self._read_player(line, 3)

        self._hands = {}
        self._hands[1] = self._read_hand(line, 1)
        self._hands[2] = self._read_hand(line, 2)
        self._hands[3] = self._read_hand(line, 3)
        self._hands[4] = self._read_hand(line, 4)

    def _read_hand(self, line: str, player: int) -> str:
        '''Extracts and returns the hand belonging to player a string from a line.

        Args:
            line (str): a .svg skat game line
            player (int): The player (1, 2, 3 or 4 for skat)

        Returns:
            str: Represents a hand of 10 cards represented as two characters
            separated by underscores:

            'HQ_HA_H7_CT_ST_SK_SA_HJ_CJ_CK'

            The first character indicates the suit of each card:
                H is Hearts, C is Clubs, S is Spades, D is Diamonds
            The second character indicates the value of each card:
                A is Ace, K is King, Q is Qeen, J is Jack, T is 10, 9..7 are 9 to 7.
        '''
        # player 4 is the skat
        if player == 4:
            length = 2
        else:
            length = 10
        start = (2+(player-1)*30)
        end = start + length*3-1
        return '_'.join(line.split(']MV[')[1][start:end].split('.'))

    def _read_player(self, line: str, player: int) -> str:
        '''
        Extracts and returns the name of the player given by 'player'.

        Args:
            line (str): .svg game line
            player (int): Player number (1-3 or 4 for skat)

        Returns:
            str: A player name
        '''
        return line.split(']P' + str(player-1) + '[')[1].split(']')[0]

    def get_player(self, player: int) -> str:
        '''Returns the name of player 'player' (1-3, not skat) as a string'''
        if player == 1:
            return self.get_player1()
        if player == 2:
            return self.get_player2()
        if player == 3:
            return self.get_player3()

    def get_player1(self) -> str:
        '''Returns the name of player 1 as a string'''
        return self._player1

    def get_player2(self) -> str:
        '''Returns the name of player 2 as a string'''
        return self._player2

    def get_player3(self) -> str:
        '''Returns the name of player 3 as a string'''
        return self._player3

    def get_hand(self, player: int) -> str:
        '''Returns the hand of to player a string from a line.'''
        try:
            return self._hands[player]
        except KeyError:
            self._hands[player] = self._read_hand(player)
            return self._hands[player]

    def get_hand1(self) -> str:
        '''Returns the hand of player 1'''
        return self._hands[1]

    def get_hand2(self) -> str:
        '''Returns the hand of player 1'''
        return self._hands[2]

    def get_hand3(self) -> str:
        '''Returns the hand of player 1'''
        return self._hands[3]

    def get_skat(self) -> str:
        '''Returns the skat as a two-card hand'''
        return self._hands[4]

    def get_all(self) -> str:
        '''Returns all hands and the skat'''
        return self.get_hand1()\
            + self.get_hand2()\
            + self.get_hand3()\
            + self.get_skat()

    def get_date(self) -> str:
        '''Returns the session date as a string'''
        return self._date

    def get_id(self) -> str:
        '''Returns the session id'''
        return self._id

    def get_score(self, player: int) -> str:
        '''Returns the score of the hand of player as calculated by hand_score()'''
        hand = self.get_hand(player)
        return hand_score(hand)

    def get_session(self) -> str:
        '''Returns a string representation of the session information'''
        file_string = self.get_date()
        for player in sorted([self.get_player1(), self.get_player2(), self.get_player3()]):
            file_string += '-' + player
        return file_string

    def get_hands(self) -> pandas.DataFrame:
        '''
        Provides a pandas DataFrame containing the main information for each
        player.

        Returns:
            pandas.DataFrame: Main information for each player.
        '''
        return_dict = {
            'id': [],
            'session': [],
            'player': [],
            'position': [],
            'hand': []
        }

        for playerpos in range(1, 4):
            return_dict['id'].append(self.get_id())
            return_dict['session'].append(self.get_session())
            return_dict['player'].append(self.get_player(playerpos))
            return_dict['position'].append(playerpos)
            return_dict['hand'].append(self.get_hand(playerpos))

        return pandas.DataFrame(return_dict)
