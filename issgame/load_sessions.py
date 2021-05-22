def load_sessions(filename, player):
    all_hands = {}

    with open(filename) as games:
        for line in games:
            player, session = line.split(',')[:2]

            if player not in all_hands.keys():
                all_hands[player] = {}
            if session not in all_hands[player].keys():
                all_hands[player][session] = []

            for score in line.split(',')[2:]:
                all_hands[player][session].append(float(score))

    return all_hands
