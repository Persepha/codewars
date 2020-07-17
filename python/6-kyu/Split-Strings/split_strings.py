from textwrap import wrap

def solution(s):
    if len(s) % 2:
        s += '_'
    return wrap(s, 2)
