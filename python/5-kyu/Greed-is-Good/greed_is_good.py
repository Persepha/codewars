def score(dice):
    game_rules = {
        1: {
            "repetitions": 0,
            "triplePoints": 1000,
            "singlePoints": 100
        },
        2: {
            "repetitions": 0,
            "triplePoints": 200,
            "singlePoints": 0
        },
        3: {
            "repetitions": 0,
            "triplePoints": 300,
            "singlePoints": 0
        },
        4: {
            "repetitions": 0,
            "triplePoints": 400,
            "singlePoints": 0
        },
        5: {
            "repetitions": 0,
            "triplePoints": 500,
            "singlePoints": 50
        },
        6: {
            "repetitions": 0,
            "triplePoints": 600,
            "singlePoints": 0
        }
    }

    for die in dice:
        game_rules[die]["repetitions"]  += 1

    score = 0

    for key, value in game_rules.items():
        if value["repetitions"] > 3:
            score += value["triplePoints"]
            value["repetitions"] -= 3
            score += value["singlePoints"] * value["repetitions"]
        elif value["repetitions"] == 3:
            score += value["triplePoints"]
        else:
            score += value["singlePoints"] * value["repetitions"]
            
    return score
