#!/usr/bin/env python3

class GameLine():
    def __init__(self, line):
        self._line = line

    def _read_hand(self, player):
        # player 4 is the skat
        if player == 4:
            length = 2
        else:
            length = 10
        start = (2+(player-1)*30)
        end = start + length*3-1
        return sorted(self._line.split(']MV[')[1][start:end].split('.'))

    def _read_player(self, player):
        return self._line.split(']P' + str(player-1) + '[')[1].split(']')[0]

    def get_player1(self):
        return self._read_player(1)

    def get_player2(self):
        return self._read_player(2)

    def get_player3(self):
        return self._read_player(3)

    def get_hand(self, player_name):
        for i in range(1, 4):
            if self._read_player(i) == player_name:
                return self._read_hand(i)

    def get_hand1(self):
        return self._read_hand(1)

    def get_hand2(self):
        return self._read_hand(2)

    def get_hand3(self):
        return self._read_hand(3)

    def get_skat(self):
        return self._read_hand(4)

    def get_all(self):
        return self.get_hand1() + self.get_hand2() + self.get_hand3() + self.get_skat()

    def get_date(self):
        return self._line.split(']DT[')[1].split('/')[0]

    def get_id(self):
        return self._line.split(']ID[')[1].split(']')[0] + "_" + \
            self._line.split(']DT[')[1].split(']')[0]

    def _getGrandScore(self, player):
        score = 0.0

        for card in self._read_hand(player):
            if card[1] == 'J' or card[1] == 'A' or card[1] == 'T':
                score += 1

        return score/3*5

    def getScore(self, player):
        score = 0.0
        suitscores = {}
        suits_found = []

        for suit in ['C', 'S', 'H', 'D']:
            suitscores[suit] = 0.0
            for card in self._read_hand(player):
                if card[1] != 'J' and card[0] not in suits_found:
                    suits_found.append(card[0])
                if card[0] == suit or card[1] == 'J':
                    suitscores[suit] += 1
                if card[1] == 'J':
                    suitscores[suit] += 1
                if card[1] == 'A' or card[1] == 'T':
                    suitscores[suit] += 1

        score += max(suitscores.values())

        hand = self._read_hand(player)

        if 'CJ' in hand and 'SJ' in hand and 'HJ' in hand and 'DJ' in hand:
            score += 2
        elif 'SJ' in hand and 'HJ' in hand and 'DJ' in hand:
            score += 0.5
        elif 'CJ' in hand and 'SJ' in hand and 'HJ' in hand:
            score += 1.5
        elif 'CJ' in hand and 'SJ' in hand:
            score += 0.5

        score += 2 - len(suits_found)/2

        return max([score, self._getGrandScore(player)])

    def getSession(self):
        file_string = self.get_date()
        for player in sorted([self.get_player1(), self.get_player2(), self.get_player3()]):
            file_string += '-' + player
        return file_string

    def saveScore(self, filename, playerpos, append=True):

        file_string = ''

        file_string += self.get_id() + ','
        file_string += self.getSession()
        file_string = file_string + ',' + self._read_player(playerpos) + ',' + str(
            playerpos) + ',' + str(self.getScore(playerpos)) + "\n"

        if append == False:
            with open(filename, 'w') as the_file:
                the_file.write(file_string)
        else:
            with open(filename, 'a') as the_file:
                the_file.write(file_string)

    def saveScoreAllHands(self, filename, append=True):
        for i in range(1, 4):
            self.saveScore(filename, i, append)

    def __str__(self):
        return str(self.get_hand1()) + str(self.get_hand2()) + \
            str(self.get_hand3()) + str(self.get_skat())
