def battle(player1, player2):
    min_deck = len(min([player1, player2], key=len))

    return {
        'player1': [creature for i, creature in enumerate(player1)
                    if i+1 > min_deck or creature[1] > player2[i][0]],
        'player2': [creature for i, creature in enumerate(player2)
                    if i+1 > min_deck or creature[1] > player1[i][0]],
    }
