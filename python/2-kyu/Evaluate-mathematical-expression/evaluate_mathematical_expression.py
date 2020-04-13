import operator


operators = {
    'negate': {
        'precedence': 3,
        'associative': 'right',
        'func': lambda x: x * -1
    },
    '*': {
        'precedence': 2,
        'associative': 'left',
        'func': operator.mul
    },
    '/': {
        'precedence': 2,
        'associative': 'left',
        'func': operator.truediv
    },
    '+': {
        'precedence': 1,
        'associative': 'left',
        'func': operator.add
    },
    '-': {
        'precedence': 1,
        'associative': 'left',
        'func': operator.sub
    }
}

def parse(string):
    string = string.replace(' ', '')
    expression = []
    number = ''
    for index, token in enumerate(string):
        if token in '1234567890.':
            number += token
        elif number:
            expression.append(float(number))
            number = ''
        if token in operators or token in '()':
            if token == '-':
                if index == 0:
                    expression.append('negate')
                else:
                    prev_token = string[index-1]
                    next_token = string[index+1]
                    if ((prev_token in operators or prev_token == '(') and
                            (next_token in '-(' or next_token in '1234567890.')):
                        expression.append('negate')
                    else:
                        expression.append(token)
            else:
                expression.append(token)
    if number:
        expression.append(float(number))
    
    return expression

def get_reverse_polish_notation(expression):
    expression = parse(expression)
    reverse_polish_notation = []
    operator_stack = []
    for token in expression:
        if token in operators:
            while (operator_stack and operator_stack and operator_stack[-1] != '(' and
                       (operators[operator_stack[-1]]['precedence'] > operators[token]['precedence'] or
                        (operators[operator_stack[-1]]['precedence'] == operators[token]['precedence'] and
                         operators[token]['associative'] == 'left'))):
                reverse_polish_notation.append(operator_stack.pop())
            operator_stack.append(token)
        elif  token == '(':
            operator_stack.append('(')
        elif token == ')':
            while operator_stack[-1] != '(':
                reverse_polish_notation.append(operator_stack.pop())
            if operator_stack[-1] == '(':
                operator_stack.pop()
        else:
            reverse_polish_notation.append(token)
    if operator_stack:
        reverse_polish_notation.extend(reversed(operator_stack))
    return reverse_polish_notation

def calc(expression):
    reverse_polish_notation = get_reverse_polish_notation(expression)
    pending = []
    for token in reverse_polish_notation:
        if token in operators:
            if token == 'negate':
                x = pending.pop()
                pending.append(operators[token]['func'](x))
            else:
                y, x = pending.pop(), pending.pop()
                pending.append(operators[token]['func'](x, y))
        else:
            pending.append(token)
    return pending[0]
