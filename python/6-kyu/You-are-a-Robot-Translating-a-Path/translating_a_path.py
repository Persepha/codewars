from itertools import groupby

def get_formatted_instruction(mark, count):
    path_marks = {
        "^": "up",
        "v": "down",
        "<": "left",
        ">": "right",
    }

    return f"Take {count} {'steps' if count > 1 else 'step'} {path_marks.get(mark)}"


def walk(path):
    if not path:
        return "Paused"

    return "\n".join(get_formatted_instruction(x, len(list(group)))
                     for x, group in groupby(path))
