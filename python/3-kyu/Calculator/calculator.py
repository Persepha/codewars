import operator


class Calculator(object):
    operators = {
        '*': (2, operator.mul),
        '/': (2, operator.truediv),
        '+': (1, operator.add),
        '-': (1, operator.sub)
    }

    def get_reverse_polish_notation(self, string):
        expression = [float(token) if token.isdigit() or '.' in token else token for token in string.split()]

        reverse_polish_notation = []
        operator_stack = []
        for token in expression:
            if token in self.operators:
                while (operator_stack and operator_stack[-1] != '(' and
                           self.operators[operator_stack[-1]][0] >= self.operators[token][0]):
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
            reverse_polish_notation.extend(operator_stack)

        return reverse_polish_notation

    def evaluate(self, string):
        reverse_polish_notation = self.get_reverse_polish_notation(string)
        pending = []
        for token in reverse_polish_notation:
            if token in self.operators:
                y, x = pending.pop(), pending.pop()
                pending.append(self.operators[token][1](x, y))
            else:
                pending.append(token)

        return pending[0]

#calculator = Calculator()
#print(calculator.evaluate('2 / 2 + ( 1 + 4 ) + 3 * 4 - 6'))
