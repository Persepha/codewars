def parse_bank_account(bank_account):
    digits = {
        ' _ | ||_|': '0',
        '     |  |': '1',
        ' _  _||_ ': '2',
        ' _  _| _|': '3',
        '   |_|  |': '4',
        ' _ |_  _|': '5',
        ' _ |_ |_|': '6',
        ' _   |  |': '7',
        ' _ |_||_|': '8',
        ' _ |_| _|': '9'
    }

    bank_account = bank_account.strip('\n').split('\n')
    return int(''.join(digits[''.join(x[i:i+3] for x in bank_account)] for i in range(0, len(bank_account[0]), 3)))
