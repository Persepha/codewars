def rank(st, we, n):
    if not st:
        return 'No participants'

    names = st.split(',')
    if n > len(names):
        return 'Not enough participants'

    winning_numbers = [len(name) + sum(ord(letter)-96 for letter in name.lower()) for name in names]

    participants_data = zip(names, we, winning_numbers)
    participants = [(x[0], x[1] * x[2]) for x in participants_data]
    participants = sorted(participants, key=lambda x: (-x[1], x[0]))

    return participants[n-1][0]
