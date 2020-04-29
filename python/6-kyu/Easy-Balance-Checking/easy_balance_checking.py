import re

def balance(book):
    pattern = r'[^\da-zA-Z.\n]'
    book = [x.split() for x in re.sub(pattern, ' ', book).splitlines() if x]
    original_balance = float(*book[0])
    remains = original_balance

    report = ''
    for line in book[1:]:
        remains -= float(line[-1])
        line[-1] = f'{float(line[-1]):.2f}'
        report += ' '.join(line) + f' Balance {remains:.2f}\r\n'

    total_expense = original_balance - remains
    average_expense = total_expense / len(book[1:])

    return (
        f'Original Balance: {original_balance:.2f}\r\n'
        f'{report}'
        f'Total expense  {total_expense:.2f}\r\n'
        f'Average expense  {average_expense:.2f}'
    )
